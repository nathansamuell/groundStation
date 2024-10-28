# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
import serial

print("reaching serial initialization")
ser = serial.Serial(
    "/dev/serial/by-id/usb-FTDI_FT231X_USB_UART_D30DN1TR-if00-port0", 9600
)
print("serial init complete")

print("starting read loop")
for i in range(20):
    print(i)
    message = str(i)
    # ser.write(message.encode('utf-8'))
    codedBits = ser.readline()
    message = codedBits.decode()
    if message == "":
        print("Empty message")
    else:
        outputMsg = "Message received: {}".format(message)
        print(outputMsg)
