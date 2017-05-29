import random

class GPIO(object):

    BCM = "bcmmode"

    OUT = 0
    IN = 1


    @staticmethod
    def setmode(txt):
        print(txt)

    @staticmethod
    def setup(a, b):
        print(a, b)

    @staticmethod
    def output(txt, bool):
        print(txt, bool)

    @staticmethod
    def input(port):
        return random.randrange(0, 2)

    @staticmethod
    def cleanup():
        print "cleanup"
