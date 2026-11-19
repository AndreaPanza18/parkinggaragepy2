from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import MagicMock

import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from src.parking_garage import ParkingGarage
from src.parking_garage import ParkingGarageError

class TestParkingGarage(TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_input: MagicMock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass
