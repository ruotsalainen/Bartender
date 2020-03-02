from time import sleep

top_left = (
	0b00011,
	0b01111,
	0b11111,
	0b11100,
	0b11000,
	0b11000,
	0b11000,
	0b11000
)

top = (
	0b11111,
	0b11111,
	0b11111,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000
)

top_right = (
	0b11000,
	0b11110,
	0b11111,
	0b00111,
	0b00011,
	0b00011,
	0b00011,
	0b00011
)

right = (
    0b00011,
	0b00011,
	0b00011,
	0b00011,
	0b00011,
	0b00011,
	0b00011,
	0b00011
)

bottom_right = (
    0b00011,
	0b00011,
	0b00011,
	0b00011,
	0b00111,
	0b11111,
	0b11110,
	0b11000
)

bottom = (
    0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b11111,
	0b11111,
	0b11111
)

bottom_left = (
	0b11000,
	0b11000,
	0b11000,
	0b11000,
	0b11100,
	0b11111,
	0b01111,
	0b00011
)

left = (
    0b11000,
	0b11000,
	0b11000,
	0b11000,
	0b11000,
	0b11000,
	0b11000,
	0b11000
)

time = 0.05

def draw_ring(lcd):

	lcd.create_char(0, top_left)
	lcd.create_char(1, top)
	lcd.create_char(2, top_right)
	lcd.create_char(3, right)
	lcd.create_char(4, bottom_right)
	lcd.create_char(5, bottom)
	lcd.create_char(6, bottom_left)
	lcd.create_char(7, left)

	lcd.write_string(chr(0))
	sleep(time)
	for i in range(18):
	    lcd.write_string(chr(1))
	    sleep(time)
	lcd.write_string(chr(2))
	lcd.cursor_pos = (1, 19)
	for i in range(2):
	    lcd.write_string(chr(3))
	    lcd.cursor_pos = (2, 19)
	    sleep(time)
	lcd.cursor_pos = (3, 19)
	lcd.write_string(chr(4))
	sleep(time)

	col = 18
	for i in range(18):
	    lcd.cursor_pos = (3, col)
	    lcd.write_string(chr(5))
	    col -= 1
	    sleep(time)
	lcd.cursor_pos = (3, 0)
	lcd.write_string(chr(6))
	sleep(time)

	row = 2
	for i in range(2):
	    lcd.cursor_pos = (row, 0)
	    lcd.write_string(chr(7))
	    row -= 1
	    sleep(time)