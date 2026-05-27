# Class Vision: Attendance Management System Using Face Recognition

A highly robust, neat, and secure computer vision-based attendance tracking platform. Class Vision automates student cataloging and attendance logging via real-time biometric face detection, local binary descriptors, and pandas-driven spreadsheet consolidation.

---

## 🚀 Key Features

*   **Real-time Facial Biometrics**: Leverages high-accuracy OpenCV Haar Cascade Classifiers to isolate and crop facial regions instantly from the webcam stream.
*   **LBPH Recognition Classifier**: Integrates **Local Binary Patterns Histograms (LBPH)**, a robust spatial-texture face recognition model that is highly resilient to variations in lighting, background noise, and pose.
*   **Intuitive Desktop Dashboard**: A beautifully organized dark-themed Tkinter GUI, with vibrant interactive buttons, stylized icons, and clear tabular data viewers.
*   **Auditory Feedback System**: Features built-in Text-to-Speech (TTS) vocal guidance using `pyttsx3` to provide audible cues, warnings, and success confirmations.
*   **Merged Attendance Analytics**: Automatically matches, aggregates, and computes attendance statistics (such as attendance percentage) across all active sessions using Pandas.
*   **Manual Administration Console**: Includes a secure manual entry desktop portal (`takemanually.py`) to mark attendance when biometric capture is unavailable.

---

## 🛠️ System Architecture

Below is the logical workflow of the Attendance Management System:

```mermaid
graph TD
    A[Launch Dashboard] --> B[Register Student Details]
    B --> C[Webcam Face Crops Capture]
    C --> D[Save Samples to local TrainingImage]
    D --> E[Run Model Trainer]
    E --> F[Generate TrainingImageLabel/Trainner.yml]
    F --> G[Fill Attendance via Real-Time WebCam]
    G --> H[Check Confidence & Match database CSV]
    H --> I[Mark Present with DateTime Logs]
    I --> J[Consolidate Subject Sheets]
    J --> K[Generate Attendance Analytics Report]
```

---

## 📂 File Anatomy

The project directory is structured cleanly to separate presentation layers, computational models, database records, and generated assets:

```text
├── Attendance/                      # Consolidated and session-level CSVs per subject
│   ├── math/
│   └── phy/
├── Attendance(Manually)/            # Manually recorded attendance logs
├── StudentDetails/                  # Student registration data
│   └── studentdetails.csv           # Maps Enrollment ID -> Name
├── TrainingImageLabel/              # Directory holding trained models
│   └── Trainner.yml                 # Serialized LBPH recognition weights
├── UI_Image/                        # Image assets for the GUI dashboard
├── attendance.py                    # Main launcher and central dashboard dashboard
├── automaticAttedance.py            # Real-time face detection & marking module
├── takeImage.py                     # Captures cropped facial datasets
├── trainImage.py                    # Builds and saves the LBPH model
├── show_attendance.py               # Aggregates, calculates percentages, & renders data tables
├── takemanually.py                  # Standalone manual attendance administrator
└── haarcascade_frontalface_default.xml  # Haar Cascade Frontal Face model
```

---

## 📦 Prerequisites & System Setup

### 1. Requirements

*   **Operating System**: Windows (Tested and verified) or macOS/Linux.
*   **Python**: Version 3.6 or higher.

### 2. Installation Steps

Clone the repository or navigate to the project directory, then install the necessary dependencies using your preferred terminal tool:

```bash
pip install -r requirements.txt
```

#### Content of `requirements.txt`:
*   `numpy` (Linear algebra & matrix array operations)
*   `opencv-contrib-python` (OpenCV with extra modules including face recognition)
*   `opencv-python` (Core Computer Vision tools)
*   `openpyxl` (Excel sheet engines)
*   `pandas` (Consolidation and data manipulation)
*   `pillow` (Advanced image resizing and loading for GUI)
*   `pyttsx3` (Offline Text-to-Speech library)

---

## 🖥️ Operational User Guide

Follow these steps to run and test the complete attendance pipeline:

### Step 1: Start the Dashboard
Launch the central application:
```bash
python attendance.py
```

### Step 2: Register a New Student
1. Click **Register a new student**.
2. Enter a unique integer **Enrollment No** (e.g., `101`) and the student's **Name** (e.g., `Alice`).
3. Click **Take Image**.
   * The webcam will activate.
   * Sit comfortably in standard lighting. The algorithm will capture and store **50 cropped grayscale face frames** inside the `./TrainingImage` folder.
   * You will hear a speech confirmation when complete.

### Step 3: Train the Biometric Model
1. Once images are recorded, click **Train Image** on the registration screen.
2. The LBPH engine will compile the facial characteristics and serialize the weights file into `TrainingImageLabel/Trainner.yml`.

### Step 4: Run Real-time Automatic Attendance
1. On the main dashboard, click **Take Attendance**.
2. Input the Subject Name (e.g., `math`) and click **Fill Attendance**.
3. The webcam launches:
   * **Recognized Faces**: Rendered with a **green bounding box** showing their `ID - Name`.
   * **Unknown Faces**: Rendered with a **red bounding box** showing `Unknown`.
4. Press `q` or `ESC` (or wait for the timer to complete) to close the camera stream.
5. The session attendance file will be generated instantly and shown in a neat grid display.

### Step 5: View Consolidated Reports & Percentages
1. Click **View Attendance** on the dashboard.
2. Enter the subject name (e.g. `math`) and click **View Attendance**.
3. The program will scan all past session sheets, calculate the **average attendance percentage** for each student, and display the consolidated master file (`attendance.csv`).

---

## 🔒 Code Optimizations & Safety Improvements

The following codebase fixes have been deployed:
1.  **Resolved Drive Root Folder Creation**: Relocated `TrainingImage` folder creation from absolute path (`/TrainingImage`) to safe local workspace directories (`./TrainingImage`).
2.  **Fixed String Escape Pathing Errors**: Replaced manual backslash string additions (like `f"{path}\ "`) with clean, platform-independent `os.path.join` operations inside `takeImage.py`.
3.  **Corrected Double Path Merging Crashes**: Resolved the critical bug in `automaticAttedance.py` where a folder path was joined twice (e.g., `Attendance/math/Attendance/math/...`), preventing runtime failures when writing and reading sheet tables.
4.  **Bulletproofed Dataset File Validation**: Added file format checks and folder existence guards inside `trainImage.py` to filter out stray non-image files and directory structures safely.
5.  **Removed Hardcoded Paths**: Cleaned up manual check sheet paths in `takemanually.py` that pointed to unavailable user profiles, replacing them with dynamic Windows file system launchers.

---

## 📝 License & References

*   **Haar Cascade Classifiers**: Developed and licensed by Intel under the standard 3-clause BSD License ([OpenCV Cascades GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)).
*   **LBPH Recognition**: Supported through `opencv-contrib-python` wrappers.
