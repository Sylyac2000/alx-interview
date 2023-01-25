#!/usr/bin/python3
"""a method that determines if a given data set represents
a valid UTF-8 encoding
"""


def check(num):
    mask = 1 << (8 - 1)  # 10000000
    i = 0
    while num & mask:  # 11000110 & 100000
        mask >>= 1
        i += 1
    return i


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True
