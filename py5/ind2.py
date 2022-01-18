#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    x1 = float(input("Enter х1 = "))
    x2 = float(input("Enter х2 = "))
    y1 = float(input("Enter у1 = "))
    y2 = float(input("Enter у2 = "))
    r1 = float(input("Enter r1 = "))
    r2 = float(input("Enter r2 = "))

    d = float(math.sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2)))

    if (d == r1 + r2) or (d + r2 == r1) or (d + r1 == r2):
        print("1 point of intersection; d = %.2f" % d)
    elif (d >= r1 + r2) or (d + r2 < r1) or (d + r1 < r2):
        print("No intersection points; d = %.2f" % d)
    elif (x1 == x2) and (y1 == y2) and (r1 == r2):
        print("The circles match; d = %.2f" % d)
    else:
        print("2 points of intersection; d = %.2f" % d)

