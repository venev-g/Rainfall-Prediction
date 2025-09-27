# 🚀 Quick Setup Guide

## Prerequisites
- Python 3.10 or higher
- Git (for cloning repository)

## Installation Steps

1. **Clone and Navigate**
   ```bash
   git clone https://github.com/venev-g/Rainfall-Prediction.git
   cd Rainfall-Prediction
   ```

2. **Setup Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   streamlit run app.py
   ```

5. **Access Application**
   - Open browser to: `http://localhost:8501`

## 🎯 Key Features Available

### 🗺️ Interactive Weather Map
- Click any location on the world map
- Get real-time weather data via API
- 5-day forecast with recommendations

### 🤖 AI Rainfall Prediction
- Input 5 weather parameters:
  - Humidity (9AM & 3PM)
  - Wind Gust Speed  
  - Atmospheric Pressure
  - Wind Direction
- Get AI-powered rainfall probability
- Visual results with confidence metrics

## 📁 Project Structure
```
Rainfall-Prediction/
├── app.py                 # Main Streamlit application
├── XGB_classifier.pkl     # Trained XGBoost model
├── XGB_Rainfall.ipynb     # Model training notebook
├── test_model.py         # Model testing script
├── test_webhook.py       # API testing script
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🔧 Troubleshooting

### Common Issues:
1. **Import Errors**: Ensure virtual environment is activated
2. **Model Not Found**: Check `XGB_classifier.pkl` exists in project root
3. **API Connection**: Verify n8n/webhook service running on port 5678
4. **Streamlit Issues**: Try `streamlit run app.py --server.port 8502`

### Debug Mode:
- Enable "Show Debug Info" in the app for API troubleshooting
- Use "Test Webhook Connection" to verify API availability

Enjoy predicting the weather! 🌦️✨