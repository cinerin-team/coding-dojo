from unittest import TestCase

from etotist_felcsi_15 import fibo_smaller

class Test(TestCase):
    def test_fibo_smaller(self):
        expect = "0 1 1"
        actual = fibo_smaller(2)

        self.assertEqual(expect, actual, "Egyenlő, jihááá!")
        self.assertNotEqual('o.O', actual, "Nem egyenlő, búúú!")
