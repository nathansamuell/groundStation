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
from pathlib import Path  # noqa: E402

import pytest
from flightctl.FileWriter import FileWriter  # noqa: E402


@pytest.fixture
def file_writer():
    writer = FileWriter()
    yield writer


def test___init__(file_writer):
    file_path = Path("dataOut.tmp")
    assert file_path.is_file() is True
    assert file_writer.tempFile == "dataOut.tmp"
    with open(file_writer.tempFile, "r") as file:
        file_contents = file.read()
        assert file_contents == "File Initialized\n"


def test_addToFile(file_writer):
    file_writer.addToFile("Test Text")
    with open(file_writer.tempFile, "r") as file:
        assert file.read() == "File Initialized\nTest Text"


def test_writeEOF(file_writer):
    file_writer.addToFile("Test Text")
    file_writer.writeEOF("TestOutput")
    file_path = Path("TestOutput.csv")
    assert file_path.is_file() is True

    with open("TestOutput.csv", "r") as file:
        assert file.read() == "File Initialized\nTest Text"

    os.remove("TestOutput.csv")
