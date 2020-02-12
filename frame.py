from time import sleep

class Frame():
    def __init__(self):
        self.top_left = (
            0b00011,
            0b01111,
            0b11111,
            0b11100,
            0b11000,
            0b11000,
            0b11000,
            0b11000
        )
        self.top = (
            0b11111,
            0b11111,
            0b11111,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000
        )
        self.top_right = (
            0b11000,
            0b11110,
            0b11111,
            0b00111,
            0b00011,
            0b00011,
            0b00011,
            0b00011
        )
        self.right = (
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011
        )
        self.bottom_right = (
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00111,
            0b11111,
            0b11110,
            0b11000
        )
        self.bottom = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b11111,
            0b11111,
            0b11111
        )
        self.bottom_left = (
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11100,
            0b11111,
            0b01111,
            0b00011
        )
        self.left = (
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000
        )

    def draw_frame(self, lcd, time):
        lcd.create_char(0, self.top_left)
        lcd.create_char(1, self.top)
        lcd.create_char(2, self.top_right)
        lcd.create_char(3, self.right)
        lcd.create_char(4, self.bottom_right)
        lcd.create_char(5, self.bottom)
        lcd.create_char(6, self.bottom_left)
        lcd.create_char(7, self.left)

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