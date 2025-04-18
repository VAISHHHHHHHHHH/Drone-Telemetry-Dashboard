import tkinter as tk
from tkinter import ttk
import random
import time
import threading


class DroneTelemetrySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Telemetry Simulator")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Create a style for progress bars
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

        # Battery Voltage
        self.battery_label = tk.Label(root, text="Battery Voltage (V):", font=("Helvetica", 14))
        self.battery_label.pack(anchor="w", padx=20, pady=5)
        self.battery_value = tk.Label(root, text="0.0", font=("Helvetica", 16), fg="blue")
        self.battery_value.pack(anchor="w", padx=40)

        # IMU Sensor Data
        self.imu_label = tk.Label(root, text="IMU Sensor Data (Roll, Pitch, Yaw):", font=("Helvetica", 14))
        self.imu_label.pack(anchor="w", padx=20, pady=5)
        self.imu_value = tk.Label(root, text="0.0, 0.0, 0.0", font=("Helvetica", 16), fg="blue")
        self.imu_value.pack(anchor="w", padx=40)

        # Temperature Sensor Data
        self.temp_label = tk.Label(root, text="Temperature (°C):", font=("Helvetica", 14))
        self.temp_label.pack(anchor="w", padx=20, pady=5)
        self.temp_value = tk.Label(root, text="0.0", font=("Helvetica", 16), fg="blue")
        self.temp_value.pack(anchor="w", padx=40)

        # Altitude Sensor Data
        self.altitude_label = tk.Label(root, text="Altitude (m):", font=("Helvetica", 14))
        self.altitude_label.pack(anchor="w", padx=20, pady=5)
        self.altitude_value = tk.Label(root, text="0.0", font=("Helvetica", 16), fg="blue")
        self.altitude_value.pack(anchor="w", padx=40)

        # GPS Position
        self.gps_label = tk.Label(root, text="GPS Data (Latitude, Longitude, Altitude):", font=("Helvetica", 14))
        self.gps_label.pack(anchor="w", padx=20, pady=5)
        self.gps_value = tk.Label(root, text="0.0000, 0.0000, 0.0", font=("Helvetica", 16), fg="blue")
        self.gps_value.pack(anchor="w", padx=40)

        # Connection Health
        self.connection_label = tk.Label(root, text="Connection Health:", font=("Helvetica", 14))
        self.connection_label.pack(anchor="w", padx=20, pady=5)
        self.connection_value = tk.Label(root, text="Excellent", font=("Helvetica", 16), fg="green")
        self.connection_value.pack(anchor="w", padx=40)

        # Start updating telemetry data
        self.is_running = True
        threading.Thread(target=self.update_telemetry, daemon=True).start()

    def update_telemetry(self):
        while self.is_running:
            # Simulate battery voltage (0-12V LiPo battery)
            battery_voltage = round(random.uniform(0, 12), 2)

            # Simulate IMU sensor data: roll, pitch, yaw
            roll = round(random.uniform(-180, 180), 2)
            pitch = round(random.uniform(-90, 90), 2)
            yaw = round(random.uniform(0, 360), 2)

            # Simulate temperature sensor data
            temperature = round(random.uniform(-20, 50), 2)

            # Simulate altitude sensor data
            altitude = round(random.uniform(0, 2000), 2)

            # Simulate GPS data
            latitude = round(random.uniform(-90.0, 90.0), 4)
            longitude = round(random.uniform(-180.0, 180.0), 4)
            gps_altitude = round(random.uniform(0, 5000), 2)

            # Simulate connection health
            connection_states = ["Excellent", "Good", "Poor", "No Signal"]
            connection_health = random.choice(connection_states)
            connection_color = "green" if connection_health == "Excellent" else \
                               "orange" if connection_health == "Good" else \
                               "red"

            # Update the GUI with telemetry data
            self.battery_value.config(text=f"{battery_voltage} V")
            self.imu_value.config(text=f"{roll}, {pitch}, {yaw} (°)")
            self.temp_value.config(text=f"{temperature} °C")
            self.altitude_value.config(text=f"{altitude} m")
            self.gps_value.config(text=f"{latitude}, {longitude}, {gps_altitude} m")
            self.connection_value.config(text=connection_health, fg=connection_color)

            time.sleep(1)  # Simulate real-time updates every second

    def on_close(self):
        self.is_running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = DroneTelemetrySimulator(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
