# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
import threading

import serial  # noqa: F401


class SerialCommunicator:
    def __init__(self, sp, br):
        serialPort = sp  # noqa: F841
        baudRate = br  # noqa: F841
        self.ser = serial.Serial(serialPort, baudRate)

        self.stopEvent = threading.Event()

    def read(self):
        codedBits = self.ser.readline()  # noqa: E1101
        bits = codedBits.decode()
        return bits

    def transmit(self, message):
        self.ser.write(message.encode("utf-8"))  # noqa: E1101

    def write(self, message):
        return message

    def start(self, queue):
        while not self.stopEvent.is_set():
            message = self.ser.readline().decode("utf-8").rstrip()
            # message = "Testing message read "  # Swap with the previous line to use the serial monitor
            if not message == "":
                queue.put(message)

    def stop(self):
        self.stopEvent.set()
