from gpiozero import LED, Button
from time import sleep

led = LED(27)
button = Button(17)

button_count = 0
while True:
    button.wait_for_press()
    button_count += 1
    print(f"Button pressed {button_count} times on {button.pin}")
    led.toggle()
    sleep(0.5) #This is here because the RPI will detect multiple presses on one physical press.
