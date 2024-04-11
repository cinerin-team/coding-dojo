from unittest import TestCase

from etotist_felcsi_14 import print_out_stars


class Test(TestCase):
    def test_print_out_stars(self):
        expect = '***\n***\n'
        actual = print_out_stars(2,3)

        self.assertEqual(expect,actual,"Egyenlő, jihááá!")
        self.assertNotEqual('o.O', actual, "Nem egyenlő, búúú!")
