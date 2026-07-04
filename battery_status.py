"""
battery_status.py
Checks a drone's battery voltage against safety thresholds
and reports flight status: CRITICAL, WARNING, or OK.
"""

def check_battery_status(voltage):
    """Return a status message based on battery voltage."""
    if voltage <= 9.5:
        return "CRITICAL: Land immediately."
    elif voltage <= 10.5:
        return "WARNING: Return to base soon."
    else:
        return "Battery OK. Continue mission."


# Test the function with a few sample readings
test_readings = [11.8, 10.2, 9.0, 10.5, 9.5]

for voltage in test_readings:
    status = check_battery_status(voltage)
    print(f"Voltage: {voltage}V -> {status}")