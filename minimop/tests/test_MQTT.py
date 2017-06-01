import time

import minimop.run.runSound

print("startup main")
s = minimop.run.runSound.Sound("test.mosquitto.org", 1883)
print("running main")


while True:
    time.sleep(1)
