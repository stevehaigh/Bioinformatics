"""
    File: RandomisedMotifSearch
    Author: steve
    Created: 25/11/14
    
"""
import random
import sys
from builtins import range, len

import GreedyMotifSearch as gms


def initialize_random_motifs(dna, k):
    result = []
    l = len(dna[0])
    i = random.randint(0, l - k)
    for row in dna:
        result.append(row[i:i + k])

    return result


def create_profile(motifs):
    return gms.create_profile_with_pseudocounts(motifs, len(motifs))


def create_motifs(profile, dna, k):
    """
    for each row get the most probably kmer given profile
    :param profile:
    :param dna:
    :param k:
    :return:
    """

    result = []
    for seq in dna:
        result.append(gms.get_profile_most_probable_kmer(seq, k, profile))

    return result


def score_motifs(motifs):
    motif_score = 0

    for i in range(0, len(motifs)):
        for j in range(i + 1, len(motifs)):
            motif_score += gms.get_hamming_distance(motifs[i], motifs[j])

    return motif_score


def randomised_motif_search(dna, k, t):
    """
    RANDOMIZEDMOTIFSEARCH(Dna, k, t)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string
            from Dna
        BestMotifs ← Motifs
        while forever
            Profile ← Profile(Motifs)
            Motifs ← Motifs(Profile, Dna)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
            else
                return BestMotifs
    """

    motifs = initialize_random_motifs(dna, k)
    best_motifs = motifs
    best_motif_score = score_motifs(best_motifs)

    while True:
        profile = create_profile(motifs)
        motifs = create_motifs(profile, dna, k)
        motif_score = score_motifs(motifs)
        if motif_score < best_motif_score:
            best_motif_score = motif_score
            best_motifs = motifs
        else:
            return best_motifs, best_motif_score


def rms_multiple(dna, k, t, n):
    best_result = []
    best_score = sys.maxsize

    for i in range(0, n):
        result, score = randomised_motif_search(dna, k, t)
        if score < best_score:
            best_result = result
            best_score = score
            print(score)

    return best_result


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv


if __name__ == "__main__":
    sys.exit(main())