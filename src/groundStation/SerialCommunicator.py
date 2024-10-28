# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# TODO:
# check out this link: https://www.youtube.com/watch?v=AnZ0uTOerUI

# in the beginning, he says that error handling is often an indicator of bad design
# quote says to "only use exceptions when you cannot know if an operation can succeed or fail"
# for us, we can't guarantee we'll receive rocket data perfectly reliably -- so we have ample
# reason to use an exception or try/catch block to handle having an empty queue...for version
# 1 of the app.

# HOWEVER:
# quote says that "Asking for data can fail. giving data when you have it cannot" at 16:35

# we're currently facing issues trying to read from an empty queue -- the display always checks for data
# even if the serial communicator doesn't ever receive it... this is an error where we're asking for
# data we don't have!

# shouldn't we refactor so that the serial communicator receiving data prompts a display update?
# right now, it updates as it reads from a queue. What if we send a signal to update the display
# containing our data--this should have the same effect. we still constantly update no matter
# when its received, still solving our original system clock problem, but in this way, we
# only give data when we have it -- instead of asking for data when we don't. Interesting stuff :)


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
