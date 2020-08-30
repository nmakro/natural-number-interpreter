import sys

class Error(Exception):
    def __init__(self, *args):
        if args:
            self.error_msg = args[0]
        else:
            self.error_msg = None


class RetryNeeded(Error):
    def __init__(self):
        super().__init__(self)


class BadInputType(Error):
    pass


class BadInputFormat(Error):
    pass


class NotGreekNumber(Error):
    pass


def utils_decorator(func):
    def inner_function(*args):
        try:
            func(*args)
        except Error as e:
            sys.stdout.write(f"{e.error_msg}\n")
            raise RetryNeeded

    return inner_function


def get_user_input():
    return input("Please enter your number: ")


def is_only_numbers(user_input: str) -> bool:
    stripped_input = user_input.replace(" ", "")
    try:
        int(stripped_input)
    except ValueError:
        return False
    return True


def validate_size_per_three(user_input: str) -> bool:
    listed_input = user_input.split()
    if len(listed_input) <= 1:
        return True
    valid_size = (
        len(x) <= 3
        for x in listed_input
    )
    return all(valid_size)


def is_greek_number(user_input: str) -> bool:
    input_size = len(user_input)
    if input_size not in [10, 14]:
        return False
    numb_prefix_map = {10: ["2", "69"], 14: ["00302", "003069"]}
    return user_input.startswith(tuple(numb_prefix_map[input_size]))


def print_is_valid_number(num: str) -> str:
    if is_greek_number(num):
        return "VALID"
    return "INVALID"


def zero_trailing(num: str) -> bool:
    if num[-1] == "0":
        return True
    return False


def starts_with_zero(num: str) -> bool:
    if num[0] == "0":
        return True
    return False


def is_larger_by_factor_ten(num1: str, num2: str) -> bool:
    if starts_with_zero(num2):
        return False
    elif starts_with_zero(num1):
        condition = is_larger_by_factor_ten(num1[1:], num2)
        return condition
    else:
        return len(num1) - len(num2) > 0


@utils_decorator
def validate_input(user_input: str):
    if not is_only_numbers(user_input):
        raise BadInputType("Input must be only integers that can be separated with spaces.")

    if not validate_size_per_three(user_input):
        raise BadInputFormat("Numbers must be separated max per three.")
