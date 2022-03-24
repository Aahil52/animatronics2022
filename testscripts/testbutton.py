from gpiozero import Button

btn = Button(20)

btn.wait_for_press()

print("Button pressed")