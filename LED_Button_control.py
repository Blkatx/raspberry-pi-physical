from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

button_count = 0
while True:
    button.wait_for_press()
    print("Button pressed")
    button_count += 1
    if button_count % 2 == 0:
        led.on()
    elif button_count % 2 == 1:
        led.off()