# Pico Producer remix by Blue_ON

a shorcut keypad using YD-RP2040/Pi Pico.\
original project by https://github.com/pjgpetecodes/pico-streamdeck

# Parts List
all parts are THT components, making easy to assemble.

| Part | Qty | note |
|------|-----|------|
| PCB | 1 | generate with kicad |
| 3mm THT LED | 12 |  |
| Cherry MX switches | 12 | compatible switches can be used | 
| 1k Ohm THT Resistor | 12 |  |
| YD-RP2040 | 1 | you can use Pi Pico instead |
| 20 pin Header pin | 2 | will come with YD-RP2040 |
| 3D Printed Case | 1 |  |
| 3D printed keycaps | 12 |  |
| 3D printed faceplate | 1 |  |

Notes: 
- you can use Pi Pico instead, but you will need external WS2812B LED.
- print 3D models with 25% infill at least.

# Instructions
- connect YD-RP2040 to computer while pressing onboard BOOT button.
- download circuitpython for YD-RP2040 [link](https://circuitpython.org/board/vcc_gnd_yd_rp2040/)
- install circuitpython to YD-RP2040 by copying uf2 file to newly appeared drive.
- install [neopixel driver](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/releases) to 'CIRCUITPY' drive
- install [hid library](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases) to 'CIRCUITPY' drive
- copy code.py to 'CIRCUITPY' drive and disconnect the board from computer.
- solder the R68 jumper on the YD-RP2040. this enables onboard RGB LED.
- solder LEDs to PCB.
- solder resistors to PCB.
- solder pin header to PCB.
- solder key switches to PCB.
- solder YD-RP2040 to PCB.
- trim the header pins.
- assemble all together.

## CircuitPython HID

You can find some more info about the CircuitPython KeyMappings here;

https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html
