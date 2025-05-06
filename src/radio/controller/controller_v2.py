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

# pyright: reportUnknownMemberType=false, reportUnknownParameterType=false, reportMissingParameterType=false

# Code by Mathieu BORDIER-AUPY

from microbit import *
import radio

# Clear screen at startup
display.clear()

global radio_status
radio_status = True
data = [0, 0, 0, 0]

# Convert a range to another range
def convert_range(value, in_min=0, in_max=1024, out_min=0, out_max=255):
    """
    Convert a range to another range
    Args:
        value (int): Value to convert
        in_min (int): Range 'in' minimum, default to 0
        in_max (int): Range 'in' maximum, default to 1024
        out_min (int): Range 'out' minimum, default to 0
        out_max (int): Range 'out' maximum, default to 255
    """
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min))

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


def encode_data(data):
    """
    Encode data to bytes
    Args:
        data (list[bool, bool, int, int]): Data to encode
    Returns:
        (bytes): Binary data to send
    """
    on_state = int(data[0]).to_bytes(1, "little")
    reverse_state = int(data[1]).to_bytes(1, "little")
    direction = data[2].to_bytes(2, "little")
    speed = data[3].to_bytes(1, "little")

    return b"".join([on_state, reverse_state, direction, speed])


while True:
    # # Turn on or off the radio module
    # if button_a.was_pressed():
    #     radio_status = not radio_status
    #     _switch_radio(radio_status)

    if radio_status:
        data = [False, False, 0, 255]

        # Enable motor
        if button_a.is_pressed():
            data[0] = True

        # Enable backward mode
        if button_b.is_pressed():
            data[1] = True

        pin_v = pin0.read_analog()
        if pin_v is not None:
            data[2] = pin_v  # Set the direction
            data_to_send = encode_data(data)

            radio.send_bytes(data_to_send)
