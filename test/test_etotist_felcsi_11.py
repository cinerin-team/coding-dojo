from unittest import TestCase

from etotist_felcsi_11 import shitting_out_0_or_1


class Test(TestCase):
    def test_shitting_out_0_or_1(self):
        expect = '010'
        actual = shitting_out_0_or_1(3)

        self.assertEqual(expect,actual,"Egyenlő!")
        self.assertNotEqual('0101', actual, "Nem egyenlő!")


