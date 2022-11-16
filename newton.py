#!/usr/bin/env python3
import argparse
from math import sin

from scipy.misc import derivative


def parse_args():
    parser = argparse.ArgumentParser(description='Newthon\\'s method for finding roots')

    parser.add_argument('f', type=str, help='The function whose root we are trying to find')
    parser.add_argument('--x0', default=1, type=float, help='The initial guess')
    parser.add_argument('--tolerance', default=1e-7, type=float, help='How many digits of accuracy is desired')
    parser.add_argument('--epsilon', default=1e-14, type=float, help='Do not divide by a number smaller than this')
    parser.add_argument('--max_iterations', default=50, type=int, help='Max number of iterations')
    return parser.parse_args()


if __name__ == '__main__':
    solution_found = False
    args = parse_args()
    print(args)

    x0 = args.x0

    def f(x):
        return eval(args.f)

    def fprime(x):
        return derivative(f, x)

    for i in range(args.max_iterations):
        y = f(x0)
        yprime = fprime(x0)

        # Stop if the denominator is too small
        if abs(yprime) < args.epsilon:
            break

        # Do Newton's computation
        x1 = x0 - y/yprime

        # Stop when the result is within the desired tolerance
        if abs(x1 - x0) <= args.tolerance:
            solution_found = True
            break
        # Update x0 to start the process again
        x0 = x1

    if solution_found:
        # x1 is a solution within tolerance and maximum number of iterations
        print("Solution: ", x1)
        exit(0)
    else:
        # Newton's method did not converge
        print("Did not converge")
        exit(1)