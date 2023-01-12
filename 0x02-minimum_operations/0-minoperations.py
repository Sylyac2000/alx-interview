#!/usr/bin/python3
""" this module is about calculation of the fewest number of operations needed
to result in exactly n H characters in the file."""


def minOperations(n):
    """ minimum operation processing"""
    nbre_operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            nbre_operations += min_operations
            n /= min_operations
        min_operations += 1
    return nbre_operations
