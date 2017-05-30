import numpy as np


class Mathf(object):
    """Math heper """

    @staticmethod
    def lerp(xvalue, yvalue, delta):
        x_axis = [0, 1]
        y_axis = [xvalue, yvalue]
        result = np.interp(delta, x_axis, y_axis)
        return round(result, 3)

    @staticmethod
    def smoothstep(edge0, edge1, x):    
        # Scale, bias and saturate x to 0..1 range
        x = Mathf.scale(x, edge0, edge1)
        # Evaluate polynomial
        return round(x*x*(3 - 2*x), 3)

    @staticmethod
    def scale(x, lowIn, highIn, lowOut=0.0, highOut=1.0):
        return Mathf.clamp((x - lowIn) / (highIn - lowIn), lowOut, highOut)

    @staticmethod
    def clamp(x, lowerlimit, upperlimit):        
        if (x < lowerlimit):
            x = lowerlimit
        if (x > upperlimit):
            x = upperlimit
        return x

