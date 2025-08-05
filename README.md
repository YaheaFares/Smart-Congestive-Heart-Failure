# Smart-Congestive-Heart-Failure
A complete IoT + AI solution to monitor SpO₂ and heart rate for congestive heart failure patients, powered by ESP32, MAX30100 sensor, SIM800L GSM module, and a Flutter mobile app with AI-based risk prediction.
<!-- Optional: Add an image/gif of your project --> 
🚀 Features
✅ Real-time measurement of SpO₂ and heart rate using MAX30100 sensor
✅ Wireless data transmission to Flutter mobile app via Wi-Fi
✅ Integrated AI model in the app to predict oxygen shortness risk
✅ Automatic emergency SMS alert via SIM800L to patient’s family
✅ User-friendly Flutter UI for continuous monitoring
✅ Built on affordable and widely available hardware (ESP32, MAX30100, SIM800L)
🛠️ Hardware Used
ESP32 Dev Module
MAX30100 Pulse Oximeter Sensor
SIM800L GSM Module (for sending SMS alerts)
Power Supply (e.g., LiPo battery or USB 5V)
Optional: OLED/TFT display for local display
📱 Mobile App
Developed with Flutter, the app:
Displays live SpO₂ and heart rate readings
Integrates a lightweight AI model in the backend to classify patient state
Sends commands back to ESP32 for SMS alerts if abnormal patterns are detected
Provides a clean and intuitive interface
🤖 AI Integration
The AI model (TensorFlow Lite or custom classifier) predicts shortness of oxygen risk based on real-time heart rate and SpO₂ data.
Triggers an alert if thresholds or patterns indicate potential health deterioration.
🔔 How it Works
1️⃣ ESP32 reads SpO₂ & heart rate from MAX30100
2️⃣ Data is sent over Wi-Fi to the Flutter app
3️⃣ AI model analyzes the data
4️⃣ If oxygen shortness risk detected, app sends a command to ESP32
5️⃣ ESP32 uses SIM800L to send SMS alert to patient’s family
6️⃣ Family members can assist the patient immediately
📷 Screenshots
App DashboardAI Risk Prediction
📝 How to Build
Hardware Setup
Connect MAX30100 to ESP32 via I2C (SCL/SDA)
Connect SIM800L TX/RX pins to ESP32 UART (use level shifter if needed)
Power ESP32 and SIM800L appropriately.
ESP32 Firmware
Flash your ESP32 with the provided Arduino/PlatformIO code in /firmware.
Mobile App
Clone the Flutter project in /flutter_app.
Run flutter pub get.
Build and install the app on your mobile device.
AI Model
Place your trained model file (e.g., model.tflite) in the app assets directory.
Update inference logic as needed.
SMS Configuration
Set the recipient phone numbers in the ESP32 firmware.
Test sending SMS manually before relying on automatic alerts.
📦 Repository Structure
bash
Copy code
├── firmware/ # ESP32 Arduino/PlatformIO code ├── flutter_app/ # Flutter mobile app source code ├── ai_model/ # Scripts & notebooks for training AI model └── README.md # This file 
🩺 Use Cases
✅ Patients with congestive heart failure (CHF)
✅ Elderly individuals needing remote oxygen monitoring
✅ Hospitals or caregivers seeking low-cost early-warning systems
✨ Future Improvements
Add fall detection with MPU6050 or accelerometer
Push notifications via Firebase instead of SMS
Cloud integration for doctor dashboards
Extended AI model with more vital signs (temperature, BP, ECG)
📄 License
This project is open-sourced under the MIT License. See LICENSE for details.
🙌 Acknowledgments
Special thanks to open-source libraries, the ESP32 and Flutter communities, and everyone working to make affordable healthcare technology accessible.
