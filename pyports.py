import sys, socket, argparse
assert sys.version_info.major == 2

def checkRangeArg(value):
    if value.count('-') != 1:
        raise argparse.ArgumentTypeError("Invalid Range Value! Example: 1-65535")
    else:
        first, last = value.split("-")
        int(first)
        int(last)
    

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, nargs='*', choices=xrange(1,65535))
parser.add_argument('-r', '--range', type=checkRangeArg)
