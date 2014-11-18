"""
    File: ApproxMatching
    Author: steve
    Created: 06/08/2014
    
"""
import sys


def read_string_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """
    with open(filename) as contents:
        lines = contents.readlines()
        pattern = lines[0].strip()
        sequence = lines[1].strip()
        num = int(lines[2].strip())

    return pattern, sequence, num


def is_approx_match(pattern, sequence, tolerance):
    if len(pattern) != len(sequence):
        return False

    mismatch_count = 0
    for a, b in zip(pattern, sequence):
        if a != b:
            mismatch_count += 1
            if mismatch_count > tolerance:
                return False

    return True


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # #pattern, sequence, tolerance = read_string_from_file(argv[1])
    sequence = "CATGCCATTCGCATTGTCCCAGTGA"
    pattern = "CCC"
    tolerance = 2

    approx_matches = []

    for i in range(len(sequence) - len(pattern) + 1):
        if is_approx_match(pattern, sequence[i:i + len(pattern)], tolerance):
            approx_matches.append(i)

    print len(approx_matches)

    print " ".join(str(s) for s in approx_matches)


if __name__ == "__main__":
    sys.exit(main())