#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for item in my_list:
            try:
                print("{:d}".format(item), end="")
                printed_count += 1
                x -= 1
                if x == 0:
                    break
            except:
                pass
    except:
        pass
    finally:
        print()
        return printed_count
