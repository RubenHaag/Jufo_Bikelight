import time
import RPi.GPIO as gp 
from neopixel import *



# LED strip configuration:
LED_COUNT      = 144      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistorlevel shift)

def reihe (streifen, farbe, wait_ms = 50):
    for i in range (144):
        streifen.setPixelColor(i, farbe)
        streifen.show()
        time.sleep(wait_ms/1000.0)

if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	streifen = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	streifen.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
		reihe(streifen, Color(159, 159, 159))


