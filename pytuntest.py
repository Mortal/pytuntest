#!/usr/bin/env python3
import argparse
from pytun import TunTapDevice


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-addr', default='10.8.0.1')
    parser.add_argument('-d', '--dest-addr', default='10.8.0.2')
    parser.add_argument('-m', '--netmask', default='255.255.255.0')
    parser.add_argument('-l', '--mtu', default=1500, type=int)
    args = parser.parse_args()

    tun = TunTapDevice()
    try:
        tun.addr = args.source_addr
        tun.dstaddr = args.dest_addr
        tun.netmask = args.netmask
        tun.mtu = args.mtu
        while True:
            buf = tun.read(tun.mtu)
            print(buf)
            tun.write(buf)
    finally:
        tun.close()


if __name__ == '__main__':
    main()
