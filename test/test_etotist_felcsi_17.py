from unittest import TestCase

from etotist_felcsi_17 import all_three_pos


class Test(TestCase):
    def test_all_three_pos(self):
        expect = True
        actual = all_three_pos(4, 12, 14)

        self.assertEqual(expect, actual, ":) *.* <3!")
        self.assertNotEqual('o.O', actual, ":( -.-")
