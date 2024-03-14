from unittest import TestCase

from erkmiap_felcsike4_TDD_minta import oszthato_e_ottel_vagy_harommal


class Test(TestCase):
    def test_oszthato_e_ottel_vagy_harommal(self):
        het = 7
        ot = 5

        actual_value_true = oszthato_e_ottel_vagy_harommal(ot)
        actual_value_false = oszthato_e_ottel_vagy_harommal(het)

        self.assertEqual("igen osztható 5-tel vagy 3-mal", actual_value_true, "az oszhatóság nincs jól ellenőrizve")
        self.assertEqual("nem osztható 5-tel vagy 3-mal", actual_value_false, "ha nem oszható akkor nem jó a válasz")

