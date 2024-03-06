# Blue_ON Mar 2024
# MIT
#
# Pete Gallagher 11th February 2021
# MIT
#
# 2022 Dan Halbert for Adafruit Industries
# MIT

import time
import digitalio
import board
import keypad
import neopixel
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

KEY_PINS = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
)

LED_PINS = [
    board.GP13,
    board.GP14,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28,
]

KEYCODES = (
    Keycode.F13,
    Keycode.F14,
    Keycode.F15,
    Keycode.F16,
    Keycode.F17,
    Keycode.F18,
    Keycode.F19,
    Keycode.F20,
    Keycode.F21,
    Keycode.F22,
    Keycode.F23,
    Keycode.F24,
)

ON_COLOR = (0, 0, 255)
OFF_COLOR = (0, 128, 0)

led_pin_array = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(12):
    led_pin = digitalio.DigitalInOut(LED_PINS[i])
    led_pin.direction = digitalio.Direction.OUTPUT
    led_pin_array[i] = led_pin

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
neopixels = neopixel.NeoPixel(board.GP23, 1, brightness=1)
neopixels.fill(OFF_COLOR)
kbd = Keyboard(usb_hid.devices)


while True:
    event = keys.events.get()
    if event:
        key_number = event.key_number
        # A key transition occurred.
        if event.pressed:
            kbd.press(KEYCODES[key_number])
            neopixels[0] = ON_COLOR
            
            for i in range(12):
                led_pin_array[i].value=False
                
            led_pin_array[key_number].value=True

        if event.released:
            kbd.release(KEYCODES[key_number])
            neopixels[0] = OFF_COLOR
    # debounce for 1ms
    time.sleep(0.001)