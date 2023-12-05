import RPi.GPIO as led
import time

led_pin = 2 #rosso
led_pin_blue = 4
led_pin_giallo = 3

led.setmode(led.BCM)
def blink(luce):
    led.setup(luce,led.OUT)
    led.output(luce, led.HIGH)
    time.sleep(3)
    led.output(luce,led.LOW)
t=0

while t < 60:
    f = blink(led_pin)
    z = blink(led_pin_blue)
    c=blink(led_pin_giallo)
    t +=1
