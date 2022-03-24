from time import sleep
from gpiozero import RGBLED

indicatorLED = RGBLED(18, 23, 24)

print("Red")
indicatorLED.color = (1, 0, 0)
sleep(1)
print("Green")
indicatorLED.color = (0, 1, 0)
sleep(1)
print("Blue")
indicatorLED.color = (0, 0, 1)
sleep(1)