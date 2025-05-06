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
    """
    Convert a range to another range
    Args:
        value (int): Value to convert
        in_min (int): Range 'in' minimum, default to 0
        in_max (int): Range 'in' maximum, default to 1024
        out_min (int): Range 'out' minimum, default to 0
        out_max (int): Range 'out' maximum, default to 9
    """
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min))


def decode_data(data):
    """
    Decode data to list
    Args:
        data (bytes): Data to decode
    Returns:
        (list[bool, bool, int, int): Binary data Convert
    """
    on_state = bool(data[0])
    reverse_state = bool(data[1])
    direction = int.from_bytes(data[2:4], "little")
    speed = data[4]

    return [on_state, reverse_state, direction, speed]


class Main:
    def __init__(self):
        self.radio_status = True
        self.paused = False

        self.old_data = (None, None, 0, None)

        self._switch_radio(True)

    def _switch_radio(self, status):
        """
        Turn radio on / off
        Args:
            status (bool): Status to set the radio to
        """
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

        # Run only if the radio is on
        if self.radio_status:
            data = radio.receive_bytes()

            if data is not None:
                # *** RUN ALL OF YOUR LOGIC HERE ***
                data_decoded = decode_data(data)

                if data_decoded is not None:
                    display.set_pixel(0, 0, 9)

                    print(
                        "\rMOTOR: {:<10} | BACKWARD: {:<10} | DIRECTION: {:<10} | SPEED: {:<10}".format(
                            data_decoded[0],
                            data_decoded[1],
                            data_decoded[2],
                            data_decoded[3],
                        ),
                        end="",  # Only use 'end=""' to overwrite the previous line
                    )

                # *** IF YOU WANT TO ACCESS CURRENT DATA, USE data_decoded !!! ***
                # *** YOUR CODE HERE ***

            else:
                display.set_pixel(0, 0, 1)


main = Main()
while True:
    main.mainloop()
