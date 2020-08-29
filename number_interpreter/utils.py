from itertools import islice
from math import pow


class Error(Exception):
    def __init__(self, *args):
        if args:
            self.error_msg = args[0]
        else:
            self.error_msg = None


class BadInputType(Error):
    pass


class BadInputFormat(Error):
    pass


class NotGreekNumber(Error):
    pass


prefix = None
is_greek_number = False


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


def validate_greek_number(user_input) -> bool:
    input_size = len(user_input)
    if input_size not in [10, 14]:
        return False
    numb_prefix_map = {10: ["2", "69"], 14: ["00302", "003069"]}
    global is_greek_number
    is_greek_number = True
    return user_input.startswith(tuple(numb_prefix_map[input_size]))


def analyze_ambiguities(user_input):
    input_list = user_input.split()
    for i in input_list[1:]:
        if len(i) == 2:
            possible_nums = [(int(i[0]) * 10, int(i[1])), (int(i),)]
            print(possible_nums)
        if len(i) == 3:
            possible_nums = [((int(i[0]) * 100, int("".join(i[1:]))), ((int(i[0]) * 100) + int(i[1]) * 10, int(i[2]))), (int(i),)]
            print(possible_nums)


def zero_trailing(num: str) -> bool:
    if num[-1] == "0":
        return True
    return False


def is_larger_by_factor_ten(num1: str, num2: str) -> bool:
    return len(num1) - len(num2) > 0


def validate_input(user_input):
    if not is_only_numbers(user_input):
        raise BadInputType("Input must be only integers that can be separated with spaces.")

    if not validate_size_per_three(user_input):
        raise BadInputFormat("Numbers must be separated max per three.")

    if not validate_greek_number(user_input):
        print("number: INVALID")
    else:
        print("number: VALID")


class Indexer:
    def __init__(self, num_list: list):
        self.num_list = num_list
        self.ambiguities_dict = {}

    def calculate_ambiguities(self, num: str):
        ambiguities = []
        if len(num) == 2:
            if num[0] == "0":
                pass
            elif num[-1] == "0":
                ambiguities = [num[0]]
            else:
                ambiguities = [str(int(num[0]) * 10) + str(int(num[-1]))]
        elif len(num) == 3:
            if num[0] == "0":
                rightmost_ambiguities = self.calculate_ambiguities("".join(num[1:]))
                if rightmost_ambiguities:
                    ambiguities = ["0" + rightmost_ambiguities[0]]
            elif num[-1] == "0" and num[1] == "0":
                ambiguities = [num[0]]
            elif num[-1] == "0" and num[1] != "0":
                ambiguities = [num[:-1], str(int(num[0]) * 100) + str(int(num[1]) * 10), str(int(num[0]) * 100) + num[1]]
            else:
                ambiguities = [str(int(num[0]) * 100) + str(int(num[1:2]) * 10) + num[-1],
                               str(int(num[0]) * 100) + num[1] + num[-1],
                               str(int(num[0:2]) * 10) + num[-1]]
        return ambiguities

    def calculate_nums(self, num_list, step=0, current_number=""):
        step += 1
        ambiguities_remaining = 0
        for index, num in enumerate(num_list):
            if current_number:
                previous = current_number + "".join(num_list[:index]) + num
            else:
                previous = "".join(self.num_list[:index + step])
            if self.has_ambiguity(num, index=step+index):
                if not self.num_ambiguity_indexed(num):
                    self.ambiguities_dict[num] = self.calculate_ambiguities(num)
                    ambiguities_remaining += len(self.ambiguities_dict[num])
                self.calculate_nums(num_list[index + 1:], step=step+index, current_number=previous)
                try:
                    for i, amb in enumerate(self.ambiguities_dict[num]):
                        if current_number:
                            previous = current_number + "".join(num_list[:index]) + str(amb)
                        else:
                            previous = "".join(self.num_list[:index+step-1]) + str(amb)
                        self.calculate_nums(num_list[index + 1:], step=step + index, current_number=previous)
                        ambiguities_remaining -= 1
                        if i == len(self.ambiguities_dict[num]) - 1:
                            return
                except KeyError:
                    pass
            if index == len(num_list) - 1:
                print(previous)

    def has_ambiguity(self, num: str, index):
        if len(num) >= 2 and int(num) > 12:
            if num[-1] != "0":
                return True
            else:
                try:
                    if num[-1] == "0" and is_larger_by_factor_ten(num, self.num_list[index]):
                        return True
                except IndexError:
                    return False
        return False

    def num_ambiguity_indexed(self, num: str) -> bool:
        return num in self.ambiguities_dict.keys()

    def index_ambiguities(self, ambiguity_list, index):
        self.ambiguities_dict[index] = {ambiguity_list}
