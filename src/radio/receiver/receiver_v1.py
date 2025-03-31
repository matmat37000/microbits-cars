"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

# pyright: reportUnknownMemberType=false, reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownArgumentType=false

# Code by Mathieu BORDIER-AUPY

from microbit import *
import radio

# Clear screen at startup
display.clear()

# Convert a range to another range
def convert_range(value, in_min=0, in_max=1024, out_min=0, out_max=9):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min))

# Set the whole led panel to a light level
def set_display_to(light_level):
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, light_level)

class Main:
    def __init__(self):
        self.radio_status = True
        self.paused = False
        
        self._switch_radio(True)

    def _switch_radio(self, status):
        if status == True:
            radio.on()
            display.show(Image.YES)
            self.radio_status = True
        else:
            radio.off()
            display.show(Image.NO)
            self.radio_status = False
        sleep(500)
        display.clear()
        
    # Pause the script
    def pause(self):
        self.paused = not self.paused
        if self.paused:
            display.show(Image.NO)
        else:
            display.show(Image.YES)
        sleep(500)
        display.clear()
    
    def mainloop(self):
        # Turn on or off the radio module
        if button_a.was_pressed():
            radio_status = not self.radio_status
            self._switch_radio(radio_status)
            
        if self.radio_status:
            data = radio.receive_bytes() 
            
            if data is not None:
                data_int = int(data, 2)
                
                if data_int == 5000:
                    self.pause()
                    #sleep(1000)
                elif not self.paused:
                    #display.show(str(data_int))
                    set_display_to(convert_range(data_int))
                        
main = Main()
while True:
    main.mainloop()


