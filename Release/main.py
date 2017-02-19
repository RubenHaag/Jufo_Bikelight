#Dieses Programm wurde im Rahmen des Jugend Forscht Projekts geschrieben

from time import time, sleep
from math import pi, sin, cos
from PIL.Image import open
from neopixel import Adafruit_NeoPixel, Color
import RPi.GPIO as gp

im = open("/home/pi/Jufo_Bikelight/Release/Ihr_Bild_hier.png")
pix = im.load()
breite, höhe = im.size	#die Breite und die Höhe des Bildes wird ausgelesen
breite = breite / 2
höhe = höhe / 2 


# LED strip configuration:
LED_COUNT       = 140      	# Number of LED pixels.
LED_PIN         = 18      	# GPIO pin connected to the pixels (must support PWM!).
MAGNET_PIN      = 17		# Nummer des Magnet Pins
LED_FREQ_HZ     = 800000  	# Frequenz der Led's in Hz
LED_DMA         = 5       	# DMA Kanal, des Led pins(siehe C code der Library)
LED_BRIGHTNESS  = 40    	# Set to 0 for darkest and 255 for brightest
LED_INVERT      = False		# Wenn ein transistor zwischengeschaltet ist Aktivieren
ANZAHL_STREIFEN = 4			# Anzahl der verwendeten Led Streifen pro pin

# LED-Streifen-Konfiguration:
LED_COUNT       = 140      	# LED-Anzahl.
LED_PIN         = 18      	# GPIO-Pin für die LEDs (muss PWM unterstützen)
MAGNET_PIN      = 17		# Magnet-Pin-Nummer
LED_FREQ_HZ     = 700000  	# Frequenz der LEDs in Hz
LED_DMA         = 5       	# DMA Kanal, des LED-Pins
LED_BRIGHTNESS  = 40    	# 0->dunkel; 255->hell
LED_INVERT      = False		# Falls Transistor zwischengeschaltet,Aktivieren
ANZAHL_STREIFEN = 4		# Anzahl der verwendeten LED-Streifen
t = 1       # Zeitabschnitt  
T = 2       # Umlaufzeit
i = 0       # Variable Für die for-Schleife
minR = 5    # Mindestradius
w = 0       # Winkelgeschwindigkeit

# erschaffen einer Liste

radien = [0 for x in range(0, int(LED_COUNT/ANZAHL_STREIFEN))]
for i in range(0, int(LED_COUNT/ANZAHL_STREIFEN)): 	# Erschaffen der Radien
    radien[i] = int(i+1+minR)

# Startanzeige

def line(länge):
	s = ""
	for i in range(0, länge):
		s += "-"
	print(s)
	

def startPrint():   
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
	print("LED Helligkeit: " + str(LED_BRIGHTNESS))
	print("Invertiertes Signal: " + str(LED_INVERT))
	print("")
	line(50)
	print("Drücke Strg-C zum beenden.")
	line(50)


def bildAuslesen(winkel, rad):

	x = int(round(cos(winkel) * rad + breite))   # Berechnung der X-Koordinate
	y = int(round(sin(winkel) * rad + höhe))   	# Berechnung der Y Koordinate

    try:
		r,g,b = pix[x, y]		# auslesen eines Pixels
	except:
		r,g,b,_ = pix[x, y]


# Startanzeige

def line(länge):
	s = ""
	for i in range(0, länge):
		s += "-"
	print(s)

def startPrint():   
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
	print("LED Helligkeit: " + str(LED_BRIGHTNESS))
	print("Invertiertes Signal: " + str(LED_INVERT))
	print("")
	line(50)
	print("Drücke Strg-C zum beenden.")
	line(50)

def streifenBedienen(t, w):
	global radien
	global streifen

	alpha = w * t #ausrechnen des Winkels in Bogenmaß
	beta  = alpha + pi / 2
	gamma = beta  + pi / 2
	delta = gamma + pi / 2

	#if vorführung:	#das Entstehende Bild wird für eine Vorführung um 180° gedreht
	#	alpha+=pi

	n = streifen.numPixels()
	u = int(n/ANZAHL_STREIFEN)
	M = int(n/2)

	for i in range(u):
		u-=1		#u wird heruntergezählt, da dieser Teil des Led Streifens gespiegelt ist
		streifen.setPixelColor(i, bildAuslesen(alpha, radien[u])) # alpha + pi, da dieser LED streifen gespiegelt ist
		streifen.setPixelColor(i + M, bildAuslesen(gamma, radien[u]))

	u = int(n/ANZAHL_STREIFEN)

	for i in range(u, M):

		streifen.setPixelColor(i, bildAuslesen(beta, radien[i-u-1]))

		streifen.setPixelColor(i + M, bildAuslesen(delta, radien [i-u-1]))

def streifenBedienen():
    global radien
    global T
    global t
    global streifen
    global w

    alpha = w * t 				#Ausrechnen des Winkels in Bogenmaß
    beta  = alpha + pi / 2
    gamma = beta  + pi / 2
    delta = gamma + pi / 2

    n = streifen.numPixels()
    u = int(n/ANZAHL_STREIFEN)
    M = int(n/2)

    for i in range(u):
        u-= 1		
        streifen.setPixelColor(i, bildAuslesen(alpha, radien[u]))              
        streifen.setPixelColor(i, bildAuslesen(gamma, radien[u])) 
		
    u = int(n/ANZAHL_STREIFEN)

    for i in range(u, M):
        streifen.setPixelColor(i, bildAuslesen(beta, radien[i-u]))
        streifen.setPixelColor(i + M, bildAuslesen(delta, radien[i-u]))
    streifen.show()

def main():
	global radien
	global streifen
	T=2

	gp.setmode(gp.BCM)          # Welche Nummern für die Pins verwendet werden
	gp.setwarnings(False)       # Keine Warnungen
	gp.setup(MAGNET_PIN, gp.IN) # Anschluss

    global T 
    global t
    global t1
    global radien
    global streifen
    global w

    gp.setmode(gp.BCM)          # GPIO-Nummern verwenden
    gp.setwarnings(False)       # Keine Warnungen
    gp.setup(MAGNET_PIN, gp.IN) # Anschluss
	
    #Erschaffen des Led-Streifen-Objekts
    streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, 
                                 LED_INVERT, LED_BRIGHTNESS)

    streifen.begin()    #Initialisieren des LED-Streifens
    startPrint()        #Drucken der Startanzeige


    while True:                             
        t1 = time()		#Startzeit der Umdrehung t1
		
        if gp.input(MAGNET_PIN) == False:	#Zeitmessung einmal je Umdrehung
			
            w = 2 * pi / T 	#Berrechnen der Aktuellen Winkelgeschwindigkeit
			
			while gp.input(MAGNET_PIN) == False:
				t = time() - t1 			#Ausrechnen der größe des Zeitabschnitts
				#print(t)
				streifenBedienen(t, w)
				streifen.show()
			T = time() - t1              #Ausrechnen von T nach T = t2 - t1

		
		while gp.input(MAGNET_PIN) == False:
		    t = time() - t1   #Größe des Zeitabschnitts
		    streifenBedienen()
	  T = time() - t1                   #Ausrechnen von T nach T = t2 - t1
	print (w * 0,3556)
	
if __name__ == '__main__':
    main()
