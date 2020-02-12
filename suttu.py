from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

frame1,frame2,frame3 = (
    0b11111,
	0b10001,
	0b11001,
	0b10111,
	0b10001,
	0b10001,
	0b10001,
	0b11111
),(
    0b11111,
	0b10001,
	0b10001,
	0b11111,
	0b10001,
	0b10001,
	0b10001,
	0b11111
),(
    0b11111,
	0b10001,
	0b10011,
	0b11101,
	0b10001,
	0b10001,
	0b10001,
	0b11111
)
splash = (
	0b00000,
	0b00000,
	0b00100,
	0b00010,
	0b00000,
	0b01000,
	0b00100,
	0b00000
)
lcd.create_char(0, frame1)
lcd.create_char(1, frame2)
lcd.create_char(2, frame3)
lcd.create_char(3, splash)

try:
	while True:
		for i in range(3):
			lcd.clear()
			lcd.cursor_pos = (1, 6 + i)
			lcd.write_string(chr(i))
			lcd.cursor_pos = (1, 11 - i)
			lcd.write_string(chr(max(i-2, 2-i)))
			sleep(0.5)
		lcd.cursor_pos = (0, 8)
		lcd.write_string(chr(3))
		lcd.cursor_pos = (0, 9)
		lcd.write_string(chr(3))
except KeyboardInterrupt:
	lcd.backlight_enabled = False
	lcd.close()
    