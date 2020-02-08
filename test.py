from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep
import sys

button_right = Button(17)
button_left = Button(27)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

BOUNCE = 0.5

drink_options = [
	{"name": "Gin", "value": "gin"},
	{"name": "Rum", "value": "rum"},
	{"name": "Vodka", "value": "vodka"},
	{"name": "Tequila", "value": "tequila"},
	{"name": "Tonic Water", "value": "tonic"},
	{"name": "Coke", "value": "coke"},
	{"name": "Orange Juice", "value": "oj"},
	{"name": "Margarita Mix", "value": "mmix"}
]

current_drink = 0
modified = True

while True:
    if modified:
        lcd.clear()
        lcd.write_string(drink_options[current_drink].get("name"))
        sleep(BOUNCE)
        modified = False

    if button_right.when_activated:
        modified = True
        if current_drink == 7:
            current_drink = 0
        else:
            current_drink += 1
    
    if button_left.when_activated:
        modified = True
        drink_name = drink_options[current_drink].get("name")
        lcd.write_string(" coming right up!")
        sleep(2)
