from assertpy import assert_that
from src import fizzbuzz

class TestFizzBuzz:

    def test_given_empty_value_return_empty_value(self):
        assert_that(fizzbuzz.calculate(""), "")