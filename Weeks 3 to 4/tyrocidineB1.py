"""
    File: tyrocidineB1
    Author: steve
    Created: 01/11/2014
    
"""
import sys

from Tools.CodonTable import CodonTable


protein_mapping = {"His": "H",
                   "Gln": "Q",
                   "Pro": "P",
                   "Arg": "R",
                   "Leu": "L",
                   "Asp": "D",
                   "Glu": "E",
                   "Ala": "A",
                   "Gly": "G",
                   "Val": "V",
                   "Tyr": "Y",
                   "Ser": "S",
                   "Cys": "C",
                   "Trp": "W",
                   "Phe": "F",
                   "Asn": "N",
                   "Lys": "K",
                   "Thr": "T",
                   "Ile": "I",
                   "Met": "M"}


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

        tyrocidineB1 = "Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr"
        tyrList = tyrocidineB1.split("-")
        table = CodonTable()
        aminoCount = 1

        for p in tyrList:
            codons = table.get_codons_for_amino(protein_mapping[p])
            print(p, " ", len(codons))
            aminoCount *= len(codons)

        print aminoCount
        aminoCount = 1
        print("MASS")
        for p in ['M', 'A', 'S', 'S']:
            codons = table.get_codons_for_amino(p)
            print(p, " ", len(codons))
            aminoCount *= len(codons)

        print aminoCount


if __name__ == "__main__":
    sys.exit(main())