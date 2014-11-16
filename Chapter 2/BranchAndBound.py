"""
    File: BranchAndBound
    Author: steve
    Created: 09/11/14
    
"""
import sys

all_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def linear_spectrum(peptide):
    prefix_mass = [0]

    for i in range(0, len(peptide)):
        prefix_mass.append(prefix_mass[i] + peptide[i])

    linear_spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    return sorted(linear_spectrum)


def is_consistent(theoretical, experimental):
    """

    :param theoretical: a theoretical spectrum
    :param experimental: an observed spectrum
    :return: True if the theoretical spectrum is consistent with the observed experimental spectrum.
    """

    # sanity check, total mass must be les than total mass of observed
    if len(theoretical) != 0 and sum(theoretical) > experimental[-1]:
        return False

    lin_spec = linear_spectrum(theoretical)
    exp = experimental[:]

    for t in lin_spec:
        if t in exp:
            exp.remove(t)
        else:
            return False
    return True


def expand(peptides):
    expanded = []
    for p in peptides:
        for m in all_masses:
            new_p = p + [m]
            expanded.append(new_p)

    return expanded


def cyclo_spectrum(peptide):
    prefix_mass = [0]

    for i in range(0, len(peptide)):
        prefix_mass.append(prefix_mass[i] + peptide[i])

    peptide_mass = prefix_mass[-1]

    cyclic_spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            # do wrap arounds
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))

    return sorted(cyclic_spectrum)


def cyclopeptide_sequencing(spectrum):
    parent_mass = spectrum[-1]
    peptides = [[]]
    results = []

    while len(peptides) > 0:
        peptides = expand(peptides)
        # make a copy so we can delete from original
        peps = peptides[:]
        for peptide in peps:
            if sum(peptide) == parent_mass:
                if cyclo_spectrum(peptide) == spectrum:
                    results.append(peptide)
                    peptides.remove(peptide)
            elif not is_consistent(peptide, spectrum):
                peptides.remove(peptide)

    return results


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    data = "0 101 103 113 114 115 128 128 129 186 186 214 216 229 232 241 242 257 289 314 329 330 342 357 360 371 372 418 427 443 457 458 474 475 486 500 528 546 571 571 587 589 603 604 613 643 660 690 699 700 714 716 732 732 757 775 803 817 828 829 845 846 860 876 885 931 932 943 946 961 973 974 989 1014 1046 1061 1062 1071 1074 1087 1089 1117 1117 1174 1175 1175 1188 1189 1190 1200 1202 1303"
    e = list(map(int, data.split(' ')))
    # #e= [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]

    results = cyclopeptide_sequencing(e)
    output = ""
    for result in results:
        output += ("-".join(map(str, result))) + " "

    print(output)


if __name__ == "__main__":
    sys.exit(main())