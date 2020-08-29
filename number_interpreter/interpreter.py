from utils import validate_input, Indexer


def run():

    l = "2 10 020 03 3 60 4   ".split()
    indexer = Indexer(l)

    indexer.calculate_nums(l, step=0, current_number="")


if __name__ == "__main__":
    run()
