from Tkinter import *
from minimop.conf import Mop
import math
import paho.mqtt.client as mqtt
import json

master = Tk()

width = 1000
height = 500

radar_values = [181]

step = 0
stepsize = 5

w = Canvas(master ,width=width, height=height)
w.pack()


botmid_x = width/2
botmid_y = 500


def on_connect(self, client, userdata, flags, rc):
    self.printme("Connected with result code " + str(rc))
    client.subscribe(Mop.mqtt_radar)


def on_message(self, client, userdata, msg):
    self.printme(msg.topic + " " + str(msg.payload))
    info = json.load(msg.payload)
    draw_to(info[0], info[1], "green")


def draw_to(angle, dist, color):
    # lighten old
    # w.create_rectangle(0, 0, width, height, fill="white", stipple="gray50")
    # w.create_rectangle(0, 0, width, height, fill="white", stipple="gray25")
    length = dist
    angle += 180

    # find the end point
    endy = length * math.sin(math.radians(angle)) + botmid_y
    endx = length * math.cos(math.radians(angle)) + botmid_x
    w.create_line(botmid_x, botmid_y, endx, endy, fill=color)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(Mop.mqtt_server, Mop.mqtt_port, 60)


master.mainloop()
