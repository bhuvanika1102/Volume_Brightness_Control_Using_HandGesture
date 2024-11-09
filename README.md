# Hand Gesture Control for Volume and Brightness

This project allows users to control their computer's volume and screen brightness using hand gestures. The program uses hand landmarks detection with the help of **MediaPipe** to track hand movements, and based on the gestures, it adjusts the volume and brightness. The thumb and index finger's distance is used to control brightness, and the left and right hands are used for controlling volume.

## Features:
- **Brightness Control**: The distance between the thumb and index finger adjusts the screen brightness.
- **Volume Control**: Hand gestures (thumb above index finger for volume up, thumb below index finger for volume down) control the system volume.
- **Full-Screen Mode**: The application runs in full-screen mode, showing the camera feed with detected hand landmarks.

## Requirements:
- **Python 3.x**
- **Libraries**:
  - `opencv-python` (OpenCV for computer vision tasks)
  - `mediapipe` (for hand gesture recognition)
  - `numpy` (for numerical operations)
  - `pyautogui` (for simulating keypresses to control system volume)
  - `screen_brightness_control` (to adjust screen brightness)

## Installation and Setup:

### 1. Clone the repository:
```bash
git clone https://github.com/bhuvanika1102/Volume_Brightness_Control_Using_Handgesture.git
cd hand-gesture-control
```
### 2. Install dependencies:
Make sure you have Python 3 installed, then use the following command to install the required libraries:

```bash
pip install opencv-python mediapipe numpy pyautogui screen_brightness_control
```
### 3. Configure your environment:
For screen brightness control, this script uses screen_brightness_control, which works on Windows, macOS, and Linux. You might need additional setup depending on your operating system.
PyAutoGUI is used to control the volume through key presses, so ensure your keyboard's volume control keys are mapped correctly.
How to Run:
After installing the required dependencies, run the script using:
```bash
python main.py
```
The script will open the webcam and enter a loop where it will:

Track hand gestures and display the landmarks on the screen.
Adjust screen brightness when the thumb and index fingers move apart or together.
Increase or decrease system volume using hand gestures with your right hand.
`To exit the application, press q on your keyboard.`

### Known Limitations:
The accuracy of hand tracking may vary depending on the lighting conditions and camera quality.
The system volume control uses the volume up and down keys (default), so it may not work for all systems or may require specific hotkey configurations.
The brightness control uses screen_brightness_control, which should work on most systems but may require additional setup.


## Contact
For any questions or comments, please reach out bhuvani1102@gmail.com.
