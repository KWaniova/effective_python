#!/usr/bin/env python3
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Process something')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', ##opcjonalne
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
    parser.add_argument('f', type=str, help="something")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args)
    exit(0)