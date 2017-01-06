# Jufo_Bikelight

### Hierbei handelt es sich um den Projektordner für ein Jugend Forscht Projekt

Ist es möglich kostengünstig eine Fahrradfelgenbeleuchtung, welche in der Lage ist auf einem Speichenrad ein Bild zu erzeugen, herzustellen? Dies soll mit Hilfe eines von uns selbst erstellten Systems und Programmes möglich gemacht werden. Das System besteht aus einem Raspberry PI Zero, einem Akku, und einem LED-Streifen und das Programm für die radiale, geschwindigkeitsabhängige Ansteuerung der LEDs haben wir selbst in Python 3 programmiert. Mit der Adafruit-Neopixel-Library kann unser Programm auf den LED-Streifen zugreifen und die einzelnen Licht emittierenden Dioden ansteuern. Mit der PIL kann unser Programm ein beliebiges Bild auslesen und uns die Farbwerte jedes einzelnen Pixels des Bildes angeben. Es kann außerdem den Stromfluss eines Magnetschalters überprüfen, womit es die Winkelgeschwindigkeit ermittelt und damit ein geschwindigkeitsunabhängiges Bild erstellt. Aufgrund der Trägheit des Auges des Betrachters und der konstant hohen Geschwindigkeit des Rades, entsteht für den Betrachter der Eindruck eines ruhenden  Bildes. Somit gelingt es uns, das ruhende Bild zu erschaffen. 

Um sich ein Bild von 
