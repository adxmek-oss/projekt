import utime
from machine import I2C, Pin
from lcd import Lcd_i2c   # ← tvůj driver

# Nastavení I2C pinů (uprav podle zapojení)
I2C_SDA = 0
I2C_SCL = 1

# Globální proměnná pro LCD
lcd = None

def init_display():
    global lcd
    i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=400000)
    lcd = Lcd_i2c(i2c, cols=16, rows=2)
    lcd.clear()
    return lcd


def show_message(text):
    lcd.clear()
    lcd.set_cursor(0, 0)
    lines = text.split("\n")
    for i, line in enumerate(lines[:2]):
        lcd.set_cursor(0, i)
        lcd.write(line[:16])


def show_coords(lat, lon):
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.write("Lat: {:.4f}".format(lat))
    lcd.set_cursor(0, 1)
    lcd.write("Lon: {:.4f}".format(lon))


def show_weather(data):
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.write("Temp: {:.1f}C".format(temp))
    lcd.set_cursor(0, 1)
    lcd.write(desc[:16])