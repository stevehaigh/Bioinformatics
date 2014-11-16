"""
    File: SpectralConvolution
    Author: steve
    Created: 13/11/14
    
"""
import sys


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    list_as_space_separated_string = "773 920 923 473 342 1051 285 792 128 129 156 673 360 0 608 544 895 131 137 664 388 774 764 113 266 479 535 902 738 886 488 257 730 1023 551 379 617 645 893 739 996 663 792 129 610 1152 1021 601 360 128 413 259 285 1015 1024 679 378 542 1039 414 867 867 1023 507 229 232 489 241 810 250 101 422 911 1024"
    list_as_string = list_as_space_separated_string.split(' ')

    integer_masses = sorted(list(map(int, list_as_string)))

    result = []

    for i in range(0, len(integer_masses)):
        for j in range(i + 1, len(integer_masses)):
            if (integer_masses[j] - integer_masses[i] > 0):
                result.append(integer_masses[j] - integer_masses[i])

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    sys.exit(main())