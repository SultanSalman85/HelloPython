import binary_utilities.bin_utility as bu


def half_adder(a: bool, b: bool) -> (bool, bool):
    """
    Half Adder, see: https://en.wikipedia.org/wiki/Adder_(electronics)#Half_adder

    [Parameters]\n
    a (bool): first bit.
    b (bool): second bit.

    [Returns]\n
    Tuple(bool, bool): SUM and CARRY-OVER
    """  # noqa
    return (a ^ b, a & b)


def full_adder(c: bool, a: bool, b: bool) -> (bool, bool):
    """
    Full Adder, see: https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder

    [Parameters]\n
    c (bool): carry-over bit.
    a (bool): first bit.
    b (bool): second bit.

    [Returns]\n
    Tuple(bool, bool): SUM and CARRY-OVER
    """  # noqa
    (first_sum, first_carry_over) = half_adder(a, b)
    (second_sum, second_carry_over) = half_adder(c, first_sum)
    return (second_sum, second_carry_over | first_carry_over)


def sum_two_number(first_number: int, second_number: int) -> int:
    """
    Just a summary between 2 integer, but executed in binary fashion.

    [Parameters]\n
    first (int): first number.
    second (int): second number.

    [Returns]\n
    int: sum result.
    """
    # Get the binary representation of the integers in boolean arrays
    first_binary = bu.get_boolean_array_from(first_number)
    second_binary = bu.get_boolean_array_from(second_number)
    result_binary = [False] * bu.MAX_BIT_LENGTH

    # Do binary adder
    for i in range(0, bu.MAX_BIT_LENGTH - 1):
        if i == 0:
            (sum, co) = half_adder(first_binary[i], second_binary[i])
        else:
            (sum, co) = full_adder(co, first_binary[i], second_binary[i])
        result_binary[i] = sum
    return bu.get_integer_from(result_binary)
