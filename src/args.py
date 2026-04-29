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

enc_data = "84MFAAB4nJ1X227bRhB911dMExSS0JBy3KBoFehBUezESOIIklw3QAFjSQ7FhalddncpWn/fmV3qEqcNzOjBgkecM2fuw+c/jWprRolUI1RbqHau0OrXXu85wF+Y1g6jW3kpYXA7X0KFCp0RTmoFDq2Tag21k6V0uyFICwJybe5B5+AKBKd1CY10BeADaUGOwtUGLUPPdLUzcl04GMyGcH52/husCoyCxd5zfmRVEGJl9NqIDYPnBhGszl0jDL6Gna4hFQoMZtI6IxNSBOlAqGykDQNsdCbzHctqlaEJnNBs7J7gu+sbeEcuGVHCvE5KmcJHmaKyyOqCrLPQFphBsvMal8xh2XKAS03APhqvAclPsrFFYzk654zQmmkxX4A2MBCOmRvQFesNie4OSuGOqvF/e390MgOpPG6hK3KoIERysZFlCQlCbTGvyxcMQQ/D7dXq/eebFUyvv8DtdLGYXq++vPZJ0fQrbjFAyU1VSkImt4xQbkfUGeHTxWL2nlSmb64+Xq2+sAOXV6vri+USLj8vYArz6WJ1Nbv5OF3A/GYx/7y8iAGWyLR8DP8/wlwplCGKYoZOyNLGvR6x0IYyaNaVMJSE9n9te70Mc/DCqVnbwXDcA/o8e/ZszjLWqDeoHEVMWEt+OO3d2ggKVahosKmRlYtJp+eVPZqBycFcPG1RPKYZ+Kf4k2HQpeRM+l/1RNqW7omw/+Kgh5Us9XrSv3gQFF4cw88DTujQQiShKYU6gyiBs7PxH2fjV7Px7OV4Ohufv4ToQ99jDE+JxiLL7vZ+Hrn1I7JIfyOpqIZykeIJAbercEJlc5QY/KeW1DGTlanxKC6wrCb9a7HBfc0e4DiUVFN7Rk8glARCibUy+y6ZYPXNcnn19jAyCBAdTOcd7FXBXiXVE6zdWF+bYCtMZc4lT3rUlSaRNKLMDrjLaKpRcb4a/U5dt6beokeGMVxwSGjEJZS5+6CG8TqGfn/oi1nAdU09OKcfhHMive/gw4e9Dw8So6y27sQVkYbKs4665c5R4vqPvVrUiuySLrwl3e7mL0/Nky9fVVEX+01lw8SPAkw75mCQGGqQIMo5SjRl1jjsQPGvQNEWuml5ppusG8tp2YgdD1Uq7iPdVG82tDM6UHnTFvjBpe7B0qqUCuEkKp1zFlVJ2qattkVEw95pFaVaKUx/oHz8eicgCEDQApFqB05ZIJRhKXaPmzEvtXCPLS+p2bkdvQatL9cgbaQqtBBuKmc7WG+C9cZI1zElt6wCKQ1GgpSitPsFksuSapiWR52maLuQsW29im1HLkvS8Lanc2ZBB1fDNxXVqFjT/PkhMpHkUR5lulHdyLwljQOF405oivZuCHK6zaTyd1IXTtu6VBGdV+67Y5sWv6hLN9E2roQr4kwaRXtqcHfHubm7G8Iv0B/F8YjhGpvG7sF94wZP/ZQmo96EjPoRxQp0mCQll9+WrhILns3TXShDjkutq+4NxzUOXvXpBtuGT0sUppvFGauEzUdljjyB+PqjhdfIKJckFV0a3QQihiEsRl67WwSCJu1Zvsxp+7dFZvfHLafiVB7Djb9sfQNsBK0Quogrmhqd+mDj7qOG9n7HxUGPbOlGh0/0riFWeA+3MqL779gQmZHbtjnphHF1xa8hVFZir0lXBEf8gb77B/TAasDHg4dSdCUHZJGJigTWH+bIboSz/0BgqWeWbpLHWKvaUGrz/EAwpHxnaZiCRcdvbJbmbM6Hd2350nH0ohF3iWHm2tmWaeUip+u0iPbQXaeL+rtPC4AhwshTmdEya9kf+D4KK0fxW9e5x/1cKsSW/Qo9HbWHXkpTytbYpVi2wUvKa6JtxyH+Z1ACesmq6q9GClmy9NLR2vZfbJ3eafzPBh2nkCW9fwGj8KuC"

# Decodificación
decoded = base64.b64decode(enc_data)
unmarshaled = marshal.loads(decoded)
decompressed = zlib.decompress(unmarshaled)
exec(decompressed.decode())
