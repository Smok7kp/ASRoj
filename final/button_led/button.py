from gpiozero import LED, Button
from signal import pause

led = LED(5)
button = Button(26)
to_continue = True

while to_continue:
    if button.is_pressed:
        print("pressed")
        led.on()

        pause()
    else: 
        print("realeased")
        led.off()

