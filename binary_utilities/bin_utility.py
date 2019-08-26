from typing import List


MAX_BIT_LENGTH = 32


def get_user_number_input(message: str) -> (int, bin):
    """
    Get user input as number (integer).

    [Parameters]\n
    message (str): Message for user to input the number.

    [Returns]\n
    Tuple(int, bin): inputted number and its binary representation.
    """
    print(message)
    return_int = None
    return_bin = None
    while (not isinstance(return_int, int) or
           len(return_bin) > MAX_BIT_LENGTH):
        user_input = input("=> ")
        try:
            return_int = int(user_input)
            return_bin = bin(return_int)
        except ValueError:
            return_int = None
            return_bin = None
    print("Got {} ({})\n".format(return_int, return_bin))
    return (return_int, return_bin)


def get_boolean_array_from(number: int) -> List[bool]:
    """
    Get boolean array of a number with a fixed length bit size according to
    MAX_BIT_LENGTH constants.

    [Parameters]\n
    number (int): the number.

    [Returns]\n
    List[bool]: boolean array representation.
    """
    return_value = [False] * MAX_BIT_LENGTH
    last_bit_position = len(bin(number)) - 1
    for i in range(0, last_bit_position):
        return_value[i] = (number & (1 << i)) != 0
    return return_value


def get_integer_from(bool_array: List[bool]) -> int:
    """
    Get integer from boolean array.

    [Parameters]\n
    bool_array (List[bool]): bool[MAX_BIT_LENGTH]

    [Returns]\n
    int: integer representation.
    """
    return_value = 0
    for i in range(0, MAX_BIT_LENGTH - 1):
        return_value |= (1 << i) if bool_array[i] else 0
    return return_value
