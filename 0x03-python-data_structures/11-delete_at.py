#!/usr/bin/python3
def delete_at(custom_list=[], idx=0):
    if idx < 0 or idx >= len(custom_list):
        return custom_list
    else:
        return custom_list[:idx] + custom_list[idx+1:]
