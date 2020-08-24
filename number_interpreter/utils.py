class BadInputType(Exception):
    pass


class BadInputFormat(Exception):
    pass


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


def validate_input(user_input):
    if not is_only_numbers(user_input):
        print("Input must be only integers and/or spaces.")
        raise BadInputType

    if not validate_size_per_three(user_input):
        print("Numbers must be separated max per three.")
        raise BadInputFormat
