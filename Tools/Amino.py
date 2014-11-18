"""
    Class representing an Amino acid, used to store full name, TLA and single letter, also a list
    of associated codons for reverse lookups.

"""

class Amino(object):
    """

    """

    def __init__(self, name="", tla="", letter="", codons=[]):
        self.name = name
        self.tla = tla
        self.letter = letter
        self.codons = codons


    def __str__(self):
        return self.letter

    def single_letter(self):
        if self.letter != '*':
            return self.letter

        return ""

    protein_mapping = {"His":"H",
                      "Gln":"Q",
                      "Pro":"P",
                      "Arg":"R",
                      "Leu":"L",
                      "Asp":"D",
                      "Glu":"E",
                      "Ala":"A",
                      "Gly":"G",
                      "Val":"V",
                      "Tyr":"Y",
                      "Ser":"S",
                      "Cys":"C",
                      "Trp":"W",
                      "Phe":"F",
                      "Asn":"N",
                      "Lys":"K",
                      "Thr":"T",
                      "Ile":"I",
                      "Met":"M"}




