from time import sleep

class System():
    def __init__(self):
        self.top_left, self.top, self.top_right, self.right, self.bottom_right, self.bottom, self.bottom_left, self.left = (
            0b00011,
            0b01111,
            0b11111,
            0b11100,
            0b11000,
            0b11000,
            0b11000,
            0b11000
        ),(
            0b11111,
            0b11111,
            0b11111,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000
        ),(
            0b11000,
            0b11110,
            0b11111,
            0b00111,
            0b00011,
            0b00011,
            0b00011,
            0b00011
        ),(
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00011
        ),(
            0b00011,
            0b00011,
            0b00011,
            0b00011,
            0b00111,
            0b11111,
            0b11110,
            0b11000
        ),(
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b11111,
            0b11111,
            0b11111
        ),(
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11100,
            0b11111,
            0b01111,
            0b00011
        ),(
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000,
            0b11000
        )
        self.frame1, self.frame2, self.frame3 = (
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

        for _ in range(18):
            lcd.write_string(chr(1))
            sleep(time)

        lcd.write_string(chr(2))
        lcd.cursor_pos = (1, 19)

        for _ in range(2):
            lcd.write_string(chr(3))
            lcd.cursor_pos = (2, 19)
            sleep(time)

        lcd.cursor_pos = (3, 19)
        lcd.write_string(chr(4))
        sleep(time)

        col = 18
        for _ in range(18):
            lcd.cursor_pos = (3, col)
            lcd.write_string(chr(5))
            col -= 1
            sleep(time)
            
        lcd.cursor_pos = (3, 0)
        lcd.write_string(chr(6))
        sleep(time)

        row = 2
        for _ in range(2):
            lcd.cursor_pos = (row, 0)
            lcd.write_string(chr(7))
            row -= 1
            sleep(time)

    def cheers(self, lcd):
        # temporarily creating new characters for animation
        lcd.create_char(0, self.frame1)
        lcd.create_char(1, self.frame2)
        lcd.create_char(2, self.frame3)
        for i in range(3):
            self.clear(lcd)
            lcd.cursor_pos = (1, 6 + i)
            lcd.write_string(chr(i))
            lcd.cursor_pos = (1, 11 - i)
            lcd.write_string(chr(max(i-2, 2-i)))
            sleep(0.5)
        # returning old characters
        lcd.create_char(0, self.top_left)
        lcd.create_char(1, self.top)
        lcd.create_char(2, self.top_right)
        
    # welcome message, from Giovanni
    def hello(self, lcd):
        lcd.cursor_pos = (1, 7)
        lcd.write_string("Hello!")
        sleep(1)
        lcd.cursor_pos = (2, 3)
        lcd.write_string("I am Giovanni.")
        sleep(2)

    # goodbye message
    def goodbye(self, lcd):
        self.clear(lcd)
        lcd.cursor_pos = (1, 7)
        lcd.write_string("Ciao!")
        sleep(2)
        lcd.backlight_enabled = False
        lcd.clear()

    # custom clear function to clear all but frame
    def clear(self, lcd):
        for row in range(1,3):
            for col in range(1, 19):
                lcd.cursor_pos = (row, col)
                lcd.write_string(" ")