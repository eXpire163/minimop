from ftSense import FTSense
from minimop.conf import Mop
import paho.mqtt.client as mqtt
import json


class FTRadar(object):
    radar_values = [0.0] * 181
    step = 0
    step_size = 5

    sense = FTSense(True)

    client = mqtt.Client()


    # client.loop_start()
    client.disconnect()

    def update(self):
        self.step = (self.step + self.step_size) % 180
        self.sense.set_direction(self.step)
        distance = self.sense.get_distance()
        self.radar_values[self.step] = distance

        msg = json.dumps([self.step, distance])
        self.client.publish(Mop.mqtt_radar, msg)

    def __init__(self):
        for x in range(0, 180, 1):
            self.radar_values[x] = 0
        self.client.connect(Mop.mqtt_server, Mop.mqtt_port, 60)



