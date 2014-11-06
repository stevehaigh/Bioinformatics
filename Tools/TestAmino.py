import unittest
from . import Amino
from . import CodonTable

class TestAminoClass(unittest.TestCase):

    def test_create_amino(self):

        name = "MyAmino"
        tla = "mya"
        letter = "M"
        codon1 = "GCA"
        codon2 = "GCC"
        codons = [codon1, codon2]

        amino = Amino.Amino(name, tla, letter, codons)

        self.assertEqual(amino.name, name)
        self.assertEqual(amino.tla, tla)
        self.assertEqual(amino.letter, letter)
        self.assertEqual(len(amino.codons), 2)
        self.assertEqual(amino.codons[0], codon1)
        self.assertEqual(amino.codons[1], codon2)


    def test_create_codon_table(self):
        table = CodonTable()

        amino = table.get_amino_for_codon("CUA")
        self.assertEqual(amino.letter, "L", "Wrong amino for sequence!")

        stop = table.get_amino_for_codon("UAG")
        self.assertEqual(stop.name, "(Stop)", "Wrong amino for sequence!")

        codons = table.get_codons_for_amino("L")
        self.assertEqual(len(codons), 6, "Wrong number of codons for L")
        self.assertTrue("UUA" in codons)

        codons = table.get_codons_for_amino("M")
        self.assertEqual(codons, ["AUG"], "Methionine only has one codon!")
