import RPi.GPIO as gp
import time



gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(17, gp.IN)
a = time.time()
b = a + 5
if 1 == 1:
    while b >= a + 5:
        b = a + 0.001
        while True:
            x = time.time()
            if gp.input(17) == False:
                while gp.input(17) == False:
                    pass

                a = time.time() - x   
                print(a)
                