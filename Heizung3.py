class Heizung:
	def __init__(self, art, größe, anzahl, ort, verwendungszeit, modulverbrauch, gesamtverbrauch):
		self.art = art
		self.größe = größe
		self.anzahl = anzahl
		self.ort = ort
		self.verwendungszeit = verwendungszeit
		self.modulverbrauch = modulverbrauch
		self.gesamtverbrauch = gesamtverbrauch

		
>>> def alles():
	self.gesamtverbrauch = self.anzahl * self.modulverbrauch
