# Code by Mathieu BORDIER-AUPY

from microbit import *
import radio
import time

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


