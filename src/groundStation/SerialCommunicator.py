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
import threading


class SerialCommunicator:
    def __init__(self, sp, br):
        serialPort = sp
        baudRate = br
        # self.ser = serial.Serial(serialPort, baudRate)

        self.stopEvent = threading.Event()

    def read(self):
        codedBits = self.ser.readline()
        bits = codedBits.decode()
        return bits

    def transmit(self, message):
        self.ser.write(message.encode())

    def write(self, message):
        return message

    def start(self, queue):
        while not self.stopEvent.is_set():
            # message = self.read()
            message = "Testing message read "
            if not message == "":
                queue.put(message)

    def stop(self):
        self.stopEvent.set()
