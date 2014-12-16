from builtins import len, range, open
import sys


def reconstruct(kmers):
    reconstructed = ""
    for i in range(0, len(kmers) - 1):
        reconstructed += (kmers[i][0])

    reconstructed += (kmers[-1])

    return reconstructed


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    with open("paths.txt") as contents:
        kmers = contents.readlines()

    result = reconstruct(kmers)

    with open("result.txt", "w") as text_file:
        text_file.write(result)


if __name__ == "__main__":
    sys.exit(main())