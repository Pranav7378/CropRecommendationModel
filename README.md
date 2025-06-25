<!-- Banner -->
<h1 align="center">🌾 Crop Recommendation Model</h1>
<p align="center">
  <a href="https://croprecommendationmodel.streamlit.app" target="_blank">
    <img alt="Streamlit App" src="https://img.shields.io/badge/Live%20Demo-Open-green?logo=streamlit&logoColor=white">
  </a>
  <img alt="Python" src="https://img.shields.io/badge/Made%20with-Python%203.11-blue?logo=python">
  <img alt="scikit-learn" src="https://img.shields.io/badge/Model-RandomForest-orange">
  <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-lightgrey">
</p>

<div align="center">
  <sub>Predict the optimal crop for any set of soil &amp; climate conditions — in real time.</sub>
</div>

<br/>

<!-- Screenshot -->
<p align="center">
  <a href="https://croprecommendationmodel.streamlit.app" target="_blank">
    <img src="src="App%20Screenshort.png" width="800" alt="App Screenshot">
  </a>
</p>

---

## 🚀 Live Demo
🔗 **[Try it out →](https://croprecommendationmodel.streamlit.app)**  
Enter values for N (Nitrogen), P (Phosphorus), K (Potassium), temperature, humidity, pH, and rainfall — the model instantly suggests the best crop and shows its confidence.

---

## ✨ Features
- **Interactive Streamlit UI** – clean, responsive, dark-mode-friendly  
- **Random Forest Classifier** trained on 2.2 k observations, 95 % validation accuracy  
- **Class-probability table** so users see *why* a crop is chosen  
- **Cached model loading** for sub-second predictions  
- **One-click deploy** (Streamlit Cloud) – zero DevOps required

---

## 🧑‍💻 Tech Stack
| Layer            | Tools / Libraries |
|------------------|-------------------|
| Front-end        | Streamlit 1.35 |
| ML Model         | RandomForest (scikit-learn 1.6.1) |
| Data Wrangling   | Pandas, NumPy |
| Deployment       | Streamlit Community Cloud |
| Language         | Python 3.11 |

---

## 🔬 Dataset
- **Source:** [Kaggle – Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)  
- **Features:** N, P, K, temperature (°C), humidity (%), pH, rainfall (mm)  
- **Target:** 22 possible crops

---

## 🛠️ Local Setup

```bash
# clone the repo
git clone https://github.com/Pranav7378/CropRecommendationModel.git
cd CropRecommendationModel

# create & activate virtual environment (Windows PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# install deps
pip install -r requirements.txt

# run the app
streamlit run streamlitapp.py
