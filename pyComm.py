# Author: Artip Nakchinda
# This code is used to communicate with an Arduino 
# and plot Differential Pressure sensor data in real-time.
# Disclaimer: GitHub Copilot was used for assistance in development of this code.
# Libraries used:
# - matplotlib
# - pyserial

# Python Code for serial communication with Arduino
import matplotlib.pyplot as plt
import serial

# Get the serial port
COM = input("Enter COM port (format 'COM#'): ")
arduino = serial.Serial(COM, timeout=1)
arduino.baudrate = 115200

# arduino = serial.Serial('COM8', timeout=1)
# arduino.baudrate = 115200

rawdata = []
count = 0

# Create empty lists to store x and y values
x_values = []
y_values = []

while True:
    try:
        data = arduino.readline().decode().strip()
        if data:
            print("Received data:", data)
            # Parse the received data and append to the lists
            x, y = map(float, data.split(','))  # Assuming the data is in the format "x,y"
            x_values.append(x)
            y_values.append(y)
            
            # Plot the data
            plt.plot(x_values, y_values)
            plt.xlabel('Time')
            plt.ylabel('Differential Pressure')
            plt.title('Live Differential Pressure vs Time')
            plt.grid(True)
            plt.pause(0.01)  # Pause to allow the plot to update
            
    except KeyboardInterrupt:
        break

# Show the plot
plt.show()

arduino.close()