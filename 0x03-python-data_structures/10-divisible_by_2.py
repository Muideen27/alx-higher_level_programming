#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find even"""
    even = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            even.append(True)
        else:
            even.append(False)

    return (even)
