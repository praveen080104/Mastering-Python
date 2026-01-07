'''round(): Rounds a number to the specified number of decimal places. 
By default this function rounds to the nearest integer, and returns 
a whole number with no decimal places:'''

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

#abs(): returns the absolute value of a number,

num = -15

absolute_value = abs(num)
print(absolute_value) # 15

#pow(): raises a number to the power of another or performs modular exponentiation.

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3