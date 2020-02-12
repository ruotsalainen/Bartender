from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

a = (
    0b11111,
	0b10001,
	0b11001,
	0b10111,
	0b10001,
	0b10001,
	0b10001,
	0b11111
)

b = (
    0b11111,
	0b10001,
	0b10001,
	0b11111,
	0b10001,
	0b10001,
	0b10001,
	0b11111
)

c = (
    0b11111,
	0b10001,
	0b10011,
	0b11101,
	0b10001,
	0b10001,
	0b10001,
	0b11111
)


while True:
    for i in range(3):
        lcd.clear()
        lcd.cursor_pos = (1, 6)
        lcd.write_string(chr(i))
        sleep(0.2)
    