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

enc_data = "81YEAAB4nK1WUW/iOBB+z6+Ytg8JEoRVT1qdWvHAsbBF14UogLpVr6pMMml8DXZkO6VcxX+/cRICqba6l8sLiT3zzcz3jcdcnPULrfprLvooXiHfmVSK3xznAuAnRoXB3h2fcPDuggXkKNAoZrgUYFAbLp6hMDzjZtcBroFBItULyARMimCkzGDLTQr4Rl6QIDOFQm2hRzLfKf6cGvBGHbj8cvkVlin2qojOhTVZpoSYK/ms2MaCJwoRtEzMlim8hp0sIGICFMZcG8XX5AjcABNxXyoLsJExT3Z2rRAxqionVBt9SPD7bAXfqSTFMgiKdcYjuOURCo3WnVF0u6hTjGG9Kz0mNodFnQNMJAGXbFwDUp0U4xWVtuxcWoQ6TI3ZBanAY8ZmrkDm1q9D6e4gY+bo6v+6+mORMXBR4qYyp4JSQqQStzzLYI1QaEyKrGshyBjupsub+WoJw9k93A3DcDhb3l+XokjaxVesoPgmzzghU1mKCbOj1C3Cj3E4uiGX4R/T2+ny3hYwmS5n48UCJvMQhhAMw+V0tLodhhCswmC+GPsAC7RplRx+zrDtFFKIWIzRMJ5p33EoC6kM6J0+vMrmLWcmzfi6sSnWRE6EWjvOajEOn27mP8YwACLJq039gH79VG7Q63ScBSU9nc8WT9+mIdkl7nvjtu/7J53e1wRKOui+6wTTn9MxNf5/O+X8jeM2t07hOJiHy8qncpLaf0YTbWOvs+8rtAVYQyfGhKQdilhJTntXDtBzfn4+SjF6AW67p2qCvzEytglIG6DmYpWHT6ZO6aOQDpaANR04L2WaGWKBWOyCS3Fra5bzjPTOXCKjipywCEcm87ig9rMfV5a+LrDItmb5ccwpKOzRgsYWity2Qyy34phHJDcbCkdVP7g8dyl+xsWL/dVo6Ie4aAD21XcVbO8+VghG7aqQJ3BP1Ko5hR+cqO6rQnj1frdxsA+KiM69eB64hUl6v1MUbWJCGJw4B9Ng3PYiG1Tq1Gax/EYHpzHqlG/4FmFOM+vEbsSyDOOg+horJYnBCVE9k6acD+VSx04TtG/H6nJFXICXuA9njzAiboU0VLIwisbmkedygPIcLJNX8JeA9xJn73ZanNckPdkpkedoNWjv+BUNfmng1c681YC2xSYs03hM0jbKk0r+pOmyEutMRi+HPj08KnmhzadT6aslK3tR+djXLU/4QeXD01K7kaItchu/C5E9HIOlKrDT1v1/lKYlUa3QhIYU0Wok1EUdNeo20nFRUOv9SqaabTec9Epy7BD/RLp2HlUO7kPvEWpfK1OZgb1+y+l9TKTOjXbcNj0fRWxrWM6PpiU+NE61S6cK4WwAXz50cE3P+yfFNATUM+pT7GooRRkytYjomhWnA9GuNvc3F3Sb6NLmOHpoxtLEM7jx3BLDradczNEz9P/j4zgrDx8dulIlO1GpgcprlE6bkKL3DypZLdnkjnEoiG+XD2Vb7D3pTfH+BUgF9tk="

# Decodificación
decoded = base64.b64decode(enc_data)
unmarshaled = marshal.loads(decoded)
decompressed = zlib.decompress(unmarshaled)
exec(decompressed.decode())
