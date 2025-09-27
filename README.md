# 🌦️ Weather Prediction Chatbot

A Streamlit-based interactive weather prediction application that allows users to select any location on an OpenStreetMap and get detailed weather information.

## 🚀 Features

1. **📍 Interactive Map Selection**
   - OpenStreetMap integration using Folium
   - Click anywhere on the map to select coordinates
   - Real-time coordinate display

2. **🎯 Location Confirmation**
   - Visual confirmation of selected location
   - Display of latitude and longitude coordinates
   - Select button to confirm the pointed location

3. **🌐 API Integration**
   - Automatic extraction of coordinates (latitude/longitude)
   - POST request to weather API endpoint
   - Endpoint: `http://localhost:5678/webhook/rainfall`

4. **📊 Weather Display**
   - Markdown response rendering
   - Beautiful weather information display
   - 5-day forecast with recommendations

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

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Start the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`

3. **Use the application**
   - Click on any location on the interactive map
   - Verify the coordinates displayed
   - Click "Confirm Location & Get Weather"
   - View the detailed weather report

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

- **Frontend:** Streamlit
- **Maps:** Folium + OpenStreetMap
- **HTTP Requests:** Python requests library
- **Map Integration:** streamlit-folium

## 📋 Dependencies

- streamlit==1.50.0
- folium==0.20.0
- streamlit-folium==0.25.2
- requests==2.32.5

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

The application connects to a weather API running on `localhost:5678`. Make sure your weather service is running on this endpoint before using the application.

## 🎯 How It Works

1. User clicks on the interactive map
2. Coordinates are extracted and displayed
3. User confirms the location selection
4. App sends POST request to weather API
5. Weather data is retrieved and displayed
6. Markdown response is beautifully rendered

Enjoy exploring weather data from anywhere in the world! 🌍