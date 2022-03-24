from time import sleep
from signal import pause
from gpiozero import Button
from gpiozero import RGBLED
from gpiozero import LED
from gpiozero import DigitalOutputDevice
from pygame import mixer

mixer.init()

t1 = mixer.Sound('/home/tsa/animatronics/audio/1.wav')
t2 = mixer.Sound('/home/tsa/animatronics/audio/2.wav')
t3 = mixer.Sound('/home/tsa/animatronics/audio/3.wav')
t4 = mixer.Sound('/home/tsa/animatronics/audio/4.wav')
t5 = mixer.Sound('/home/tsa/animatronics/audio/5.wav')
t6 = mixer.Sound('/home/tsa/animatronics/audio/6.wav')
t7 = mixer.Sound('/home/tsa/animatronics/audio/7.wav')
t8 = mixer.Sound('/home/tsa/animatronics/audio/8.wav')
t9 = mixer.Sound('/home/tsa/animatronics/audio/9.wav')
t10 = mixer.Sound('/home/tsa/animatronics/audio/10.wav')

triggerBtn = Button(17)
interactBtn = Button(18)
indicatorLED = RGBLED(27, 23, 24)
stringLEDs = DigitalOutputDevice(22)

signal1 = DigitalOutputDevice(5)
signal2 = DigitalOutputDevice(6)

signal1.off()
signal2.off()

indicatorLED.color = (1, 0 , 0)

while True:
    triggerBtn.wait_for_press()
    print("Initialized")
    indicatorLED.color = (0, 0, 1)
    stringLEDs.off()

    triggerBtn.wait_for_release()
    print("Starting Sequence")
    indicatorLED.color = (0, 1, 0)
    stringLEDs.on()
    signal1.blink(1, 1, 1)

    sleep(1)
    t1.play()
    sleep(t1.get_length())

    sleep(2)
    t2.play()
    sleep(t2.get_length())

    t3.play()
    sleep(t3.get_length())

    t4.play()
    sleep(t4.get_length())

    t5.play()
    sleep(t5.get_length())

    t6.play()
    sleep(t6.get_length())

    t7.play()
    sleep(t7.get_length())

    print("Sequence Paused")
    print("Waiting for input...")
    indicatorLED.color = (0, 0, 1)
    interactBtn.wait_for_press()
    print("Sequence Resumed")
    indicatorLED.color = (0, 1, 0)
    signal2.blink(1, 1, 1)

    t8.play()
    sleep(t8.get_length())

    t9.play()
    sleep(t9.get_length())

    t10.play()
    sleep(t10.get_length())
    sleep(1)

    print("Sequence Complete")
    indicatorLED.color = (1, 0, 0)