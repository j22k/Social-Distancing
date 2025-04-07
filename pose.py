import cv2
import torch
import torchvision.transforms as transforms
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load MiDaS model for depth estimation
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
midas.eval()

# Define transformation for MiDaS input
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform pose estimation
    results = pose.process(rgb_frame)

    # Apply transformations and perform depth estimation
    input_image = transform(rgb_frame).unsqueeze(0)
    with torch.no_grad():
        depth_map = midas(input_image).squeeze().cpu().numpy()

    # Resize depth map to match frame size
    depth_map = cv2.resize(depth_map, (frame.shape[1], frame.shape[0]))

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            x = int(landmark.x * frame.shape[1])
            y = int(landmark.y * frame.shape[0])

            # Ensure coordinates are within valid range
            x = max(0, min(x, frame.shape[1] - 1))
            y = max(0, min(y, frame.shape[0] - 1))

            depth = depth_map[y, x]

            # Visualize 2D keypoints
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            # Display depth information
            cv2.putText(frame, f'Depth: {depth:.2f}', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow('Pose and Depth Estimation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()