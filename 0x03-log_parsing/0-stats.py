#!/usr/bin/python3
""" using other script as input """
import sys

import re


def print_log_stats(size_list, list_status_tuple):
    """ print size and count status"""
    size = 0
    for asize in size_list:
        try:
            size += asize
        except ValueError:
            pass

    print('File size: {}'.format(size))
    # print status
    for atuple in list_status_tuple:
        print('{}: {}'.format(atuple[0], atuple[1]))


numbers = []
cpt_line = 0
tabloDeList = []
list_of_size = []
list_status_tuple = []
list_of_status = []
tabloDeCode = [200, 301, 400, 401, 403, 404, 405, 500]
try:

    for line in sys.stdin:

        # print('from stat =>',line)
        aline = line.replace('[', '')
        aline = aline.replace(']', '')
        alist = re.split("[\\s\n-]+", aline)

        # remove last elt
        alist = alist[:-1]
        # print('split', alist)

        # add to tablo de liste
        tabloDeList.append(alist)

        # compute values

        # print('tablo de list', tabloDeList)
        try:
            list_of_size = [int(sublist[-1]) for sublist in tabloDeList]
        except (ValueError, IndexError):
            pass
        try:
            list_of_status = [sublist[-2] for sublist in tabloDeList]
        except (IndexError):
            pass
        # print('\n \n size =>', list_of_size)
        # print('\n \n list_of_status =>', list_of_status)

        # check all status is integer
        list_of_status = [int(status) for status in list_of_status
                          if status.isdigit()]
        # print('\n \n =====real list_of_status =>', list_of_status)

        filtered_list_of_status = list(filter(lambda x: x in tabloDeCode,
                                       list_of_status))

        # print('\n \n ')
        # sorted filtered_list_of_status
        list_of_status_sorted = sorted(filtered_list_of_status)

        # print('\n \n ')

        list_status_tuple = [(elt, list_of_status_sorted.count(elt))
                             for elt in set(list_of_status_sorted)]
        list_status_tuple = sorted(list_status_tuple)

        cpt_line += 1
        if cpt_line == 10:
            # 10 lines printed
            # print('number of line =>',cpt_line)
            cpt_line = 0
            print_log_stats(list_of_size, list_status_tuple)

            tabloDeList = []

except KeyboardInterrupt:
    print_log_stats(list_of_size, list_status_tuple)
    raise
