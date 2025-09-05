from gpiozero import LED
from time import sleep

led = LED(17)

for _ in range(10):
    led.on()
    print(f"LED blinked {_ + 1} times on {led.pin}")
    sleep(0.5)
    led.off()
    sleep(0.5)