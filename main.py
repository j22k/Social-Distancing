import cv2
import numpy as np
from ultralytics import YOLO
import time

# Initialize the YOLOv8 model
model = YOLO('yolov8n.pt')  # Ensure you have the 'yolov8n.pt' model file

# Parameters
DISTANCE_THRESHOLD = 1.5  # meters
calibration_mode = True
image_points = []
world_points = []

# Mouse callback function to capture image points
def click_event(event, x, y, flags, param):
    global image_points, world_points, calibration_mode
    if event == cv2.EVENT_LBUTTONDOWN and calibration_mode:
        print(f"Clicked at pixel coordinates: ({x}, {y})")
        real_x = float(input("Enter real-world X coordinate (meters): "))
        real_y = float(input("Enter real-world Y coordinate (meters): "))
        image_points.append([x, y])
        world_points.append([real_x, real_y])
        if len(image_points) >= 4:
            calibration_mode = False
            print("Collected sufficient points. Exiting calibration mode.")

# Function to compute homography matrix
def compute_homography():
    global image_points, world_points
    if len(image_points) >= 4:
        H, _ = cv2.findHomography(np.array(image_points, dtype=np.float32),
                                  np.array(world_points, dtype=np.float32))
        return H
    else:
        raise ValueError("Insufficient points for homography calculation.")

# Function to transform image coordinates to real-world coordinates
def image_to_world(image_point, H):
    point = np.array([image_point[0], image_point[1], 1.0], dtype=np.float32).reshape((3, 1))
    world_point = np.dot(H, point)
    world_point /= world_point[2, 0]
    return (world_point[0, 0], world_point[1, 0])

# Open a connection to the webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam
cv2.namedWindow('Distance Measurement')
cv2.setMouseCallback('Distance Measurement', click_event)

homography_matrix = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if calibration_mode:
        cv2.putText(frame, "Calibration Mode: Click 4 points and enter real-world coordinates",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    else:
        if homography_matrix is None:
            homography_matrix = compute_homography()

        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Extract bounding boxes and class IDs
        boxes = results[0].boxes.xyxy.cpu().numpy()
        class_ids = results[0].boxes.cls.cpu().numpy()

        # Filter detections for persons (class ID 0)
        person_indices = np.where(class_ids == 0)[0]
        person_boxes = boxes[person_indices]

        # List to store real-world coordinates of detected persons
        real_world_points = []

        for box in person_boxes:
            x1, y1, x2, y2 = box
            bottom_center = (int((x1 + x2) / 2), int(y2))
            real_world_point = image_to_world(bottom_center, homography_matrix)
            real_world_points.append(real_world_point)

            # Draw bounding box and label on the frame
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, 'Person', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Calculate distances between each pair of persons
        for i in range(len(real_world_points)):
            for j in range(i + 1, len(real_world_points)):
                point1 = real_world_points[i]
                point2 = real_world_points[j]
                distance = np.linalg.norm(np.array(point1) - np.array(point2))

                # Display the distance on the frame
                midpoint = (int((person_boxes[i][0] + person_boxes[j][0]) / 2),
                            int((person_boxes[i][1] + person_boxes[j][1]) / 2))
                cv2.putText(frame, f'{distance:.2f} meters', midpoint,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # Check if distance is below threshold
                if distance < DISTANCE_THRESHOLD:
                    cv2.putText(frame, 'ALERT: Distance Violation', (10, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    # Log the violation
                    with open("distance_violations.log", "a") as log_file:
                        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Distance violation: {distance:.2f} meters\n")

    # Display the frame
    cv2.imshow('Distance Measurement', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break