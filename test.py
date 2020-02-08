from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep

button = Button(17)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)



strings = ["Hello", "R2", "What", "would", "you", "like", "on", "your", "pizza"]
for i in range(10):
    if button.wait_for_active():
        lcd.write_string(strings[i])
        sleep(0.5)
        lcd.clear()
