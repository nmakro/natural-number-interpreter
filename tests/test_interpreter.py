import unittest
from unittest.mock import patch, call
from .context import analyzer


class InterpreterTest(unittest.TestCase):
    def setUp(self) -> None:
        patcher1 = patch("number_interpreter.analyzer.sys")
        self.mock_sys_out = patcher1.start()

    def tearDown(self) -> None:
        self.mock_sys_out.stop()

    def test_interpreter_finds_four_ambiguities(self):
        interpreter = analyzer.NumberInterpreter("2 10 69 30 6 6 4".split())
        interpreter.calculate_nums(interpreter.num_list, step=0, current_number="")
        calls = [call.stdout.write('Interpretation 1: 2106930664 [phone number: VALID]\n'),
                 call.stdout.write('Interpretation 2: 210693664 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 3: 21060930664 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 4: 2106093664 [phone number: VALID]\n'),
                 ]
        self.mock_sys_out.stdout.write.assert_has_calls(calls=calls)

    def test_interpreter_finds_ambiguity_of_three_digits_num(self):
        interpreter = analyzer.NumberInterpreter("724 100 1".split())
        interpreter.calculate_nums(interpreter.num_list, step=0, current_number="")

        calls = [call.stdout.write('Interpretation 1: 7241001 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 2: 72411 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 3: 7002041001 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 4: 70020411 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 5: 700241001 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 6: 7002411 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 7: 72041001 [phone number: INVALID]\n'),
                 call.stdout.write('Interpretation 8: 720411 [phone number: INVALID]\n'),
                 ]
        self.mock_sys_out.stdout.write.assert_has_calls(calls=calls)


if __name__ == '__main__':
    unittest.main()
