from time import sleep
from signal import pause
from gpiozero import LED
from gpiozero import Button
from pygame import mixer

mixer.init()

placeholder = mixer.Sound('placeholder.wav')
ph_len = placeholder.get_length()

led = LED(25)
btn = Button(4)

while True:
    btn.wait_for_press()
    print("Initialized")

    btn.wait_for_release()
    print("Starting Sequence")

    # Light and Sound Sequence
    placeholder.play()

    led.blink(.5, .5, round(ph_len))
    sleep(ph_len)

    print("Sequence Complete")
