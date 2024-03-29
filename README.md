# Differential Pressure Sensor
This program interfaces an Arduino with a Sensirion Differential Pressure Sensor to a Python program that outputs its data as a live graph (pressure v. time)

## Hardware Connection
From the [Sensirion I2C-SDP Repository](https://github.com/Sensirion/arduino-i2c-sdp?tab=readme-ov-file):
1. Connect the SDP Sensor to your Arduino board's standard I2C bus. Check the pinout of your Arduino board to find the correct pins. The pinout of the SDP Sensor board can be found in the data sheet.
    - VDD of the SEK-SDP to the 3V3 of your Arduino board (5V is also possible)
    - GND of the SEK-SDP to the GND of your Arduino board
    - SCL of the SEK-SDP to the SCL of your Arduino board
    - SDA of the SEK-SDP to the SDA of your Arduino board

![Sensirion](https://github.com/Sensirion/arduino-i2c-sdp/raw/master/images/sdp8xx-pinout.png)

## Materials 
- Arduino Board (For our case, we are using either an UNO or a Portenta H7)
- Sensirion Differential Pressure Sensor SDP8xx-Analog
- A PC that has Python installed

## Software
- There are two main programs in this repository:
    1. Arduino Program: Slightly modified Sensirion Code to acquire Differential Pressure from sensor
    2. Python Program: Acquires sensor data and outputs onto a dynamic graph (pressure vs. time)

## Installation/Usage
1. Connect the Arduino board to a PC
2. Verify and Upload Arduino code `main.ino` to the board.
3. Run `python pyComm.py` on the terminal
    a. The program will ask for a COM port, check which COM port the Arduino is connected, and then input as specified.
    b. When the Arduino starts sending data, the Python program picks up on the data and outputs a live graph.
4. When finished, close the Python program (`Ctrl-C`)

## Images
![Sensirion Pressure Sensor connected to Arduino UNO](images\20240328_184812.jpg)

![Sensirion Pressure Sensor connected to Arduino Portenta H7](images\20240225_234952.jpg)


## Live Sensor Graph Demo
This is a demo of the python program acquiring differential pressure data from the Arduino
<video width="480" height="480" controls>
    <source src="images/graphDemo.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

## References
- GitHub Copilot for suggesting code to get it working in the first place
- [Matplotlib: Visualization with Python](https://matplotlib.org/)
- [Instructables: Arduino Python Communication via USB](https://www.instructables.com/Arduino-Python-Communication-via-USB/)
- [Instructables: Sending Data From Arduino to Python Via USB](https://www.instructables.com/Sending-Data-From-Arduino-to-Python-Via-USB/)
- [pySerial](https://pythonhosted.org/pyserial/)
- [Sensirion: Arduino SDP](https://github.com/Sensirion/arduino-sdp)
- [Sensirion: Arduino Core](https://github.com/Sensirion/arduino-core)
- [Sensirion: Arduino I2C SDP](https://github.com/Sensirion/arduino-i2c-sdp?tab=readme-ov-file)
- [Sensirion: Differential Pressure Datasheet for SDP8xx Analog](https://sensirion.com/media/documents/68DF0025/6167E542/Sensirion_Differential_Pressure_Datasheet_SDP8xx_Analog.pdf)
- [Sensirion: SDP816-500Pa](https://sensirion.com/products/catalog/SDP816-500Pa/)
- [Arduino: Portenta H7](https://docs.arduino.cc/hardware/portenta-h7/#features)
