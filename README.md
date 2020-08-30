# A natural number interpreter for greek telephone numbers.

This projects includes an interperter application to validate if the given number is a greek telephone number and also identify all possible amiguities in number spelling.
The input accepts a sequence of numbers with the restriction that each number may be up to three digits.

Some examples of ambiguities that come from the greek language:

- A two digit number above 12 like 25 may be interpeted like 20 5. The opposite is also true.

- A three digit number like 725 may be interpreted in to 720 5 or 700 25 or 700 20 5.


# Usage for installing and running the application inside a docker container.

- From the current directory inside your local maching type inside a terminal `make up` to build and run the container.

- Type `make install` to install the project inside the container.

- Type `make run` to interact with the application.

- To run the tests and report the test-coverage type `make tests`

- To stop the container from running type `make down`


# Usage examples.

- `make tests` outputs:

```shell
----------------------------------------------------------------------
Ran 5 tests in 0.006s

OK
Name                             Stmts   Miss  Cover
----------------------------------------------------
number_interpreter/__init__.py       0      0   100%
number_interpreter/analyzer.py      68     13    81%
number_interpreter/utils.py         69     10    86%
tests/__init__.py                    0      0   100%
tests/context.py                     4      0   100%
tests/test_interpreter.py           21      1    95%
tests/test_utils.py                 20      1    95%
----------------------------------------------------
TOTAL                              182     25    86%

```
- `make run` outputs:

```shell
Please enter your number: 2 10 69 30 6 6 4
Interpretation 1: 2106930664 [phone number: VALID]
Interpretation 2: 210693664 [phone number: INVALID]
Interpretation 3: 21060930664 [phone number: INVALID]
Interpretation 4: 2106093664 [phone number: VALID]
```

