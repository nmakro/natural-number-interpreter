import sys
from utils import is_larger_by_factor_ten, print_valid_number


class NumberAnalyzer:
    def __init__(self, num_list: list):
        self.num_list = num_list
        self.ambiguities_dict = {}
        self.interpretations_count = 0

    def calculate_ambiguities(self, num: str):
        """"
        A heuristic method that calculates all possible ambiguities for greek numbers.
        """
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

    def calculate_nums(self, num_list: list, step=0, current_number=""):
        """
        A recursive method to calculate all possible numbers that can be produced by the ambiguities in the string provided.
        The algorithm exhausts all possible numbers that can be produced, by starting from left to right and if a number that can
        produce an ambiguity is found, then this method is called recursively for the remaining string. To construct the final number printed
        the string before the ambiguity is passed to the function by using the current_number param. When the method returns it is called again
        with the remaining string but the ambiguity now is passed as an argument by using the current number param again.

        :param num_list:
        :param step:
        :param current_number:
        :return:
        """
        step += 1
        for index, num in enumerate(num_list):
            if current_number:
                previous = current_number + "".join(num_list[:index]) + num
            else:
                previous = "".join(self.num_list[:index + step])
            if self.has_ambiguity(num, index=step + index):
                if not self.num_ambiguity_indexed(num):
                    self.ambiguities_dict[num] = self.calculate_ambiguities(num)
                self.calculate_nums(num_list[index + 1:], step=step + index, current_number=previous)
                try:
                    for i, amb in enumerate(self.ambiguities_dict[num]):
                        if current_number:
                            previous = current_number + "".join(num_list[:index]) + str(amb)
                        else:
                            previous = "".join(self.num_list[:index + step - 1]) + str(amb)
                        self.calculate_nums(num_list[index + 1:], step=step + index, current_number=previous)
                        if i == len(self.ambiguities_dict[num]) - 1:
                            return
                except KeyError:
                    pass
            if index == len(num_list) - 1:
                self.interpretations_count += 1
                sys.stdout.write(f"Interpretation {self.interpretations_count}: {previous} [phone number: {print_valid_number(previous)}]\n")

    def has_ambiguity(self, num: str, index):
        """
        Find if current number is ambiguous and if there is an ambiguity with the number following.
        Such example is .. 20 3.. or .. 200 3 .. A more complex ambiguity is this .. 020 3..
        """
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

    def index_ambiguities(self, ambiguity_list: list, index: int):
        self.ambiguities_dict[index] = ambiguity_list
