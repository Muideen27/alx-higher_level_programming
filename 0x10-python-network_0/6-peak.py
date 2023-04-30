#!/usr/bin/python3
'''
Function that finds the peak in a list of unsorted integers
'''


def find_peak(listint):
    ''' Function that returns peak value in a list '''
    if listint:
        x = listint[0]
        for i in listint:
            if i > x:
                x = i
        return x
    else:
        return None
