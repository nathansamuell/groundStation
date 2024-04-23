# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# you need to install pyserial to the environment
# imports
import serial

ser = serial.Serial("/dev/serial0", 9600)

message = "hey kurt"
ser.write(message.encode())

for i in range(1, 10):
    data = ser.readline()
    decodedData = data.decode()
    print(decodedData)

ser.close()
