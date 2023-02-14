#!/usr/bin/python3
"""Module to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """ rotate 90"""
    taille = len(matrix)
    sortie = get_generated_list(matrix)

    for alist in matrix:
        rev = reverse_list(alist)
        i = 0
        for elt in alist:
            sortie[i].append(elt)
            i += 1

    matrix.clear()

    for aliste in sortie:
        # print(aliste)
        rev = reverse_list(aliste)
        matrix.append(rev)


def reverse_list(lst):
    """reverse a list"""
    return lst[::-1]


def get_generated_list(listo):
    """generate aliste with same size
        Return: a list
    """
    taille = len(listo)
    sortie = []

    for i in range(taille):
        sortie.append(list())
    return sortie
