print("This program is not done.")


#Title: PyPorts.py
#Author: WonkeyMonkey
#
#PyPorts.py -- Listens on TCP sockets and Records The Port



backlog = 5

import sys,argparse, time
import socket, select
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

            if first < last:
                return value
                
    raise argparse.ArgumentTypeError("Invalid Range Value! Example: -r 1-65535")


def listener(portset):
    sockets = []

    try:
        for p in portset:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', p))
            s.listen(backlog)
            sockets.append(s)

        running = True
        while True:
            time.sleep(1) #No, this is not best way. Get over it.
            readable, writable, errored = select.select(sockets, [], [])
            for s in readable:
                sock, address = s.accept()
                print(address)
                sock.close()
                
    except:
        for s in sockets:
            s.close()
        

    

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

listener(list(portset))



