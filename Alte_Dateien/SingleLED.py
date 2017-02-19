import RPi.GPIO as gp
import time


gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(17, gp.IN)

zeitAktuell = time.time()
zeitEnde = zeitAktuell + 5

while zeitAktuell < zeitEnde:
    if gp.input(17) == True
        print(time.time())
    zeitAktuell = time.time()

