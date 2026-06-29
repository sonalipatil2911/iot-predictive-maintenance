import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(2026)

# Configuration
rows = 200
start_time = datetime(2026, 6, 1, 0, 0, 0)
machines = [f'MC-0{i}' for i in range(1, 6)] # 5 specific machines on the floor
machine_types = {
    'MC-01': 'CNC Router',
    'MC-02': 'Injection Molder',
    'MC-03': 'CNC Router',
    'MC-04': 'Hydraulic Press',
    'MC-05': 'Robotic Welder'
}

data = []

for i in range(rows):
    # Log every 2 hours
    timestamp = (start_time + timedelta(hours=i * 2)).strftime('%Y-%m-%d %H:%M:%S')
    machine_id = np.random.choice(machines)
    m_type = machine_types[machine_id]
    
    # Baselines
    vibration = round(float(np.random.uniform(1.5, 4.0)), 2)
    temperature = round(float(np.random.uniform(45.0, 65.0)), 1)
    operating_hours = int(200 + (i * 0.5)) # Gradual wear
    parts_produced = int(np.random.randint(150, 250))
    defective_parts = int(parts_produced * np.random.uniform(0.005, 0.02)) # Normal 1-2% defect rate
    
    # --- Injecting Mechanical Anomalies ---
    
    # Anomaly 1: MC-02 Imminent Bearing Failure (Spiking vibration & friction heat)
    if machine_id == 'MC-02' and i > 120:
        vibration = round(float(vibration * np.random.uniform(2.5, 3.8)), 2)
        temperature = round(float(temperature * np.random.uniform(1.4, 1.7)), 1) # Pushes temp past 85°C
        
    # Anomaly 2: MC-04 Quality Drift (High defects, normal temperature/vibration)
    if machine_id == 'MC-04' and i > 80 and i < 140:
        defective_parts = int(parts_produced * np.random.uniform(0.12, 0.20)) # Spikes to 15-20% defect rate
        
    # Anomaly 3: MC-01 Overworked Asset Capacity Drop
    if machine_id == 'MC-01' and i > 150:
        parts_produced = int(parts_produced * 0.6) # Production capacity plummets due to strain
        defective_parts = int(parts_produced * np.random.uniform(0.05, 0.08))
        
    data.append([timestamp, machine_id, m_type, vibration, temperature, operating_hours, parts_produced, defective_parts])

# Create DataFrame
columns = ['Timestamp', 'Machine ID', 'Machine Type', 'Vibration (mm/s)', 'Internal Temp (°C)', 'Operating Hours', 'Total Parts Produced', 'Defective Parts Count']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('factory_sensor_logs.csv', index=False)
print("Successfully generated 'factory_sensor_logs.csv' with 200 operational rows!")