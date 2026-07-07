def check_battery_status(voltage):
    if voltage <= 9.5:
        return "CRITICAL: Land immediately."
    elif voltage <= 10.5:
        return "WARNING: Return to base soon."
    else:
        return "Battery OK. Continue mission."


flight_voltages = [11.8, 10.2, 9.0, 10.5, 12.1]
total = 0

for voltage in flight_voltages:
    status = check_battery_status(voltage)
    print(f"Voltage: {voltage}V -> {status}")
    total = total + voltage


average = total / len(flight_voltages)
print(f"\nAverage voltage across {len(flight_voltages)} flights: {average}")