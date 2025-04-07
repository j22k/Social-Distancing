Absolutely! Here's a professional and informative `README.md` file tailored for your **Real-World Distance Measurement System using Computer Vision and YOLOv8**, which you can directly use in your GitHub repository.

---

```markdown
# Real-World Distance Measurement using YOLOv8 and OpenCV

This project is a foundational component of a larger **Forklift Collision Monitoring System**, developed during our internship at **ZoftCares Solutions LLP**. It demonstrates how to estimate real-world distances between detected people using a standard webcam and computer vision techniques. The core idea is to use camera calibration and object detection to evaluate distances and flag proximity violations in real time.

---

## 🚀 Features

- 📷 Real-time video feed via webcam
- 🤖 Object detection using YOLOv8 (focused on detecting people)
- 🧮 Manual calibration using 4 or more points to compute real-world transformation
- 📏 Real-world distance measurement (in meters) between detected individuals
- ⚠️ Visual and logged alerts when safety distance is breached
- 📝 Logs stored with timestamps for future analysis

---

## 🔧 How It Works

1. **Calibration Mode**  
   When the program starts, users are prompted to click on **at least 4 known reference points** in the video feed and manually enter their real-world coordinates. These points are used to compute a **homography matrix** that transforms image coordinates to real-world positions.

2. **Object Detection**  
   YOLOv8 (`yolov8n.pt` or any custom weights) is used to detect people in the frame.

3. **Distance Calculation**  
   For each detected person, the bottom-center of the bounding box is transformed to real-world coordinates. Pairwise distances are then computed and displayed on the screen.

4. **Violation Alerts**  
   If the distance between any two individuals is below the defined threshold (e.g., 1.5 meters), an on-screen alert is shown and a message is appended to a `distance_violations.log` file.

---

## 📁 Folder Structure

```
├── distance_measurement.py     # Main script
├── yolov8n.pt                  # YOLOv8 model weights (download required)
├── distance_violations.log     # Log of all distance violations
└── README.md                   # Project documentation
```

---

## 🛠️ Requirements

Install the dependencies using pip:

```bash
pip install ultralytics opencv-python numpy
```

Make sure you have YOLOv8 installed. If not:

```bash
pip install ultralytics
```

---

## ▶️ Usage

Run the script:

```bash
python distance_measurement.py
```

1. A window will open showing the webcam feed.
2. Click on four or more known points (e.g., floor corners) and input their real-world coordinates.
3. After calibration, the system will start detecting people and computing distances.
4. Press `q` to quit the application.

---

## ⚙️ Parameters

- `DISTANCE_THRESHOLD`: Set in meters; if the real-world distance between two people falls below this, an alert is triggered.

---

## 📓 Example Use Case

This project is designed to be extended for safety monitoring in industrial environments, such as:
- Warehouse zones where forklifts and workers operate in close proximity
- COVID-19 social distancing enforcement
- Construction site safety compliance

---

## 🔗 Related Work

This project is part of a broader system:  
**AI-Based Forklift Collision Monitoring using Computer Vision**

Future enhancements will include:
- Forklift detection and classification
- Speed estimation
- Real-time alert dashboard
- Integration with industrial surveillance systems

---

## 👨‍💻 Developed By

- Muhammed Junaid K  
- Muhammed Shahiq  
- Muhammed Ajnas KP  
- Muhhammed Musthafa  

Internship @ **ZoftCares Solutions LLP**  
Date: **April 6, 2025**

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

---

Let me know if you'd like a version in PDF, or want me to help generate a GitHub repo structure or badge icons for version, license, etc.