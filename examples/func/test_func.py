from unittest import TestCase

from examples.func.func import ex_func


class Test(TestCase):
    def test_ex_func(self):
        exp_val = 4
        act_val = ex_func(2)
        self.assertEqual(exp_val, act_val)
