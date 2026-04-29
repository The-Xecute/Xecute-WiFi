#!/usr/bin/env python3

#  Xecute-WiFi (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 The-Xecute
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  Telegram: https://t.me/iXecute
#  Telegram: https://t.me/Xecute_Channel

import base64, zlib, marshal

enc_data = "87AEAAB4nH1W3W7iRhS+5ylOkwvbLdANF1WVlJUoCxu0WYKAKI1ShAb7GKZrZqyZcRJUVerT9MH6JD0ztjEGUl/Zc875zv83vgT4DcPMYOuRDzn4j5MZpCjQKGa4FGBQGy7WkBmecLMLgGtgEEv1DWQMZoNgpEzglZsN4BtZQYzMZAp14xKgL9Od4uuNAb8fQOdD5yeYb7CVe2xcWpX5hhBTJdeKbS14rBBBy9i8MoU3sJMZhEyAwohro/iKDIEbYCL6USoLsJURj3f2LBMRqjwmVFtdBvh5/ACfKSXFEphkq4SHcMdDFBqtOSPv9lBvMILVzlkMbQyzIgYYSgJ21bgBpDzJxwsqbavTsQiFmwKzCVKBz4yNXIFMrV1A4e4gYaYybZ/PvkoyAi4c7kamlNCGECnFV54ksELINMZZ0rQQpAyPo/nt/cMceuMneOxNp73x/OnGNUWSFF8wh+LbNOGETGkpJsyOQrcIXwfT/i2Z9H4d3Y3mTzaB4Wg+HsxmMLyfQg8mvel81H+4601h8jCd3M8GbYAZ2rBcDd+vsJ0U6hBVMULDeKLbjQZFIZUBna0o8RC1bjRiJbdgdqmdtEL8IKhKjUaYMK3hEzPsugH0XFxczAzhRUAtYbYOkfOR8jeOr6mGUG63NBxtUmw4iwhjWC654Ga59DUmcZAj2cd+tidfBtAFzzs+nZ45HSxve7Pbq3clnTOS3sP89svg6azN+H7cL7zvg12j6SXJcaiUz31mUmonoxHYp6vQjlUEL0xxtkpQV4nbRyHtogB/nyiVpspv/1EGsj8oYt7jlM+BRV6Io4NOUOWhMjGxYT6m2vlvgt7I12XRoGtYWeLowpAldmtonJMlTeUa65IAWh/zYXim1Wg62aJWlmkmtBvvfVFsUMwY3KaGJDInptA4JUdwtFr5yNGBdFWtly1VXBjfe/5+AYQu7FhOCvB///7HC/aKRTIUrCvCknrnFPvbyK8yCipkHterUKvwJRGmIILIIy2x7bISvwlKhIGlB7GuWRXBgtf+Q3LhF2bBgVOjdnVHhc4yz91Gv1/GNrWtxGie9F+biGy6B+qT0WTQtOeo1OH5bP6JGOkUAUVIhC3WXS8zcetnr6ZQFRbfQkzp2jhA7NPgYzTJvwZKSZqGIU9wLI2jaHcUWEJH+1bPuFiEvFax9/zdYt9R2FiTN27XiDg9N4bfBfzpXv/yguPBqJevnRel3uQjldw9ZY7Q7cKHemwJF6ipCWdh25o42zgVP6iZWdqz5/aicPLrk2JTIDTFPyy8Uidwu+F7xRZU56e2Ll0Sd51CHobvXXvBc+tq0bZzmPoHOR+5dZbEa7/YJdx99M7jVz4uPO/iPFjZOS5OaM0RxAHLH25fzjj/yyp06RtLKnU6yS8y+u+hbbMa5Cyl3xkU7j/ocDFtA2q8Y3+FjojEisKtJYhnr9TzFifyNlEUish/rpXAa7XSb+g19/dU81SsKvH0RIwtmu3NValSkPY7ap26WudEjWVm8w13pVpxR5xBE1KEWKG5u2WvtagvykGH6qxWVoalqa0MAVO9CTY4GYNStZqEMEGmztygU+qjObos6jdnqZzTefnbEDT+A/a+Qo0="

# Decodificación
decoded = base64.b64decode(enc_data)
unmarshaled = marshal.loads(decoded)
decompressed = zlib.decompress(unmarshaled)
exec(decompressed.decode())
