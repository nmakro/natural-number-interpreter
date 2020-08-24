from utils import validate_input


def run():
    user_input = input("Please enter your number: ")

    validate_input(user_input)

    print("Valid")


if __name__ == "__main__":
    run()
