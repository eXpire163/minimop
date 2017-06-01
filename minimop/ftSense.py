try:
    import RPi.GPIO as GPIO
    print "using real gpio"
except ImportError:
    from minimop.mocks.mypi import GPIO
    print "using mock gpio"

from helper.mathf import Mathf
from conf import Mop
import atexit
import time


class FTSense:

    TRIG = 23
    ECHO = 24

    SERVO = 11  # 7
    SERVO_ACTIVE = False

    def printme(self, txt, debug=False):
        Mop.printme(self.__class__.__name__, txt, debug)

    def __init__(self, servo_active = False):
        self.SERVO_ACTIVE = servo_active

        GPIO.setmode(GPIO.BCM)
        atexit.register(self.on_close)

        #distance senosr
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.output(self.TRIG, False)
        self.printme("Waiting For Sensor To Settle")
        time.sleep(2)

        #distance servo
        if self.SERVO_ACTIVE:
            GPIO.setup(self.SERVO, GPIO.OUT)
            self.p = GPIO.PWM(self.SERVO, 50)
            self.p.start(7.5)
            self.set_direction(90)




    def printme(self, txt):
        ## type: ( ) -> txt
        print("ftSense: {}".format(txt))

    def get_distance(self, printinfo=False):
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
        if printinfo:
            self.printme("Distance: {} cm".format(distance))
        return distance

    def set_direction(self, direction):
        ''' in grad 0-180 '''
        # https://www.johannespetz.de/raspberry-pi-servomoteren/
        if self.SERVO_ACTIVE:
            lowIn = 0
            highIn = 180
            lowOut = 2.5
            highOut = 12.5
            targetdir = Mathf.scale(direction, lowIn, highIn, lowOut, highOut)
            self.p.ChangeDutyCycle(targetdir)


    def on_close(self):
        GPIO.cleanup()
