#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):    
    # Get the first two elements of each tuple or 0 if the tuple is smaller    
    a1, a2 = tuple_a + (0, 0)[:2 - len(tuple_a)]
    b1, b2 = tuple_b + (0, 0)[:2 - len(tuple_b)]
    # Calculate the sum of corresponding elements and return a new tuple
    return (a1 + b1, a2 + b2)
