#Dieses Programm wurde im Rahmen des Jugend Forscht Projekts geschrieben 

from time import time
from math import pi, sin, cos
from PIL.Image import open
from neopixel import Adafruit_NeoPixel, Color
from time import time, sleep
import RPi.GPIO as gp

vorführung = True 

im = open("/home/pi/Desktop/JugendForscht/Stop.png")
pix = im.load()

# LED strip configuration:
LED_COUNT       = 70      # Number of LED pixels.
LED_PIN         = 18      # GPIO pin connected to the pixels (must support PWM!).
MAGNET_PIN      = 17
LED_FREQ_HZ     = 1000000  # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS  = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False
ANZAHL_STREIFEN = 2




t = 1       # Zeitabschnitt  
T = 2       # Umlaufzeit
i = 0       # Variable für die for-Schleife
minR = 5    #Mindestradius
w = 0       #Winkelgeschwindigkeit

matrix = [[0 for x in range(0, LED_COUNT)]for y in range(0, 3)] # Erschaffen einer Liste, in der drei Listen (X- und Y-Koordinaten; Radius)enthalten sind

gp.setmode(gp.BCM)          # Welche Nummern für die Pins verwendet werden
gp.setwarnings(False)       # Keine Warnungen
gp.setup(MAGNET_PIN, gp.IN) #Anschluss

for i in range(0, int(LED_COUNT/2)): # Erschaffen der Radien
    matrix[0][i] = i+1+minR

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
    print("Drücke Strg-C zum beenden.")
    line(50)

def bildAuslesen(alpha, rad):

    x = int(round(cos(alpha) * rad + 50))   #Berechnung der X-Koordinate
    y = int(round(sin(alpha) * rad + 50))   #Berrechnung der Y Koordinate

    r,g,b, _ = pix[x, y]                #auslesen eines Pixels
    return Color(g, r, b)

def streifenBedienen():
    global matrix
    global T
    global t
    global streifen

    w = 2 * pi / T #berrechnen der Aktuellen Winkelgeschwindigkeit
    alpha = w * t-pi/2 #ausrechnen des Winkels in Bogenmaß

    if vorführung:
        alpha+=pi

    x = streifen.numPixels()
    u = int(streifen.numPixels()/ANZAHL_STREIFEN)

    for i in range(u):
        u-=1
        streifen.setPixelColor(i, bildAuslesen(alpha + pi, matrix[0][u]))

    for i in range(int(x /ANZAHL_STREIFEN), x):
        streifen.setPixelColor(i, bildAuslesen(alpha, matrix[0][int(i-x/ANZAHL_STREIFEN)]))

    streifen.show()


def main():
    #Diese Variablen werden Global benötigt, da sie in mehreren Methoden benutzt werden
    #Es ist Ressourcensparender die Variablen direkt zu globalisieren, als 
    global T 
    global t
    global t1
    global matrix
    global streifen

    
    #Erschaffen des Led-Streifen-Objekts
    streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    streifen.begin()    #initialisieren des LED-Streifens
    startPrint()        #Drucken der Anfangseinstellungen
    while True:                             
        t1 = time()                                 #startzeit t1
        
        if gp.input(MAGNET_PIN) == False:           #Damit die Zeit nur einmal pro umdrehung gemessen wird

            while gp.input(MAGNET_PIN) == False:
                t = time() - t1                     #Ausrechnen der größe des Zeitabschnitts
                streifenBedienen()
            T = time() - t1                         #Ausrechnen von T nach T = t2 - t1

if __name__ == '__main__':
    main()
