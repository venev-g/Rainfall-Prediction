#!/usr/bin/env python3
"""
Test script to verify webhook payload format
"""

import requests
import json

def test_webhook():
    """Test the webhook with sample data"""
    
    # API endpoint
    api_url = "http://localhost:5678/webhook/rainfall"
    
    # Test coordinates (Mumbai)
    test_coordinates = {
        'latitude': 19.0760,
        'longitude': 72.8777
    }
    
    # Prepare payload in the exact format as the app
    payload = [
        {
            "body": {
                "latitude": test_coordinates['latitude'],
                "longitude": test_coordinates['longitude']
            }
        }
    ]
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    print("🔍 Testing Webhook Connection")
    print("=" * 50)
    print(f"URL: {api_url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print(f"Headers: {json.dumps(headers, indent=2)}")
    print("=" * 50)
    
    try:
        # Send request
        response = requests.post(
            api_url, 
            json=payload, 
            headers=headers,
            timeout=10
        )
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"📡 Response Headers: {dict(response.headers)}")
        print(f"📄 Response Content Type: {response.headers.get('content-type', 'unknown')}")
        print("📋 Response Body:")
        print("-" * 30)
        
        # Try to parse as JSON first
        try:
            response_json = response.json()
            print(json.dumps(response_json, indent=2))
        except json.JSONDecodeError:
            print("Raw response (not JSON):")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Cannot connect to webhook")
        print("💡 Make sure n8n is running on localhost:5678")
    except requests.exceptions.Timeout:
        print("⏰ Timeout Error: Request timed out")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_webhook()