class Verbrauch_einer_Geräteklasse:
    def __init__(self, geräteanzahl, verbrauch, zeit):
        self.geräteanzahl = geräteanzahl
        self.verbrauch = verbrauch
        self.zeit = zeit

    def alles(self):
        gesamtverbrauch = self.geräteanzahl * self.verbrauch * self.zeit
        if 0 <= gesamtverbrauch < 1000:
            print("Der Gesamtverbrauch beträgt",gesamtverbrauch,"Wh.")
        elif 1000 <= gesamtverbrauch:
            kilogesamtverbrauch = gesamtverbrauch / 1000
            print("Der Gesamtverbrauch beträgt",gesamtverbrauch,"kWh.")
        else:
            print("Falscher Wert!")

