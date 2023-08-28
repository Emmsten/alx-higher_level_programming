#!/usr/bin/python3

mport sys

def safe_print_integer_err(value):
        try:
                    print("{:d}".format(value))
                            return True
                            except:
                                        print("Exception: " + str(sys.exc_info()[1]), file=sys.stderr)
                                                return False
