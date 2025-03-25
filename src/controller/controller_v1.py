# Code by Mathieu BORDIER-AUPY

from microbit import *
import radio
import time

# Clear screen at startup
display.clear()

radio_status = True
buffer = ''

def _switch_radio(status):
    if status == True:
        radio.on()
        display.show(Image.YES)
        radio_status = True
    else:
        radio.off()
        display.show(Image.NO)
        radio_status = False
    sleep(500)
    display.clear()
    
_switch_radio(True)

while True: 
    # Turn on or off the radio module
    if button_a.was_pressed():
        radio_status = not radio_status
        _switch_radio(radio_status)
     
    if radio_status:
        if button_b.was_pressed():
            radio.send_bytes(bin(5000))
        
        pin_v = pin0.read_analog()
        if pin_v is not None:
            radio.send_bytes(bin(pin_v))
            #sleep(500)
            #print(pin_v.to_bytes(2, 'big'))
     

