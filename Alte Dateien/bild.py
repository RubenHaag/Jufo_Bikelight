import RPi.GPIO as GPIO

def my_callback():
    print("Hallo")

# Magnetschalter

GPIO.setmode(GPIO.BCM)

MAGNET_GPIO = 17
GPIO.setup(MAGNET_GPIO, GPIO.IN)
print (GPIO.input(MAGNET_GPIO))
GPIO.add_event_detect(MAGNET_GPIO, GPIO.BOTH, callback = my_callback)
