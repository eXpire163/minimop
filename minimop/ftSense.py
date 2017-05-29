try:
    import RPi as GPIO
except ImportError:
    from minimop.mocks.mypi import GPIO

import atexit
import time


class FTSense:

    TRIG = 23
    ECHO = 24

    def __init__(self):
        atexit.register(self.on_close)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.output(self.TRIG, False)
        self.printme("Waiting For Sensor To Settle")
        time.sleep(2)

    def printme(self, txt):
        ## type: ( ) -> txt
        print("ftSense: {}".format(txt))

    def get_distance(self):
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        self.printme("Distance: {} cm".format(distance))
        return distance

    def on_close(self):
        GPIO.cleanup()
