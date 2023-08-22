def calculate_rpm(time_between_signals):
    return 60 / time_between_signals


num_signals = int(input("How many signals will you enter? "))
prev_signal_time = float(input("Enter the time of the first signal (seconds): "))

for i in range(num_signals - 1):
    current_signal_time = float(input(f"Enter the time of {i + 2}. signal (seconds): "))
    time_between_signals = current_signal_time - prev_signal_time

    if time_between_signals > 0:
        rpm = calculate_rpm(time_between_signals)
        print("Rotation Speed (RPM):", rpm)

    prev_signal_time = current_signal_time

print("Simulation completed.")
