# 🌦️ Weather Prediction Chatbot

A comprehensive Streamlit-based weather prediction application that combines interactive mapping, real-time weather data, and machine learning forecasting. Users can select any location on an OpenStreetMap, get detailed weather information, and predict rainfall using a trained XGBoost model.

## 🚀 Features

### 📍 Interactive Map Selection
   - OpenStreetMap integration using Folium
   - Click anywhere on the map to select coordinates
   - Real-time coordinate display
   - Quick city selection dropdown
   - Manual coordinate input option

### 🎯 Location Confirmation
   - Visual confirmation of selected location
   - Display of latitude and longitude coordinates
   - Select button to confirm the pointed location
   - Reset functionality for new selections

### 🌐 API Integration
   - Automatic extraction of coordinates (latitude/longitude)
   - POST request to weather API endpoint
   - Endpoint: `http://localhost:5678/webhook/rainfall`
   - Comprehensive error handling and debugging
   - Connection testing functionality

### 📊 Weather Display
   - Markdown response rendering
   - Beautiful weather information display
   - 5-day forecast with recommendations
   - Enhanced UI with custom CSS styling

### 🔮 **NEW: XGBoost Rainfall Forecasting**
   - **Machine Learning Prediction**: Advanced rainfall forecasting using trained XGBoost classifier
   - **5 Key Weather Parameters**:
     - Humidity at 3PM (0-100%)
     - Wind Gust Speed (0-100 km/h)
     - Atmospheric Pressure at 3PM (980-1040 hPa)
     - Humidity at 9AM (0-100%)
     - Wind Direction at 3PM (encoded 0-15)
   - **Interactive Input Interface**: User-friendly sliders and dropdowns
   - **Real-time Predictions**: Instant rainfall probability calculations
   - **Visual Results**: 
     - Probability breakdown with confidence metrics
     - Animated progress bars
     - Color-coded prediction results
     - Success animations (balloons for rain predictions)
   - **Model Information**: Built with optimized XGBoost classifier trained on Australian weather data

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Rainfall-Prediction
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install system dependencies (if needed)**
   ```bash
   sudo apt install python3.10-venv  # Ubuntu/Debian
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Weather Information Retrieval

1. **Start the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`

3. **Get weather information**
   - Click on any location on the interactive map
   - OR use "Quick Select Cities" for popular locations
   - OR manually enter coordinates
   - Verify the coordinates displayed
   - Test webhook connection (optional)
   - Click "Confirm Location & Get Weather"
   - View the detailed weather report

### 🔮 **Rainfall Prediction (NEW)**

1. **Access the ML Prediction Section**
   - Scroll down to "Rainfall Prediction using XGBoost"
   - Expand "Weather Parameter Input for Prediction"

2. **Input Weather Parameters**
   - **Humidity 3PM**: Set afternoon humidity percentage (0-100%)
   - **Wind Gust Speed**: Adjust maximum wind speed (0-100 km/h)
   - **Pressure 3PM**: Configure atmospheric pressure (980-1040 hPa)
   - **Humidity 9AM**: Set morning humidity percentage (0-100%)
   - **Wind Direction 3PM**: Select encoded wind direction (0-15)

3. **Get Prediction**
   - Click "🔮 Predict Rainfall Tomorrow"
   - View probability breakdown and confidence metrics
   - See visual prediction results with animations
   - Check parameter summary in expandable section

## 📡 API Information

**Endpoint:** `POST http://localhost:5678/webhook/rainfall`

**Request Format:**
```json
[
  {
    "body": {
      "latitude": 19.21833,
      "longitude": 72.978088
    }
  }
]
```

**Response Format:**
```json
[
  {
    "output": "## 🌦️ Weather Update for Location...(Markdown content)"
  }
]
```

## 🏗️ Technical Stack

### Core Framework
- **Frontend:** Streamlit (Interactive web application)
- **Maps:** Folium + OpenStreetMap (Interactive mapping)
- **HTTP Requests:** Python requests library (API communication)
- **Map Integration:** streamlit-folium (Streamlit-Folium bridge)

### Machine Learning
- **ML Framework:** XGBoost (Gradient boosting classifier)
- **Data Processing:** Pandas + NumPy (Data manipulation)
- **Model Persistence:** Pickle (Model serialization)
- **Feature Engineering:** 5-parameter weather prediction model

### Data Sources
- **Training Data:** Australian weather dataset (weatherAUS.csv)
- **Real-time Weather:** Custom webhook API integration
- **Geolocation:** Interactive coordinate selection

## 📋 Dependencies

### Core Dependencies
- streamlit>=1.50.0
- folium>=0.20.0
- streamlit-folium>=0.25.2
- requests>=2.32.5

### Machine Learning Dependencies
- pandas>=2.0.0
- numpy>=1.24.0
- xgboost>=2.0.0
- scikit-learn>=1.3.0

### Development Dependencies
- pickle (built-in)
- json (built-in)

## 🎨 Features Overview

### Interactive Map
- **OpenStreetMap View:** Full-featured map interface
- **Click Selection:** Point and click location selection
- **Visual Markers:** Red markers for selected locations
- **Coordinate Display:** Real-time lat/lng display

### Weather Integration
- **API Communication:** Seamless webhook integration
- **Error Handling:** Comprehensive error management
- **Response Rendering:** Beautiful markdown display
- **Loading States:** User-friendly loading indicators

### User Interface
- **Responsive Design:** Two-column layout
- **Custom Styling:** Enhanced CSS styling
- **Interactive Elements:** Buttons and status indicators
- **Information Sidebar:** Help and API documentation

## 🔧 Configuration

### Weather API Setup
The application connects to a weather API running on `localhost:5678`. Make sure your weather service (e.g., n8n workflow) is running on this endpoint before using the weather retrieval features.

### XGBoost Model
- **Model File**: `XGB_classifier.pkl` (pre-trained)
- **Training Algorithm**: XGBoost with Optuna hyperparameter optimization
- **Features**: 5 key weather parameters
- **Performance**: Optimized for rainfall prediction accuracy
- **Data**: Trained on Australian Bureau of Meteorology weather data

## 🎯 How It Works

### Weather Information Flow
1. User selects location on interactive map
2. Coordinates are extracted and validated
3. User confirms the location selection
4. App sends POST request to weather API webhook
5. Weather data is retrieved and processed
6. Markdown response is beautifully rendered with recommendations

### 🤖 Machine Learning Prediction Flow
1. User inputs 5 key weather parameters via interactive controls
2. Data is formatted into model-compatible DataFrame
3. Pre-trained XGBoost model processes the input
4. Model returns probability and binary prediction
5. Results are displayed with visual indicators and confidence metrics
6. Parameter summary provided for transparency

## 🧪 Model Details

### Training Information
- **Algorithm**: XGBoost Classifier with hyperparameter optimization
- **Optimization**: Optuna-based parameter tuning (50+ trials)
- **Features**: Selected top 5 most important weather parameters
- **Target**: Binary rainfall prediction (Rain/No Rain tomorrow)
- **Validation**: Stratified cross-validation with ROC-AUC scoring

### Feature Importance Ranking
1. **Humidity3pm** - Afternoon humidity levels
2. **WindGustSpeed** - Maximum wind gust measurements
3. **Pressure3pm** - Afternoon atmospheric pressure
4. **Humidity9am** - Morning humidity levels
5. **WindDir3pm** - Afternoon wind direction (encoded)

## 🌟 Advanced Features

- **Real-time Debugging**: Toggle debug mode to see API requests/responses
- **Multiple Input Methods**: Map clicking, city selection, or manual coordinates
- **Error Handling**: Comprehensive error management for API and model issues
- **Responsive Design**: Optimized for different screen sizes
- **Interactive Visualizations**: Progress bars, animations, and color coding
- **Model Transparency**: Input parameter summaries and confidence metrics

Enjoy exploring weather data and rainfall predictions from anywhere in the world! 🌍🔮