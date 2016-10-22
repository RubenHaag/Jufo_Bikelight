from time import time
from math import sin
from math import cos
from math import pi
from PIL.Image import *
from neopixel import *

im = open("/home/pi/Desktop/JugendForscht/Bild.png")
pix = im.load()

LED_COUNT = 144 # Anzahl der LED's auf dem LED-Streifen
LED_PIN   = 18 # GPIO-Nummer des Pin's, mit dem man den LED-Streifen ansteuert.
LED_FREQ_HZ = 800000 # Blinkfrequenz
LED_DMA   = 5  # DMA-Kanal für generieren des Signals ?
LED_BRIGHTNESS = 100 # Helligkeit
LED_INVERT = False # Falls Transistor: True

matrix = [[0 for x in range(0, LED_COUNT)]for y in range(1,7)] # Erschaffen einer Liste, in der sechs Listen enthalten sind

t = 1 # Zeitabschnitt  
T = 2 # Umlaufzeit
i = 0 # Variable für die for-Schleife
z = 0 # für die while-Dauerschleife

magnetschalter = False # kann später noch in komplexere funktion umgesetzt werden

x = 0 # Variable für die for-Schleife

for i in range(0, LED_COUNT): # Setzen der Radien; sollte später aus einer Textdatei ausgelesen werden
    x = x + 0.7
    matrix[0][i] = x
    
for i in range(0,1):
    k = 2*pi*t/T #Ausrechnen des Winkels im Bogenmaß
    x = 0 #für die For-Schleife
    for i in range(0, LED_COUNT): # da wir mit der Listenrechnung nichts sinnvolles erhielten, Doppelung der For-Schleife
        x = x + 0.7
        matrix[1][i] = (cos(k) * -1 * x)  #Berechnung der X-Koordinate
        matrix[2][i] = (sin(k) * x)  #Berechnung der Y Koordinate
    print(matrix)

# for i in range(0, LED_COUNT):
#     farbe = pix[matrix[1][i], matrix[2][i]] #auslesen eines Pixels
#     _ = 0
#     for _ in range(0, LED_COUNT):
#         r = farbe[0]
#     for _ in range(0, LED_COUNT):
#         g = farbe[1]
#     for _ in range(0, LED_COUNT):
#         b = farbe[2]
#     matrix[3] = r # Zuweisung der Rot-Werte
#     matrix[4] = g # Zuweisung der Grünwerte
#     matrix[5] = b # Zuweisung der Blau-Werte

for i in range(0, LED_COUNT):
    farbe = pix[matrix[1][i], matrix[2][i]] #auslesen eines Pixels
    r = farbe[0]
    g = farbe[1]
    b = farbe[2]
    matrix[3] = r # Zuweisung der Rot-Werte
    matrix[4] = g # Zuweisung der Grünwerte
    matrix[5] = b # Zuweisung der Blau-Werte

def farbreihe(streifen, farbe, wait_ms = 50):
    i = 0
    for i in range(0, LED_COUNT):
        streifen.setPixelColor(i+1, farbe)
        streifen.show()

def main():
    while z==0:
        t1 = time() #startzeit t1
        T = 1
        while not magnetschalter:
            t = time() - T				#Ausrechnen der größe des Zeitabschnitts
            berechnungDerPixel(T, t)
            streifen.show()

        T = time() - t1 				#Ausrechnen von T nach T = t2 - t1

if __name__  == '__main__':
    streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    streifen.begin()

    print("Drück Ctrl-C zum beenden.")
    while True:
        farbreihe(streifen, Color(r, g, b))
