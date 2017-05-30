from Tkinter import *
import math

master = Tk()

width = 1000
height = 500


step = 0
stepsize = 5

w = Canvas(master ,width=width, height=height)
w.pack()


botmid_x = width/2
botmid_y = 500


def drawTo(angle, dist, color):

    w.create_rectangle(0, 0, width, height, fill="white", stipple="gray50")
    w.create_rectangle(0, 0, width, height, fill="white", stipple="gray25")

    length = dist

    angle += 180

    # find the end point
    endy = length * math.sin(math.radians(angle)) + botmid_y
    endx = length * math.cos(math.radians(angle)) + botmid_x
    w.create_line(botmid_x, botmid_y, endx, endy, fill=color)

# w.create_line(botmid_x, botmid_y, 300, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")


def update(step, stepsize):

    step = (step + stepsize)%180
    drawTo(step, 500, "green")
    master.after(250, update, step, stepsize)



master.after(250, update, step, stepsize)
master.mainloop()
