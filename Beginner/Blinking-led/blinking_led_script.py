from gpiozero import LED
from time import sleep

# Define the LED pin
led = LED(18)

# Blink in a loop
while True:
    led.on()
    print("LED on")
    sleep(1)
    led.off()
    print("LED off")
    sleep(1)
