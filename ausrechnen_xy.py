import math
from PIL import Image
from time import time


im = Image.open("Bild.png")
pix = im.load()
matrix = [[0 for _ in range(0,10)]for y in range(1, 7)] #erschaffen einer Liste mit sieben Listen, die je 10 Stellen haben
t = 0
k =  1 #(1/(t/(2*math.pi)))#winkel



	
def berrechnungDerPixel():
    for i in range(0, 10):
        matrix[0][i] = i+1 #setzten der Radien

        matrix[1][i] = (round(math.cos(k) * matrix[0][i], 1)*32) #berechnung der X-Koordinate
        matrix[2][i] = (round(math.sin(k) * matrix[0][i], 1)*32) #Berrechnung der Y Koordinate

        r, g, b, z = pix[matrix[1][i], matrix[2][i]] #auslesen eines Pixels
        matrix[3][i] = r
        matrix[4][i] = g
        matrix[5][i] = b

berrechnungDerPixel()
print(matrix)