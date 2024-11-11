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
import time
import threading
import serial  # noqa: F401

from PyQt5.QtCore import QObject, pyqtSignal


class SerialCommunicator(QObject):
    dataSignal = pyqtSignal(list)

    def __init__(self, sp, br):
        super().__init__()  # needed to inherit from any Q class
        serialPort = sp  # noqa: F841
        baudRate = br  # noqa: F841
        try:
            self.ser = serial.Serial(serialPort, baudRate, timeout=1)

        except serial.serialutil.SerialException:
            rocketPacket = "FLIGHTCTL: ERROR: Serial Port Not Open!"
            self.dataSignal.emit(rocketPacket)
        self.readThread = threading.Thread(target=self.read)
        self.stopEvent = threading.Event()

    def read(self):
        # while the thread is running,
        while not self.stopEvent.is_set():

            # attempt to collect five data collections (keeps our number of pyqt5 signals down)
            for i in range(5):
                rocketData = []   # holds our list of five correctly picked data
                try:
                    rocketPacket = self.ser.readline().decode("utf-8").rstrip()  # read from rocket
                    if rocketPacket == b'':  # empty string byte means no data was received before timeout
                        rocketPacket = "no data"  # FIXME: we need a standardized signal for this

                    rocketData.append(rocketPacket)  # add to list to send to app!

                except serial.serialutil.PortNotOpenError:
                    rocketPacket = "FLIGHTCTL: ERROR: Serial Port Not Open!"
                    self.stopEvent.set()
                    self.dataSignal.emit([rocketPacket])

                except AttributeError as e:
                    rocketPacket = "FLIGHTCTL: ERROR: " + str(e)
                    self.stopEvent.set()
                    self.dataSignal.emit([rocketError])

            self.dataSignal.emit(rocketData)  # if no errors occur then send the list!

        if self.stopEvent.is_set():
            self.dataSignal.emit(rocketData)
            self.dataSignal.emit(["FLIGHTCTL: Restart app to try again"])


    def transmit(self, message):
        self.ser.write(message.encode("utf-8"))  # noqa: E1101

    def write(self, message):
        return message

    def start(self):
        self.stopEvent.clear()
        self.readThread.start()

    def stop(self):
        self.stopEvent.set()
