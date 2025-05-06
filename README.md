# EmoLens - Human Sentimental Analysis Through Image Recognition

## 👁️ Overview

**EmoLens** is an AI-powered facial emotion recognition tool that classifies human emotions—such as happiness, sadness, and neutrality—using deep learning. This project combines computer vision, CNN-based modeling, and a user-friendly web interface to provide real-time emotional insights. EmoLens is applicable in diverse fields such as healthcare, education, customer service, marketing, and more.

---

## 👥 Team Members

- **Riya Singhal**
- **Mohd Aman**
- **Sujal Singh**

**Under the Supervision of**  
Dr. Amar Saraswat  
**Institution**: School of Engineering and Technology

---

## 🚀 Features

- 🔍 Real-time facial emotion detection using CNN.
- 💻 Web-based UI for image uploads and emotion prediction.
- 🔐 Privacy-conscious emotion tracking.
- 📊 Long-term emotional trend monitoring (future enhancement).

---

## 📽️ Project Demo

Watch the full demonstration on Google Drive:  
🔗 [EmoLens Demo Video](https://drive.google.com/file/d/1JOi4ThDSHyN6wDcMk7Kd4zY49UAxaP4o/view?usp=sharing)

---

## 📄 Project Documents

- 📊 [EmoLens Presentation (PPT)](https://docs.google.com/presentation/d/19Zo6oQc1ed_enSumKacjj3-OCOVgwEsV/edit?usp=drive_link&ouid=100608468618828059343&rtpof=true&sd=true)
- 📝 [EmoLens Report (PDF)](https://drive.google.com/file/d/1eLSE7TzPLjBOY5GoaC9LrybovUpkum6N/view?usp=sharing)

---

## 🎯 Objectives

- Develop an emotion recognition system using image classification.
- Improve prediction accuracy via CNN optimization.
- Deploy an accessible web application with real-time analysis.
- Ensure data privacy and ethical AI usage.

---

## 🔍 Problem Statement

- Subtle expressions lead to emotional misclassification.
- Limited and imbalanced datasets hinder training.
- Real-time processing requires optimized models.
- Scalability across devices poses deployment challenges.

---

## ⚙️ Tech Stack

### 👨‍💻 Frontend
- HTML, CSS, JavaScript
- React.js

### 🧠 Backend & AI
- Python with Flask
- TensorFlow/Keras (CNN for emotion recognition)
- OpenCV (Image preprocessing & face detection)

### 🗂️ Others
- Local file storage for uploaded images
- FER-2013 and CK+ datasets

---

## 🧪 Methodology

1. **Define Objectives** and expected outcomes.
2. **Collect & Prepare Data** using FER-2013, CK+.
3. **Preprocess Images**: Resize, grayscale, normalize with OpenCV.
4. **Build CNN Model** using TensorFlow/Keras.
5. **Train & Validate** model for real-world accuracy.
6. **Deploy Web App** using Flask.

---

## 🧩 Challenges & Solutions

| Challenge                 | Cause                      | Solution                               |
|--------------------------|---------------------------|----------------------------------------|
| Limited labeled data      | Dataset size               | Data augmentation, expand samples      |
| Overfitting               | Model memorization         | Dropout, regularization techniques     |
| Real-time lag             | Model complexity           | Use of optimized CNNs, TensorFlow Lite |
| Deployment on web/mobile  | Heavy model size           | Convert models to lightweight versions |
| Privacy concerns          | User data usage            | Encryption and consent mechanisms      |

---

## 💡 Future Enhancements

- Add multimodal emotion analysis (voice, gestures).
- Deploy on mobile using **TensorFlow Lite**.
- Improve model with a more diverse dataset.
- Integrate secure user accounts for emotion tracking.

---

## 🔧 Installation & Setup

### 📦 Prerequisites

- Python 3.10+
- Flask
- TensorFlow / Keras
- OpenCV

### 🛠️ Steps to Run

```bash
# Clone the repository
git clone https://github.com/amansaif/Mohd_Aman_Section_C_Emolens.git
cd Mohd_Aman_Section_C_Emolens

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py

# Open in browser
http://localhost:5000
