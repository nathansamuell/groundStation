# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
from unittest.mock import patch

import pytest
from flightctl.Numpad import Numpad  # noqa: E402
from PyQt5.QtCore import Qt  # noqa: E402
from PyQt5.QtTest import QSignalSpy, QTest  # noqa: E402
from PyQt5.QtWidgets import QApplication, QPushButton  # noqa: E402


@pytest.fixture(scope="module")
def app():
    app = QApplication([])  # Ensure QApplication is created once
    yield app
    app.quit()  # Clean up after tests


@pytest.fixture
def numpad(app):
    return Numpad()


def test_buttonClicked(numpad):
    for i in range(1, 10):
        test_button = QPushButton(str(i))
        QTest.mouseClick(test_button, Qt.LeftButton)  # Simulate a mouse click
        numpad.buttonClicked(test_button)  # Call the method to handle the click
        assert str(numpad.loginPin) == str(i)
        numpad.loginPin = ""


@patch("os.getenv")
def test_authenticate_login_success(mock_env, numpad):
    signal_spy = QSignalSpy(numpad.loginSuccess)

    mock_env.return_value = "1234"
    numpad.loginPin = "1234"

    assert numpad.loginPin == "1234"  # check to make sure values match inherently
    numpad.authenticate()  # must go after previous assertion
    assert len(signal_spy) == 1  # checks to see if signal is sent


@patch("os.getenv")
def test_authenticate_login_failure(mock_env, numpad):
    signal_spy = QSignalSpy(numpad.loginFailure)

    mock_env.return_value = "1234"
    numpad.loginPin = "4321"

    # check to make sure loginPin holds a mismatched value
    assert numpad.loginPin != "1234"

    # MUST authenticate AFTER previous assertion
    numpad.authenticate()
    assert len(signal_spy) == 1  # ensures that only one signal is sent


if __name__ == "__main__":
    pytest.main()
