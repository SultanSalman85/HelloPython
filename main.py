import binary_utilities.bin_utility as bu
import binary_utilities.bin_sum as bs
import binary_utilities.bin_sub as bsb
import binary_utilities.bin_mul as bm
import binary_utilities.bin_div as bd
import json
import os

# Get Input
os.system('clear')
(number0, binary0) = bu.get_user_number_input("Please input the 1st number:")
(number1, binary1) = bu.get_user_number_input("Please input the 2nd number:")

# Arithmetic SUM
print("Arithmetic SUM: {} + {}".format(number0, number1))
print("Normal result is {}".format(number0 + number1))
print("Binary result is {}".format(bs.sum_two_number(number0, number1)))
print()

# Arithmetic SUB
print("Arithmetic SUB: {} - {}".format(number0, number1))
print("Normal result is {}".format(number0 - number1))
print("Binary result is {}".format(bsb.subtract_two_number(number0, number1)))  # Implemented test
print()

# Arithmetic MUL
print("Arithmetic MUL: {} * {}".format(number0, number1))
print("Normal result is {}".format(number0 * number1))
print("Binary result is {}".format(bm.multiple_two_number(number0, number1)))  # Implemented test
print()

# Arithmetic DIV
print("Arithmetic DIV: {} / {}".format(number0, number1))
print("Normal result is {}".format(number0 / number1))
print("Binary result is {}".format(bd.divide_two_number(number0,number1)))  # Implemented test
print()
