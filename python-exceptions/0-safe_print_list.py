#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    res=""
    for i in range(x):
        try:
            res += str(my_list[i])
        except:
            break
    return res
