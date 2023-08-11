#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
div_result = divide(a, b)

print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {diff_result}")
print(f"{a} * {b} = {prod_result}")
print(f"{a} / {b} = {div_result}")

