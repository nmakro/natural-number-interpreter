from analyzer import NumberAnalyzer
from utils import get_user_input, validate_input


def run():

    user_in = get_user_input()
    validate_input(user_in)

    analyzer = NumberAnalyzer(user_in.split())
    analyzer.calculate_nums(analyzer.num_list, step=0, current_number="")


if __name__ == "__main__":
    run()
