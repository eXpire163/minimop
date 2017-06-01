import ftSense

from minimop.hardware import ftShield

mid_range = 15
low_range = 8


shield = ftShield.FTShield()
sense = ftSense.FTSense()

critfail = False
while not critfail:
    dist_front = sense.get_distance()
    if(dist_front > mid_range):
        shield.move(1)

    elif(dist_front > low_range):
        shield.move(0.3)
    else:
        shield.stop()
        shield.turn_left(1)

        dist_left = sense.get_distance()
        if(dist_left < dist_front):
            shield.turn_right(2)
            dist_right = sense.get_distance()
            if(dist_right < low_range):
                shield.backward(0.5)




