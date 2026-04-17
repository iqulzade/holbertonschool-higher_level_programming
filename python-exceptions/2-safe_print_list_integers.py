#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    res = ""

    for i in range(x):

        try:
            value = "{:d}".format(my_list[i])

            res += my_list[i]

        except:
            continue
       