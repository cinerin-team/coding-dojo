from unittest import TestCase

from etotist_felcsi_16 import com_div


class Test(TestCase):
    def test_com_div(self):
        expect = False
        actual = com_div(5)

        self.assertEqual(expect, actual, "Gratulálok, Uram!")
        self.assertNotEqual('o.O', actual, "Szégyenteljes!")
