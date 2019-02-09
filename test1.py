from gpiozero import LED
from time import sleep

led25 = LED(25)

while True:
    led25.on()
    sleep(0.35)
    led25.off()
    sleep(0.15)
    
