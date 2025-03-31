"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

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
     

