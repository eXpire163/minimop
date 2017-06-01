from ftSense import FTSense
import array


class FTRadar(object):
    radar_values = [0.0] * 181
    step = 0
    stepsize = 5

    sense = FTSense(True)

    def update(self):
        self.step = (self.step + self.stepsize) % 180
        self.sense.set_direction(self.step)
        distance = self.sense.get_distance()
        self.radar_values[self.step] = distance

    def __init__(self):
        for x in range(0, 180, 1):
            self.radar_values[x] = 0



