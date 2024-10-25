# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# NOTE:
# This file is NOT a unit test like its friends in this folder. This file
# mocks serial input on a development machine to provide a way to test
# serial port logic without a rocket computer or hardware. However, it
# is still a test, so the tests folder seems the best place to put it.


# imports
import os
import time

import serial
from dotenv import load_dotenv

# load environment variables, set serial port to MOCK_SERIAL
load_dotenv("../src/groundStation/.env")
mockPort = os.getenv("MOCK_SPORT_TEST")
rocketSerial = serial.Serial(mockPort, 9600)
time.sleep(2)  # wait to make sure connection is established

# send test message over serial, press ctrl+c to cancel
try:
    while True:
        message = "Sample rocket data! \n"
        rocketSerial.write(message.encode())
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Rocket Data Simulator stopped. Exiting now...")
except Exception as e:
    print("Uh Oh...")
    print(str(e))
finally:
    rocketSerial.close()
