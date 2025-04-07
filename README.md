Here’s a **professional README** for your distance monitoring and violation detection system using YOLOv8 and OpenCV. This version is structured to clearly explain the purpose, setup, usage, and features of your project while maintaining a developer-friendly tone:

---

# 📏 Real-Time Social Distance Monitoring System using YOLOv8 and OpenCV

This project implements a real-time social distancing monitoring system using the **YOLOv8** object detection model and **OpenCV**. The system detects individuals in a video feed, computes real-world distances between them using a homography matrix based on user-provided calibration points, and logs violations if individuals come too close based on a configurable distance threshold.

---

## 🚀 Features

- **Real-time person detection** using YOLOv8.
- **User-assisted perspective calibration** using manual input to map image points to real-world coordinates.
- **Homography transformation** to convert pixel coordinates into real-world measurements.
- **Live distance computation** between all detected individuals.
- **Visual alerts** and **log file creation** for any distance violations.
- **Configurable distance threshold** for flexibility in different environments.

---

## 🧠 Technologies Used

- [YOLOv8](https://github.com/ultralytics/ultralytics): Lightweight real-time object detection.
- OpenCV: Video capture, annotation, and transformation.
- NumPy: Mathematical operations and matrix transformations.
- Python 3.x

---

## 🛠️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/social-distance-monitoring.git
   cd social-distance-monitoring
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download YOLOv8 Model Weights**

   Ensure you have the YOLOv8 Nano model (`yolov8n.pt`). You can download it from the [Ultralytics model hub](https://github.com/ultralytics/ultralytics/releases).

---

## 📷 Calibration Instructions

1. **Launch the application**
   ```bash
   python main.py
   ```

2. **Calibration mode will activate on start**
   - Click **4 points** on the video feed that correspond to known real-world coordinates.
   - After each click, input the **real-world (X, Y) coordinates in meters** in the terminal.
   - Once 4 points are collected, the calibration mode automatically ends, and distance measurement starts.

---

## 🖥️ Usage

- Run the script:
  ```bash
  python main.py
  ```

- Press `Q` to exit the program gracefully.
- Any detected violations (people closer than the set threshold) are:
  - Displayed live on the video.
  - Logged into `distance_violations.log` with a timestamp and distance value.

---

## 🔧 Configuration

You can customize the following parameters in the script:

```python
DISTANCE_THRESHOLD = 1.5  # Minimum distance in meters considered safe
```

---

## 📂 File Structure

```bash
├── main.py                    # Main application script
├── yolov8n.pt                 # YOLOv8 Nano model weights
├── distance_violations.log    # Log file for violations
├── requirements.txt           # Python dependencies
```

---

## 📈 Example Output

- Bounding boxes drawn around detected people
- Labels indicating "Person"
- Red text showing measured distance (in meters)
- On-screen alert: "ALERT: Distance Violation" when too close
- Timestamped log entry saved to `distance_violations.log`

---

## 🧪 Future Improvements

- Automate calibration with ArUco markers or checkerboard pattern
- Add support for tracking individuals over time
- Visualize zones of risk with a heatmap
- Deploy via Flask or Streamlit for remote access
- Add sound alerts for violations

---

## 👤 Author

**Your Name**  
[Your GitHub](https://github.com/yourusername)  
Email: your.email@example.com  

