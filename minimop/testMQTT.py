import runSound
import time


print("startup main")
s = runSound.Sound("test.mosquitto.org", 1883)
print("running main")


while True:
    time.sleep(1)
