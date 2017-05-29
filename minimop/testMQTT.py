import sound
import time


print("startup main")
s = sound.Sound("test.mosquitto.org", 1883)
print("running main")


while True:
    time.sleep(1)
