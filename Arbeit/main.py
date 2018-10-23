import serial
import struct
import sys
import time


ser = serial.Serial()
ser.port = "/dev/ttyUSB0"       #Todo: Port muss noch überprüft werden
ser.baudrate = 9600             #Bitrate

ser.open()
ser.flushInput()

def dumpData(data):
    out = ""
    for i in data:
        out.join(i.encode('hex'))
    
    print(out)

def processFrame(data):
    dumpData(data)
    r = struct.unpack('<HHxxBBB', data[2:])
    pm25 = r[0]/10.0
    pm10 = r[1]/10.0

    checksum = sum(ord(i) for i in data[2:8])%256 #Todo: anders Schreiben, Warum mod 256?

    print("PM2.5: " + pm25 + "µg/m^3 \t PM10: "+ pm10 + "µg/m^3 \t")    #Todo: Feuchtekorrektur wird noch benötigt
    if(checksum == r[2] and r[3] == 0xab):
        print("Checksum OK")

    else:
        print("CHecksum not OK")
    

def sensorRead():
    byte = 0
    while byte != "\xaa":
        byte = ser.read(size=1)
    data = ser.read(size=10)

    if data[0] == "\xc0":
        processFrame(byte + data)

# 0xAA, 0xB4, 0x06, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x06, 0xAB
def wakeSensor():
    bytes = ['\xaa', #head
            '\xb4', #command 1
            '\x06', #data byte 1
            '\x01', #data byte 2 (set mode)
            '\x01', #data byte 3 (sleep)
            '\x00', #data byte 4
            '\x00', #data byte 5
            '\x00', #data byte 6
            '\x00', #data byte 7
            '\x00', #data byte 8
            '\x00', #data byte 9
            '\x00', #data byte 10
            '\x00', #data byte 11
            '\x00', #data byte 12
            '\x00', #data byte 13
            '\xff', #data byte 14 (device id byte 1)
            '\xff', #data byte 15 (device id byte 2)
            '\x05', #checksum
            '\xab'] #tail
    
    for b in bytes:
        ser.write(b)


def stopSensor():
    bytes = ['\xaa', #head
            '\xb4', #command 1
            '\x06', #data byte 1
            '\x01', #data byte 2 (set mode)
            '\x00', #data byte 3 (sleep)
            '\x00', #data byte 4
            '\x00', #data byte 5
            '\x00', #data byte 6
            '\x00', #data byte 7
            '\x00', #data byte 8
            '\x00', #data byte 9
            '\x00', #data byte 10
            '\x00', #data byte 11
            '\x00', #data byte 12
            '\x00', #data byte 13
            '\xff', #data byte 14 (device id byte 1)
            '\xff', #data byte 15 (device id byte 2)
            '\x05', #checksum
            '\xab'] #tail

    for b in bytes:
        ser.write(b)

def main(args):
    wakeSensor()
    time.sleep(0.5)
    ser.flushInput()
    sensorRead()
    stopSensor()
    time.sleep(0.5)

if __name__ == '__main__':
    sys.exit(main(sys.argv))