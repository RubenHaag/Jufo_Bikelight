from time import time
from math import sin
from math import cos
from math import pi
from PIL.Image import *
from neopixel import *
from time import sleep
import RPi.GPIO as gp


im = open("/home/pi/Desktop/JugendForscht/Colbert.png")
pix = im.load()

LED_COUNT = 70# Anzahl der LED's auf dem LED-Streifen
LED_PIN = 18 # GPIO-Nummer des Pin's, mit dem man den LED-Streifen ansteuert.
LED_FREQ_HZ = 80000 # Blinkfrequenz
LED_DMA   = 5  # DMA-Kanal für generieren des Signals
LED_BRIGHTNESS = 100# Helligkeit
LED_INVERT = False # Falls Transistor: True
MIN_RAD = 5

gp.setmode(gp.BCM) # Welche Nummern für die Pins verwendet werden
gp.setwarnings(False) # Keine Warnungen
gp.setup(17, gp.IN) #Anschluss

matrix = [[0 for x in range(0, LED_COUNT)]for y in range(0, 3)] # Erschaffen einer Liste, in der drei Listen (X- und Y-Koordinaten; Radius)enthalten sind

t = 1 # Zeitabschnitt  
T = 2 # Umlaufzeit
i = 0 # Variable für die for-Schleife

for i in range(0, int(LED_COUNT/2)): # Erschaffen der Radien
    matrix[0][i] = i+1+MIN_RAD


def line(länge):
    s = ""
    for i in range(0, länge):
        s += "-"
    print(s)
    

def startPrint():   # Startanzeige
    str1 = "Led Bikelight"
    str2 = "\nDie Momentanen Einstellungen sind:"
    line(50)
    print(str1)
    line(50)
    print(str2)
    print("")
    print("Anzahl der Led's: " + str(LED_COUNT))
    print("GPIO-Pin: " + str(LED_PIN))
    print("f in Hz: " + str(LED_FREQ_HZ))
    print("DMA Kanal: " + str(LED_DMA))
    print("LED HElligkeit: " + str(LED_BRIGHTNESS))
    print("Invertiertes Signal: " + str(LED_INVERT))
    print("")
    line(50)
    print("Drück Strg-C zum beenden.")
    line(50)

    
def bildAuslesen():
    global matrix
    global T
    global t
    global streifen

    
    w = 2 * pi / T #berrechnen der Aktuellen Winkelgeschwindigkeit
    k = w * t #ausrechnen des Winkels in Bogenmaß
    for i in range(LED_COUNT, 0):
        if i > (LED_COUNT / 2):
            k += pi
            u = int(LED_COUNT - i)
            
        else:
            u = i
        rad = matrix[0][u]

        matrix[1][i] = int(round(cos(k) * rad + 50, 0))	#Berechnung der X-Koordinate
        matrix[2][i] = int(round(sin(k) * rad + 50, 0))	#Berrechnung der Y Koordinate

        r,g,b, _ = pix[matrix[1][i], matrix[2][i]] #auslesen eines Pixels
        streifen.setPixelColor(i+1, Color(r, g, b))
    streifen.show()


def main():
    global T 
    global t
    global t1
    global matrix
    global streifen

    
    #   initialisierung des Led streifens
    streifen.begin()  #starten des LED-Streifens
    startPrint()                            #Drucken der Anfangseinstellungen
    while True:                             #Dauerschleife fuer die Zeit
        t1 = time()                         #startzeit t1
        
        if gp.input(17) == False:           #Damit die Zeit nur einmal pro umdrehung gemessen wird

            while gp.input(17) == False:
                t = T + time() - t1        #Ausrechnen der größe des Zeitabschnitts
                bildAuslesen()
            T = time() - t1                     #Ausrechnen von T nach T = t2 - t1

streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

main()