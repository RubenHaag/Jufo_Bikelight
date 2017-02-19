import RPi.GPIO as gp
gp.setmode(gp.BCM)          # Welche Nummern für die Pins verwendet werden
gp.setwarnings(False)       # Keine Warnungen
gp.setup(17, gp.IN) # Anschluss
while True:
	if gp.input(17):
		print("JA")
	pass