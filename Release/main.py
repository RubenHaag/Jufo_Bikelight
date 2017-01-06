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
breite, höhe = im.size	#die Breite und die höhe des Bildes wird ausgelesen

# LED strip configuration:
LED_COUNT       = 70      	# Number of LED pixels.
LED_PIN         = 18      	# GPIO pin connected to the pixels (must support PWM!).
MAGNET_PIN      = 17		# Nummer des Magnet Pins
LED_FREQ_HZ     = 1000000  	# Frequenz der Led's in Hz
LED_DMA         = 5       	# DMA Kanal, des Led pins(siehe C code der Library)
LED_BRIGHTNESS  = 100     	# Set to 0 for darkest and 255 for brightest
LED_INVERT      = False		# Wenn ein transistor zwischengeschaltet ist Aktivieren
ANZAHL_STREIFEN = 2			# Anzahl der verwendeten Led Streifen pro pin


t = 1       # Zeitabschnitt  
T = 2       # Umlaufzeit
i = 0       # Variable für die for-Schleife
minR = 5    # Mindestradius
w = 0       # Winkelgeschwindigkeit

# erschaffen einer Liste, in der drei Listen enthalten sind
# matrix[0] = r; matrix[1] =
matrix = [0 for x in range(0, LED_COUNT)]
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

	x = int(round(cos(alpha) * rad + breite))   #Berechnung der X-Koordinate
	y = int(round(sin(alpha) * rad + höhe))   #Berrechnung der Y Koordinate

	r,g,b, _ = pix[x, y]                #auslesen eines Pixels
	return Color(g, r, b)

def streifenBedienen():
	global matrix
	global T
	global t
	global streifen
	global w

	alpha = w * t-pi/2 #ausrechnen des Winkels in Bogenmaß

	if vorführung:
		alpha+=pi

	n = streifen.numPixels()
	u = int(n/ANZAHL_STREIFEN)

	for i in range(u):
		u-=1
		streifen.setPixelColor(i, bildAuslesen(alpha + pi, matrix[u]))

	u = int(n/ANZAHL_STREIFEN)

	for i in range(int(x /ANZAHL_STREIFEN), n):
		streifen.setPixelColor(i, bildAuslesen(alpha, matrix[i-u]))

	streifen.show()


def main():
	# Diese Variablen werden Global benötigt, da sie in mehreren Methoden benutzt werden
	# Es ist Ressourcensparender die Variablen direkt zu globalisieren, als sie als
	# Parameter zu übergeben
	global T 
	global t
	global t1
	global matrix
	global streifen
	global w

	gp.setmode(gp.BCM)          # Welche Nummern für die Pins verwendet werden
	gp.setwarnings(False)       # Keine Warnungen
	gp.setup(MAGNET_PIN, gp.IN) # Anschluss

	
	#Erschaffen des Led-Streifen-Objekts
	streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

	streifen.begin()    #initialisieren des LED-Streifens
	startPrint()        #Drucken der Anfangseinstellungen


	while True:                             
		t1 = time()                                 #startzeit der umdrehung t1
		
		if gp.input(MAGNET_PIN) == False:           #Damit die Zeit nur einmal pro umdrehung gemessen wird

			while gp.input(MAGNET_PIN) == False:
				t = time() - t1               #Ausrechnen der größe des Zeitabschnitts
				w = 2 * pi / T                #berrechnen der Aktuellen Winkelgeschwindigkeit
				streifenBedienen()

			T = time() - t1                   #Ausrechnen von T nach T = t2 - t1

if __name__ == '__main__':
	main()
