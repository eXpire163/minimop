import os
from tempfile import TemporaryFile
from gtts import gTTS
import paho.mqtt.client as mqtt
import pygame
from conf import Mop


class Sound(object):


    def printme(self, txt, debug=False):
        Mop.printme(self.__class__.__name__, txt, debug)
# The callback for when the client receives a CONNACK response from the server.


    def on_connect(self, client, userdata, flags, rc):
        self.printme("Connected with result code " + str(rc))
        client.subscribe("minimop/sound")

    # The callback for when a PUBLISH message is received from the server.


    def on_message(self, client, userdata, msg):
        self.printme(msg.topic + " " + str(msg.payload))
        if(msg.topic == "tts"):
            tts = gTTS(text=msg.payload, lang='en')
            f = TemporaryFile()
            tts.write_to_fp(f)
            self.printme("Created tempfile")
            pygame.mixer.music.load(f.name)
            self.printme("play sound")
            pygame.mixer.music.play()
            self.printme("close temp")
            f.close()
        elif (msg.topic == "wav"):
            if(os.path.isfile("../fx/" + msg.payload)):
                pygame.mixer.music.load("fx/" + msg.payload)
                pygame.mixer.music.play()
        else:
            if(os.path.isfile("../fx/SciFiRobotSound.wav")):
                pygame.mixer.music.load("../fx/SciFiRobotSound.wav")
                pygame.mixer.music.play()

    def __init__(self, server="localhost", port=1883):
        pygame.mixer.init()

        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        self.printme("connting to {}:{} ".format(server,port))
        client.connect(server, port, 60)
        self.printme("connected")

        #client.loop_forever()
