from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)

full = (
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111
)


lcd.create_char(0, full)
lcd.create_char(1, smiley)

for i in range(20):
    lcd.write_string(chr(0))
    sleep(0.5)

lcd.write_string(chr(1))
sleep(2)