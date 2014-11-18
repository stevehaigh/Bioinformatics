"""
    File: TheoreticalSpectrum
    Author: steve
    Created: 08/11/14
    
"""
import sys

integer_mass = dict(G=57, A=71, S=87, P=97, V=99, T=101, C=103, I=113, L=113, N=114, D=115, K=128, Q=128, E=129, M=131,
                    H=137, F=147, R=156, Y=163, W=186)


def linear_spectrum(peptide):
    """
    :param peptide: string representation of a peptide
    :return: integer linear spectrum as a list of int
    """

    prefix_mass = [0]

    for i in range(0, len(peptide)):
        amino = peptide[i]
        prefix_mass.append(prefix_mass[i] + integer_mass[amino])

    linear_spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    return sorted(linear_spectrum)


def cyclic_spectrum(peptide):
    """
    :param peptide: string representation of a peptide
    :return: integer cyclic spectrum as a list of int
    """

    prefix_mass = [0]

    for i in range(0, len(peptide)):
        amino = peptide[i]
        prefix_mass.append(prefix_mass[i] + integer_mass[amino])

    peptide_mass = prefix_mass[len(peptide)]

    cyclic_spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            # do wrap arounds
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))

    return sorted(cyclic_spectrum)


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # #peptide = "PEEP"

    # #lin_spec = linear_spectrum(peptide)
    # #print(' '.join(map(str, lin_spec)))

    peptides = ["MAMA"]

    for peptide in peptides:
        spec = cyclic_spectrum(peptide)
        print(' '.join(map(str, spec)))


if __name__ == "__main__":
    sys.exit(main())