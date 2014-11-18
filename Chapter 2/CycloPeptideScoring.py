"""
    File: CycloPeptideScoring
    Author: steve
    Created: 09/11/14
    
"""
import sys

import TheoreticalSpectrum as theoretical


def get_score(peptide, spectrum):
    score = 0
    cyc_spectrum = theoretical.cyclic_spectrum(peptide)

    for c in cyc_spectrum:
        if c in spectrum:
            score += 1
            spectrum.remove(c)

    return score


def get_linear_score(peptide, spectrum):
    score = 0
    cyc_spectrum = theoretical.linear_spectrum(peptide)

    for c in cyc_spectrum:
        if c in spectrum:
            score += 1
            spectrum.remove(c)

    return score


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    pep = "PEEP"
    spec = "0 97 97 97 100 129 194 226 226 226 258 323 323 355 393 452"
    s = list(map(int, spec.split(' ')))

    print(get_linear_score(pep, s))


if __name__ == "__main__":
    sys.exit(main())