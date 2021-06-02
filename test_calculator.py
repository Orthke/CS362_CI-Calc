"""
Tests for calc app
"""

import pytest
from calculator import *

class TestCalcApp:

    def test_add(self):
        assert add(5, 5) == 10


    def test_sub(self):
        assert sub(10, 5) == 5


    def test_mul(self):
        assert mul(5, 5) == 25

    def test_sq(self):
        assert sq(5) == 25
