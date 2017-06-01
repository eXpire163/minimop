import paho.mqtt.client as mqtt
import json


import logging
logging.basicConfig(filename='log/example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

def printme(text):
    print("VIDEO: "+text)

client = mqtt.Client()


client.connect("localhost", 1883, 60)

#client.loop_start()
faces = json.dumps( [1,2,3])
print(faces)
client.publish("minimop/faces", faces)
client.disconnect()