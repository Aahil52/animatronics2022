from gpiozero import DigitalOutputDevice

signal1 = DigitalOutputDevice(5)
signal2 = DigitalOutputDevice(6)

while(True):    
    signal1.off()