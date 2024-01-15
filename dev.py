import board
import digitalio
import time

paddle_manual = digitalio.DigitalInOut(board.GP6)
paddle_scan = digitalio.DigitalInOut(board.GP7)

bt0 = digitalio.DigitalInOut(board.GP2)
bt1 = digitalio.DigitalInOut(board.GP3)
bt2 = digitalio.DigitalInOut(board.GP4)
bt3 = digitalio.DigitalInOut(board.GP5)
bt4 = digitalio.DigitalInOut(board.GP19)
bt5 = digitalio.DigitalInOut(board.GP18)
bt6 = digitalio.DigitalInOut(board.GP17)
bt7 = digitalio.DigitalInOut(board.GP16)

led0 = digitalio.DigitalInOut(board.GP8)
led1 = digitalio.DigitalInOut(board.GP9)
led2 = digitalio.DigitalInOut(board.GP10)
led3 = digitalio.DigitalInOut(board.GP11)
led4 = digitalio.DigitalInOut(board.GP12)
led5 = digitalio.DigitalInOut(board.GP13)
led6 = digitalio.DigitalInOut(board.GP14)
led7 = digitalio.DigitalInOut(board.GP15)

buttons = [bt7, bt6, bt5, bt4, bt3, bt2, bt1, bt0]
leds = [led7, led6, led5, led4, led3, led2, led1, led0]

for b in buttons+[paddle_manual, paddle_scan]:
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP 

for d in leds:
    d.direction = digitalio.Direction.OUTPUT

blink_on = True
scan_pos = 0

while True:
    if not paddle_scan.value:
        # Scan ... run the LEDs from right to left
        for i in range(8):            
            leds[i].value = (i == scan_pos)
        scan_pos = (scan_pos + 1) % 8
        time.sleep(0.1)
    elif not paddle_manual.value:
        # Manual ... flash all the LEDs on and off
        for i in range(8):
            leds[i].value = blink_on
        blink_on = not blink_on
        time.sleep(0.5)
    else:
        # Center ... LEDs follow switches
        blink_on = True
        scan_pos = 0
        for i in range(8):
            leds[i].value = buttons[i].value
        time.sleep(0.1)
