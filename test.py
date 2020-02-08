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

menu_options = {
    1: "Tee juoma",
    2: "Sulje"
}

current_option = 1

drinks = {
    1:"Rum&Coke"
}

current_drink = 1



while True:
    lcd.clear()
    lcd.write_string(menu_options[current_option])
    sleep(BOUNCE)
    if button_right.wait_for_active():
        lcd.clear()
        if current_option == 2:
            current_option -= 1
        else:
            current_option += 1
    if button_left.wait_for_active():
        if current_option == 1:
            lcd.clear()
            lcd.write_string(drinks[current_drink])
            sleep(5)

        elif current_option == 2:
            lcd.clear()
            lcd.write_string("haha")

        else:
            lcd.backlight_enabled = False
            sys.exit()
