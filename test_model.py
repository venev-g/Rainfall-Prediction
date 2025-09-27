#!/usr/bin/env python3
"""
Test script to verify the XGBoost model functionality
"""

import pickle
import pandas as pd
import numpy as np

def test_model():
    """Test the XGBoost model with sample data"""
    
    print("🔍 Testing XGBoost Model")
    print("=" * 50)
    
    try:
        # Load the model
        with open('XGB_classifier.pkl', 'rb') as f:
            model = pickle.load(f)
        
        print("✅ Model loaded successfully")
        
        # Check model attributes
        if hasattr(model, 'feature_names_in_'):
            print(f"📊 Model features: {model.feature_names_in_}")
        
        # Create test data
        test_data = pd.DataFrame({
            'Humidity3pm': [70.0],
            'WindGustSpeed': [25.0],
            'Pressure3pm': [1013.0],
            'Humidity9am': [65.0],
            'WindDir3pm': [8]
        })
        
        print(f"📋 Test data:\n{test_data}")
        
        # Make prediction
        prediction = int(model.predict(test_data)[0])
        probability = model.predict_proba(test_data)[0]
        
        print(f"🎯 Prediction: {prediction} ({'Rain' if prediction == 1 else 'No Rain'})")
        print(f"📊 Probabilities: [No Rain: {float(probability[0]):.3f}, Rain: {float(probability[1]):.3f}]")
        print(f"🌧️ Rain Probability: {float(probability[1]):.1%}")
        
        # Test with different values
        print("\n" + "=" * 50)
        print("🧪 Testing with various scenarios:")
        
        scenarios = [
            {"name": "High Humidity", "data": [85, 30, 1010, 80, 5]},
            {"name": "Low Humidity", "data": [40, 15, 1020, 35, 10]},
            {"name": "High Wind", "data": [60, 60, 1005, 70, 12]},
            {"name": "Low Pressure", "data": [75, 40, 995, 65, 8]}
        ]
        
        for scenario in scenarios:
            test_scenario = pd.DataFrame({
                'Humidity3pm': [scenario['data'][0]],
                'WindGustSpeed': [scenario['data'][1]],
                'Pressure3pm': [scenario['data'][2]], 
                'Humidity9am': [scenario['data'][3]],
                'WindDir3pm': [scenario['data'][4]]
            })
            
            pred = int(model.predict(test_scenario)[0])
            prob = float(model.predict_proba(test_scenario)[0][1])
            
            result = "🌧️ Rain" if pred == 1 else "☀️ No Rain"
            print(f"{scenario['name']:15} -> {result:10} (Confidence: {prob:.1%})")
            
    except FileNotFoundError:
        print("❌ Model file 'XGB_classifier.pkl' not found")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_model()