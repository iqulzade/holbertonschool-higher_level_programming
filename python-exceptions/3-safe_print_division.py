#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        res = a / b
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(res))
        return res
