#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):

        res = 0

        try:
            val1, val2 = my_list_1[i], my_list_2[i]
            res = val1/val2

        except TypeError:
            print("wrong type")
            

        except ZeroDivisionError:
            print("division by 0")
            

        except IndexError:
            print("out of range")
            

        res_list.append(res)

    return res_list
