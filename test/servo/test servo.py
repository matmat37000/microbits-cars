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


from microbit import *

# def setServoSpeed(pin, direction, speed):
#   pin.set_analog_period(20)
#   if (speed >= 0 and speed <= 100):
#     if direction is 1 or direction is -1:
#       #clockwise: 1.5 ms to 1 ms | anticlockwise: 1.5ms to 2 ms (0 to 100%)
#       speed_ms = speed * direction * 0.5 / 100 + 1.5
#       pin.write_analog(1023 * speed_ms / 20)
#     else:
#       raise ValueError("continuous servomotor has no direction: '" + str(direction) + "'")
#   else:
#     raise ValueError("continuous servomotor speed is out of range: '" + str(speed) + "'")
# 
# setServoSpeed(pin2, 1, 100)

def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.write_analog(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")

# setServoAngle(pin2, 180)

while True:
    setServoAngle(pin2, 180)
#     pin2.write_analog(1023)