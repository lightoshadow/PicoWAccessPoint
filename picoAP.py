import socket
import network
import ssd1306
from machine import Pin

ssid = "picoNetwork"
password = "password"

sda = machine.Pin(18)
scl = machine.Pin(19)

i2c = machine.I2C(1,sda=sda, scl=scl,freq=200000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
led = Pin("LED", Pin.OUT)
led.value(0)

display.text("powering on...",0,9,1)
display.show()

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password) 
ap.active(True)

while ap.active == False:
    led.value(0)
    pass

print(ap.ifconfig())

led.value(1)

display.fill(0)
print("Access point active")
display.text("ssid =",0,9,1)
display.text(ssid,0,19,1)
display.text("password =",0,28,1)
display.text(password,0,37,1)

display.show()
