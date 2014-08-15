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
        return self.name



