from gpiozero import DigitalOutputDevice

stringlights = DigitalOutputDevice(22)

while(True):
    stringlights.on()
