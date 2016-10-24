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

def line(laenge):
    s = ""
    for i in range(0, laenge):
        s += "-"
    print(s)
    
def startPrint():
    #anzeigen der Starteinstellungen
    str1 = "Led Bikelight"
    str2 = "\nDie Momentanen Einstellungen sind:"
    line(30)
    print(str1)
    line(30)
    print(str2)
    print("")
    print("Laenge des Led-Streifens = " + LED_COUNT)
    print("GPIO-Pin = " = LED_PIN)
    print("f in Hz = " + LED_FREQ_HZ)
    print("DMA Kanal = " + LED_DMA)
    print("LED HElligkeit = " + LED_BRIGHTNESS)
    print("Invertiertes Signal = " + LED_INVERT)
    print("Die Radien sind:\n\t" + matrix[0])
    line(30)
    print("Drück Strg-C zum beenden.")
    
def bildAuslesen(t, T):
    global matrix
    global streifen
    for i in range(0, LED_COUNT):
        k = 2*pi*t/T #ausrechnen des Winkels in rad
        matrix[1][i] = (round(math.cos(k) * matrix[0][i], 1)*32) #berechnung der X-Koordinate
        matrix[2][i] = (round(math.sin(k) * matrix[0][i], 1)*32) #Berrechnung der Y Koordinate
        
        r, g, b, _ = pix[matrix[1][i], matrix[2][i]] #auslesen eines Pixels
        
        matrix[3] = r   # Zuweisung der Rot-Werte
        matrix[4] = g   # Zuweisung der Grünwerte
        matrix[5] = b   # Zuweisung der Blau-Werte
        streifen.setPixelColor(i+1, (matrix[3], matrix[4], matrix[5]))
                        # Zuweisung der Pixelfarben fuer den LED-Streifen


def main():
    streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    streifen.begin()                        #starten des LED-Streifens
    startPrint()                            #Drucken der Anfangseinstellungen
    while z==0:                             #Dauerschleife fuer die Zeit
        t1 = time()                         #startzeit t1 
        while not magnetschalter:
            if T is not 0:                  #dient der verhinderung von Fehlern in der ersten Umdrehung
                t = time() - T				#Ausrechnen der größe des Zeitabschnitts
                bildAuslesen;(t, T)
                streifen.show()

        T = time() - t1 				    #Ausrechnen von T nach T = t2 - t1

if __name__  == '__main__':
    main()
