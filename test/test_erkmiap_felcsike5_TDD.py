from unittest import TestCase

from erkmiap_felcsike5_TDD import ket_szam_osszege_a_haramdik


class Test(TestCase):
    def test_ket_szam_osszege_a_haramdik(self):
        a = 1
        b = 2
        c = 3
        d = 4

        actual_value_true = ket_szam_osszege_a_haramdik(a, b, c)
        actual_value_false = ket_szam_osszege_a_haramdik(a, b, d)

        self.assertEqual(True, actual_value_true, "nem jó az egyelőség vizsgálat")
        self.assertEqual(False, actual_value_false, "nem jó a hibás válasz")

        # self.assertTrue(actual_value_true, "nem jó az egyelőség vizsgálat")
        # self.assertFalse(actual_value_false, "nem jó a hibás válasz")
