import unittest
from unittest.mock import patch
import sys
import os
sys.path.append('../app')
from numpad import Numpad
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtTest import QSignalSpy


class TestNumpad(unittest.TestCase):

    def test_buttonClicked(self):
        testApp = QApplication([])
        testButton = QPushButton("a")
        numpad = Numpad()
        for i in range(1,10):
            testButton = QPushButton(str(i))
            numpad.buttonClicked(testButton)
            self.assertEqual(str(numpad.loginPin), str(i))
            numpad.loginPin = ''


    @patch('os.getenv')
    def test_authenticate_login_success(self,mock_env):
        testApp = QApplication([])
        numpad = Numpad()
        signalSpy = QSignalSpy(numpad.loginSuccess)
        
        mock_env.return_value = '1234'
        numpad.loginPin = '1234'

        self.assertEqual('1234', numpad.loginPin) #check to make sure values match inherently, will check signal after
        numpad.authenticate() # must go after previous assertion
        self.assertEqual(len(signalSpy),1) # checks to see if signal is sent

        self.assertEqual

    @patch('os.getenv')
    def test_authenticate_login_failure(self,mock_env):
        testApp = QApplication([])
        numpad = Numpad()
        signalSpy = QSignalSpy(numpad.loginFailure)

        mock_env.return_value = '1234'
        numpad.loginPin = '4321'

        # check to make sure loginPin holds a mismatched value
        self.assertNotEqual('1234',numpad.loginPin)

        # MUST authenticate AFTER previous assertion, otherwise test will succedd WRONGLY
        numpad.authenticate()
        self.assertEqual(len(signalSpy),1) # ensures that only one signal is sent (only one is sent if authentication fails)
        

if __name__ == '__main__':
    unittest.main()