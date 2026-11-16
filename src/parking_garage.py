import time
from datetime import datetime

DEPLOYMENT = False # This variable is to understand whether you are deploying on the actual hardware

try:
    import RPi.GPIO as GPIO
    import SDL_DS3231
    DEPLOYMENT = True
except:
    import mock.GPIO as GPIO
    import mock.SDL_DS3231 as SDL_DS3231


class ParkingGarage:

    # Pin number declarations
    INFRARED_PIN1 = 11
    INFRARED_PIN2 = 12
    INFRARED_PIN3 = 13
    SERVO_PIN = 16
    LED_PIN = 18

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.INFRARED_PIN1, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN2, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN3, GPIO.IN)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        GPIO.setup(self.LED_PIN, GPIO.OUT, initial=GPIO.LOW)
        self.rtc = SDL_DS3231.SDL_DS3231(1, 0x68)
        self.servo = GPIO.PWM(self.SERVO_PIN, 50)
        self.servo.start(5)  # Starts generating PWM on the pin with a duty cycle equal to 5% (corresponding to 0 degree)
        if DEPLOYMENT: # Sleep only if you are deploying on the actual hardware
            time.sleep(1)  # Waits 1 second so that the servo motor has time to make the turn
        self.door_open = False
        self.red_light_on = False

    def check_occupancy(self, pin: int) -> bool:
        # See User Story #1
        pass

    def get_number_occupied_spots(self) -> int:
        # See User Story #2
        pass

    def calculate_parking_fee(self, entry_time: datetime) -> float:
        # See User Story #3
        pass

    def open_garage_door(self) -> None:
        # See User Story #4
        pass

    def close_garage_door(self) -> None:
        # See User Story #4
        pass

    def turn_on_red_light(self) -> None:
        # See User Story #5
        pass

    def turn_off_red_light(self) -> None:
        # See User Story #5
        pass

    def manage_red_light(self) -> None:
        # See User Story #6
        pass

    # This method is meant to show you how to release the hardware resources when the program running on real hardware ends.
    def cleanup(self) -> None:
        self.servo.stop() # Stops generating PWM on the pin
        GPIO.cleanup() # Resets every GPIO pin


class ParkingGarageError(Exception):
    pass
