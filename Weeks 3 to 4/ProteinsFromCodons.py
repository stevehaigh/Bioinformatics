"""
    File: ProteinsFromCodons
    Author: steve
    Created: 01/11/2014
    
"""
import sys

from Tools.CodonTable import CodonTable


def GetCodonsFromFile():
    return open("codons1.txt").readline()

    # #return "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"


def codonGenerator(data):
    for i in range(0, len(data), 3):
        yield data[i:i + 3]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    table = CodonTable()
    codons = GetCodonsFromFile()
    protein = ""

    seqs = ["CCGAGGACCGAAAUCAAC", "CCCCGUACGGAGAUGAAA", "CCCAGGACUGAGAUCAAU", "CCUCGUACUGAUAUUAAU"]

    for dna_seq in seqs:
        protein = ""
        for c in codonGenerator(dna_seq):
            protein += table.get_amino_for_codon(c).single_letter()

        print(dna_seq, protein)


if __name__ == "__main__":
    sys.exit(main())