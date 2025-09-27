import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Weather Prediction Chatbot",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2E86AB;
        font-size: 3em;
        margin-bottom: 1em;
    }
    
    .subtitle {
        text-align: center;
        color: #A23B72;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    
    .coordinates-box {
        background-color: #F18F01;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .weather-response {
        background-color: #f0f2f6;
        border-left: 5px solid #2E86AB;
        padding: 20px;
        border-radius: 5px;
        margin: 20px 0;
    }
    
    .map-container {
        border: 2px solid #2E86AB;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Title and description
    st.markdown('<h1 class="main-title">🌦️ Weather Prediction Chatbot 🌍</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Select any location on the map to get detailed weather information</p>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'selected_location' not in st.session_state:
        st.session_state.selected_location = None
    if 'coordinates' not in st.session_state:
        st.session_state.coordinates = None
    if 'weather_response' not in st.session_state:
        st.session_state.weather_response = None
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        st.subheader("🗺️ Interactive Map")
        st.info("🔍 Click on any location on the map to select coordinates for weather prediction")
        
        # Quick location selector
        with st.expander("🏙️ Quick Select Cities", expanded=False):
            cities = {
                "Mumbai, India": [19.0760, 72.8777],
                "Delhi, India": [28.6139, 77.2090],
                "Bangalore, India": [12.9716, 77.5946],
                "Chennai, India": [13.0827, 80.2707],
                "Kolkata, India": [22.5726, 88.3639],
                "New York, USA": [40.7128, -74.0060],
                "London, UK": [51.5074, -0.1278],
                "Tokyo, Japan": [35.6762, 139.6503]
            }
            
            selected_city = st.selectbox("Choose a city:", list(cities.keys()))
            if st.button(f"📍 Select {selected_city}", use_container_width=True):
                coords = cities[selected_city]
                st.session_state.selected_location = coords
                st.session_state.coordinates = {
                    'latitude': coords[0],
                    'longitude': coords[1]
                }
                st.session_state.weather_response = None
                st.success(f"📍 {selected_city} selected!")
                st.rerun()
        

        
        # Create the folium map
        m = folium.Map(
            location=[20.5937, 78.9629],  # Center of India
            zoom_start=5,
            tiles='OpenStreetMap',
            prefer_canvas=True  # Better for click detection
        )
        
        # Add a marker if location is already selected
        if st.session_state.selected_location:
            folium.Marker(
                st.session_state.selected_location,
                popup=f"Selected Location\nLat: {st.session_state.selected_location[0]:.6f}\nLon: {st.session_state.selected_location[1]:.6f}",
                tooltip="Selected Location",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
        
        # Display the map and capture clicks
        map_data = st_folium(
            m, 
            width=700, 
            height=500,
            key="weather_map",
            returned_objects=["last_clicked", "last_object_clicked", "bounds", "zoom"]
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle map clicks - Improved logic with multiple detection methods
        clicked_location = None
        
        # Method 1: Direct click detection
        if map_data.get('last_clicked'):
            clicked_location = map_data['last_clicked']
        
        # Method 2: Check if there's any click data in the map_data
        elif hasattr(map_data, 'get') and map_data:
            for key in ['last_clicked', 'clicked']:
                if map_data.get(key):
                    clicked_location = map_data[key]
                    break
        
        # Process the clicked location
        if clicked_location and 'lat' in clicked_location and 'lng' in clicked_location:
            clicked_lat = clicked_location['lat']
            clicked_lng = clicked_location['lng']
            
            # Only update if coordinates are different from current selection
            if (st.session_state.coordinates is None or 
                abs(st.session_state.coordinates.get('latitude', 0) - clicked_lat) > 0.0001 or
                abs(st.session_state.coordinates.get('longitude', 0) - clicked_lng) > 0.0001):
                
                st.session_state.selected_location = [clicked_lat, clicked_lng]
                st.session_state.coordinates = {
                    'latitude': clicked_lat,
                    'longitude': clicked_lng
                }
                # Clear previous weather response when new location is selected
                st.session_state.weather_response = None
                st.rerun()
        
        # Debug information (moved here to access map_data)
        if st.checkbox("Show Debug Info", key="debug_checkbox", help="Display map interaction details"):
            st.write("**Map Click Data:**", map_data.get('last_clicked', 'No clicks detected'))
            st.write("**Map Object Data:**", map_data.get('last_object_clicked', 'No object clicks'))
            if st.session_state.coordinates:
                st.write("**Current Coordinates:**", st.session_state.coordinates)
    
    with col2:
        st.subheader("📍 Location Details")
        
        # Prominent instruction
        if not st.session_state.coordinates:
            st.warning("👈 Click on the map to select a location!")
        
        # Manual coordinate input as backup
        with st.expander("🎯 Manual Coordinate Input", expanded=False):
            col_lat, col_lng = st.columns(2)
            with col_lat:
                manual_lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.000001, format="%.6f")
            with col_lng:
                manual_lng = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.000001, format="%.6f")
            
            if st.button("📍 Use Manual Coordinates", use_container_width=True):
                st.session_state.selected_location = [manual_lat, manual_lng]
                st.session_state.coordinates = {
                    'latitude': manual_lat,
                    'longitude': manual_lng
                }
                st.session_state.weather_response = None
                st.success(f"📍 Manual coordinates set: {manual_lat:.6f}, {manual_lng:.6f}")
                st.rerun()
        
        # Display selected coordinates
        if st.session_state.coordinates:
            st.markdown('<div class="coordinates-box">', unsafe_allow_html=True)
            st.success("✅ Location Selected!")
            st.write(f"**Latitude:** {st.session_state.coordinates['latitude']:.6f}")
            st.write(f"**Longitude:** {st.session_state.coordinates['longitude']:.6f}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Test webhook connectivity button
            if st.button("🔍 Test Webhook Connection", use_container_width=True):
                test_webhook_connection()
            
            # Confirm selection button
            if st.button("🎯 Confirm Location & Get Weather", type="primary", use_container_width=True):
                with st.spinner("🌐 Fetching weather data..."):
                    weather_data = get_weather_data(st.session_state.coordinates)
                    if weather_data:
                        st.session_state.weather_response = weather_data
                        st.success("🌦️ Weather data retrieved successfully!")
                    else:
                        st.error("❌ Failed to retrieve weather data. Please try again.")
        else:
            st.info("👆 Click on the map to select a location")
            st.write("**Steps:**")
            st.write("1. 🖱️ Click anywhere on the map")
            st.write("2. 📍 Coordinates will appear here")
            st.write("3. ✅ Confirm to get weather data")
        
        # Reset button
        if st.button("🔄 Reset Selection", use_container_width=True):
            st.session_state.selected_location = None
            st.session_state.coordinates = None
            st.session_state.weather_response = None
            st.rerun()
    
    # Display weather response
    if st.session_state.weather_response:
        st.markdown("---")
        st.subheader("🌤️ Weather Information")
        st.markdown('<div class="weather-response">', unsafe_allow_html=True)
        st.markdown(st.session_state.weather_response, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def get_weather_data(coordinates):
    """
    Send coordinates to the weather API and return the response
    """
    try:
        # API endpoint
        api_url = "http://localhost:5678/webhook/rainfall"
        
        # Prepare the payload according to the example format
        payload = [
            {
                "body": {
                    "latitude": coordinates['latitude'],
                    "longitude": coordinates['longitude']
                }
            }
        ]
        
        # Headers
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Debug: Show what we're sending
        st.info("🔍 **Debug - Sending to API:**")
        st.code(f"URL: {api_url}")
        st.code(f"Payload: {json.dumps(payload, indent=2)}")
        st.code(f"Headers: {json.dumps(headers, indent=2)}")
        
        # Make the POST request
        response = requests.post(
            api_url, 
            json=payload, 
            headers=headers,
            timeout=30
        )
        
        # Debug: Show response details
        st.info("📡 **Debug - API Response:**")
        st.code(f"Status Code: {response.status_code}")
        st.code(f"Response Headers: {dict(response.headers)}")
        response_preview = response.text[:500] + "..." if len(response.text) > 500 else response.text
        st.code(f"Response Text: {response_preview}")
        
        # Check if request was successful
        if response.status_code == 200:
            try:
                # Parse the JSON response
                response_data = response.json()
                
                # Extract the output according to the example format
                if isinstance(response_data, list) and len(response_data) > 0:
                    if 'output' in response_data[0]:
                        return response_data[0]['output']
                    else:
                        return response_data[0]
                else:
                    return response_data
                    
            except json.JSONDecodeError:
                # If response is not JSON, return as text
                return response.text
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("🔌 Connection Error: Could not connect to the weather API. Make sure the server is running on localhost:5678")
        return None
    except requests.exceptions.Timeout:
        st.error("⏱️ Timeout Error: The API request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"🚫 Request Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
        return None

def test_webhook_connection():
    """
    Test if the webhook endpoint is reachable
    """
    try:
        api_url = "http://localhost:5678/webhook/rainfall"
        
        # Simple test payload
        test_payload = [
            {
                "body": {
                    "latitude": 19.0760,
                    "longitude": 72.8777
                }
            }
        ]
        
        headers = {'Content-Type': 'application/json'}
        
        st.info("🔍 Testing webhook connection...")
        
        # Test connection with short timeout
        response = requests.post(
            api_url, 
            json=test_payload, 
            headers=headers,
            timeout=5
        )
        
        if response.status_code == 200:
            st.success(f"✅ Webhook is reachable! Status: {response.status_code}")
            st.code(f"Response preview: {response.text[:200]}...")
        else:
            st.warning(f"⚠️ Webhook responded with status: {response.status_code}")
            st.code(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("🔌 Connection Error: Cannot reach webhook at localhost:5678")
        st.info("💡 Make sure your n8n workflow is running on port 5678")
    except requests.exceptions.Timeout:
        st.error("⏱️ Timeout: Webhook is taking too long to respond")
    except Exception as e:
        st.error(f"❌ Test failed: {str(e)}")

# Sidebar information
def sidebar_info():
    st.sidebar.title("ℹ️ About")
    st.sidebar.info("""
    **Weather Prediction Chatbot**
    
    This application allows you to:
    - 🗺️ View an interactive OpenStreetMap
    - 📍 Click to select any location
    - 🌦️ Get detailed weather information
    - 📊 View 5-day weather forecasts
    - 💡 Receive weather-based recommendations
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔧 API Information")
    st.sidebar.code("POST http://localhost:5678/webhook/rainfall")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📝 Instructions")
    st.sidebar.write("""
    1. Click anywhere on the map
    2. Verify the coordinates
    3. Test webhook connection
    4. Click 'Confirm Location'
    5. View the weather report
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🐛 Debugging")
    st.sidebar.write("""
    • Use 'Test Webhook Connection' to verify API availability
    • Enable 'Show Debug Info' to see request/response details
    • Check that n8n is running on port 5678
    """)

if __name__ == "__main__":
    sidebar_info()
    main()
