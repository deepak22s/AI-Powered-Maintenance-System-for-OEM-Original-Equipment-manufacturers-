#This script is used to generate the data but we didnt used this in the project

import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration for the dataset
num_vehicles = 50  # Simulating 50 different vehicles
num_hours = 24  # For a 24-hour period
interval_minutes = 5  # Data recorded every 5 minutes

# Time range for data collection
start_time = datetime.now() - timedelta(hours=num_hours)
timestamps = [start_time + timedelta(minutes=i * interval_minutes) for i in range((num_hours * 60) // interval_minutes)]

# Function to simulate sensor data for each metric
def generate_sensor_data():
    return {
        "engine_temperature": round(random.uniform(70, 110), 2),  # in °C
        "tire_pressure": round(random.uniform(30, 35), 2),        # in PSI
        "brake_wear": round(random.uniform(0, 100), 2),           # as a percentage
        "battery_voltage": round(random.uniform(12, 14.5), 2)     # in volts
    }

# Generate data
data_records = []
for vehicle_id in range(1, num_vehicles + 1):
    for timestamp in timestamps:
        sensor_data = generate_sensor_data()
        data_record = {
            "vehicle_id": vehicle_id,
            "timestamp": timestamp,
            **sensor_data
        }
        data_records.append(data_record)

# Create a DataFrame and save to CSV and JSON
large_data_df = pd.DataFrame(data_records)
csv_file_path = '/mnt/data/large_simulated_vehicle_data.csv'
json_file_path = '/mnt/data/large_simulated_vehicle_data.json'

# Save to CSV and JSON
large_data_df.to_csv(csv_file_path, index=False)
large_data_df.to_json(json_file_path, orient='records', lines=True)

csv_file_path, json_file_path
