"""
    Codon lookup table.
"""
from Tools.Amino import Amino


class CodonTable(object):


    def __init__(self):
        """
            Read the text file to create the table of Aminos for each codon.
        :return:
            A dict mapping codon to Amino acid.
        """

        with open("coding_data.txt") as contents:
            for line in contents.readlines():
                # E.g. "UUU Phe F Phenylalanine"
                items = line.split()
                codon, tla, letter, name = items[0:4]
                if len(items) > 4:
                    name += " " + "".join(items[4:])
                if letter not in self._aminos.keys():
                    self._aminos[letter] = Amino(name, tla, letter, [])


                self._aminos[letter].codons += [codon]

                self._mapping_table[codon] = self._aminos[letter]


    def get_amino_for_codon(self, codon):
        """

        :param codon: a string representing a codon.
        :return: An amino acid object of found, otherwise None.
        """
        if codon in self._mapping_table.keys():
            return self._mapping_table[codon]

        return None

    def get_codons_for_amino(self, amino):
        """

        :param amino: single letter amino acid name.
        :return: a list of codons that encode for that acid, empty if the amino is not valid.
        """
        if amino in self._aminos.keys():
            return self._aminos[amino].codons

        return []


    _aminos = {}
    _mapping_table = {}