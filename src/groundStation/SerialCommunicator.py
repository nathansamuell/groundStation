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


class SCommunicator:
    def __init__(self, sp, br):
        serialPort = sp
        baudRate = br
        self.ser = serial.Serial(serialPort, baudRate)

    def read(self):
        codedBits = self.ser.readline()
        bits = codedBits.decode()
        return bits

    def write(self, message):
        self.ser.write(message.encode())
