"""
Tests for calc app
"""

import calculator


class TestCalcApp:
    def test_add(self):
        assert calculator.add(5, 5) == 10

    def test_sub(self):
        assert calculator.sub(10, 5) == 5

    def test_mul(self):
        assert calculator.mul(5, 5) == 25

    def test_sq(self):
        assert calculator.sq(5) == 25
