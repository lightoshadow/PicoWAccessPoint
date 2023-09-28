import socket
import network
import ssd1306

ssid = "Auguri Silvio"
password = "fracassi"


i2c = machine.I2C(1,sda=machine.Pin(18), scl=machine.Pin(19),freq=200000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text("powering on...",0,9,1)
display.show()

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password) 
ap.active(True)

while ap.active == False:
  pass

display.fill(0)
print("Access point active")
display.text("ssid =",0,9,1)
display.text(ssid,0,19,1)
display.text("password =",0,28,1)
display.text(password,0,37,1)

display.show()
print(ap.ifconfig())