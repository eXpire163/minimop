from minimop.hardware.ftRadar import FTRadar

radar = FTRadar()

while True:
    radar.update()

