# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
import os
import sys
import unittest

sys.path.append("../src")

from pathlib import Path  # noqa: E402

from groundStation.FileWriter import FileWriter  # noqa: E402


class TestFileWriter(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName=methodName)
        self.fileContents = ""

    def test___init__(self):
        TestFileWriter = FileWriter()
        filePath = Path("dataOut.tmp")
        self.assertEqual(filePath.is_file(), True)
        self.assertEqual(TestFileWriter.tempFile, "dataOut.tmp")
        with open(TestFileWriter.tempFile, "r") as file:
            self.fileContents = file.read()
            self.assertEqual(self.fileContents, "File Initialized\n")

    def test_addToFile(self):
        TestFileWriter = FileWriter()
        TestFileWriter.addToFile("Test Text")
        with open(TestFileWriter.tempFile, "r") as file:
            self.assertEqual(file.read(), "File Initialized\nTest Text")
            self.fileContents = file.read()

    def test_writeEOF(self):
        TestFileWriter = FileWriter()
        TestFileWriter.addToFile("Test Text")
        TestFileWriter.writeEOF("TestOutput")
        filePath = Path("TestOutput.csv")
        self.assertEqual(filePath.is_file(), True)

        with open("TestOutput.csv", "r") as file:
            self.assertEqual(file.read(), "File Initialized\nTest Text")

        os.remove("TestOutput.csv")


if __name__ == "__main__":
    unittest.main()
