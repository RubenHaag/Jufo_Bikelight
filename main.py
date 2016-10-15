from time import time
from math import sin
from math import cos
from math import pi
from PIL import Image*

im = open("Bild.png")
pix = im.load()

lLed = 72 #anzahl der Leds auf dem LED-Streifen

matrix = [[0 for x in range(0, lLed)]for y in range(1,7)]
#erschaffen einer Liste, in der sieben Listen enthalten sind
t = 0 # Zeitabschnitt  
T = 0 # Umlaufzeit

k = 0 # später k = 2*pi*t/T

z = 0 # für die while-Dauerschleife

magnetschalter = False # kann später noch in komplexere funktion umgesetzt werden

for i in range(0, lLed): #setzten der Radien sollte später aus einer Textdatei ausgelesen werden
    matrix[0][i] = i+1

def berrechnungDerPixel(T, t):
    for i in range(0, lLed):

    	k = 2*pi*t/T #ausrechnen des Winkels in rad
        matrix[1][i] = (round(math.cos(k) * matrix[0][i], 1)*32) #berechnung der X-Koordinate
        matrix[2][i] = (round(math.sin(k) * matrix[0][i], 1)*32) #Berrechnung der Y Koordinate

        r, g, b, z = pix[matrix[1][i], matrix[2][i]] #auslesen eines Pixels
        matrix[3][i] = r
        matrix[4][i] = g
        matrix[5][i] = b



def main():
	while z==0:
		t1 = time() #startzeit t1
		

		while !magnetschalter:
			t = time() - T				#Ausrechnen der größe des Zeitabschnitts
			berrechnungDerPixel(T, t)

		T = time() - t1 				#Ausrechnen von T nach T = t2 - t1