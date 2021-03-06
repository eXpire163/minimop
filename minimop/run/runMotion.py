import paho.mqtt.client as mqtt

from minimop.hardware.ftShield import FTShield


def printme(text):
    print("MOTION: "+text)
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    printme("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("minimop/motion")
    printme("subscribing to minimop/motion")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    printme(msg.topic+" "+str(msg.payload))
    befehl = msg.payload.decode('utf8').split(',')
    if 3 == len(befehl):
        ftShield.setMotor(befehl[0], befehl[2], befehl[1])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect device

printme("Connecting to Shield")
maxSpeed = 204
debug = True
ftShield = FTShield()
ftShield.debug = debug
printme('debugmode is {}'.format(debug))
ftShield.maxSpeed = maxSpeed


client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
