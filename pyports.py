#!/usr/bin/env python2

print("This program is not done.")
exit(0)

#Title: PyPorts.py
#Author: WonkeyMonkey
#
#PyPorts.py -- Listens on TCP sockets and Records


import sys, socket, argparse
assert sys.version_info.major == 2

#Sets are faster than list for checking if a value in inside of an object
portset = set()
blacklistedips = set()
whitelistedips = set()


def checkRangeArg(value):
    if value.count('-') == 1:
        first, last = value.split("-")
        first = int(first)
        last = int(last)

        if ((first > 0) and (first <= 65535)) and ((last > 0) and (last <65535)):

            if first != last:
                return value

    raise argparse.ArgumentTypeError("Invalid Range Value! Example: -r 1-65535")


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', nargs='*', type=int)
parser.add_argument('-r', '--range', nargs='*', type=checkRangeArg)

args = parser.parse_args()

if args.port:
    for p in args.port:
        portset.add(int(p))

if args.range:
    for r in args.range:
        first, last = r.split("-")
        first = int(first)
        last = int(last)
        for p in range(first, last+1):
            portset.add(int(p))




