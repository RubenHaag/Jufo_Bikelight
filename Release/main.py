#Dieses Programm wurde im Rahmen des Jugend Forscht Projekts geschrieben

from time import time, sleep
from math import pi, sin, cos
from PIL.Image import open
from neopixel import Adafruit_NeoPixel, Color
import RPi.GPIO as gp


path = "/home/pi/Jufo_Bikelight/Release/Bilder/Herz"

breite, höhe = im.size	#die Breite und die höhe des Bildes wird ausgelesen
breite = breite /2 	#damit der Koordinatenmittelpunkt in die mitte des Bildes Kommt
höhe = höhe / 2 


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

# erschaffen einer Liste ür die R Radien
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
	print("Aktuelle Geschwindigkeit:")
	line(50)
	print("xx km/h")

def bildNeuLaden():
	global pix
	# Ein Bild kann nun als png oder als jpg gegeben sein
	try:
		im = open(path + "png")
	except:
		im = open(path + "jpeg")
	else:
		im = open(path + "jpg")
	pix = im.load()

def bildAuslesen(winkel, rad):

	x = int(round(cos(winkel) * -rad + breite))   # Berechnung der X-Koordinate
	y = int(round(sin(winkel) * rad + höhe))   	# Berechnung der Y Koordinate

    try:
		r,g,b = pix[x, y]		# auslesen eines Pixels
	except:
		r,g,b,_ = pix[x, y]





def streifenBedienen(t, w):
	global radien
	global streifen

	alpha = w * t + pi/2 + pi/6 #ausrechnen des Winkels in Bogenmaß

	beta  = alpha + pi / 2
	gamma = beta  + pi / 2
	delta = gamma + pi / 2


	n = streifen.numPixels()
	u = int(n/ANZAHL_STREIFEN)
	M = int(n/2)

	for i in range(u):
		u-=1		#u wird heruntergezählt, da dieser Teil des Led Streifens gespiegelt ist
		streifen.setPixelColor(i, bildAuslesen(alpha, radien[u])) # alpha + pi, da dieser LED-Streifen gespiegelt ist
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

def main():
	global radien
	global streifen
	n = 0			#Zählervariable

	gp.setmode(gp.BCM)          # Welche Nummern für die Pins verwendet werden
	gp.setwarnings(False)       # Keine Warnungen
	gp.setup(MAGNET_PIN, gp.IN) # Anschluss

	
    #Erschaffen des Led-Streifen-Objekts
    streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, 
                                 LED_INVERT, LED_BRIGHTNESS)


	streifen.begin()    #initialisieren des LED-Streifens
	startPrint()        #Drucken der Anfangseinstellungen



    while True:                             
        t1 = time()		#Startzeit der Umdrehung t1
		
        if gp.input(MAGNET_PIN) == False:	#Zeitmessung einmal je Umdrehung
			
            w = 2 * pi / T 	#Berrechnen der Aktuellen Winkelgeschwindigkeit
			
			while gp.input(MAGNET_PIN) == False:
				t = time() - t1 			#Ausrechnen der größe des Zeitabschnitts

				if t < 5:
					streifenBedienen(t, w)
					streifen.show()
				else:
					for i in range(0, LED_COUNT):
						streifen.setPixelColor(i, Color(0,0,0))
						streifen.show()
			n++
			if n > 3:				#jede dritte Umdrehung wird das bild neu in den Zwischenspeicher gepackt
				n = 0
				im = open(path)
				pix = im.load()

			print("\b\b\b\b\b\b\b" + str(int(w * 0.3*3.6)) + " km/h")
			T = time() - t1              #Ausrechnen von T nach T = t2 - t1


	
if __name__ == '__main__':
    main()
