import argparse
import os
from sacremoses import MosesPunctNormalizer
import time
import sys

def most_frequent(lst):
    return max(set(lst), key = lst.count)

def main(args):
    start = time.time()
    pivot_lang, pref1, lang1, pref2, lang2 = args.pivot_lang, args.pref1, args.lang1, args.pref2, args.lang2
    assert pivot_lang != lang1 and pivot_lang != lang2
    assert os.path.isfile(f"{pref1}.{pivot_lang}")
    assert os.path.isfile(f"{pref2}.{pivot_lang}")
    assert os.path.isfile(f"{pref1}.{lang1}")
    assert os.path.isfile(f"{pref2}.{lang2}")

    mpn = MosesPunctNormalizer(lang=pivot_lang, pre_replace_unicode_punct=True)
    with open(f"{pref1}.{pivot_lang}", 'r') as f1_pivot, \
        open(f"{pref1}.{lang1}", 'r') as f1_lang1, \
        open(f"{pref2}.{pivot_lang}", 'r') as f2_pivot, \
        open(f"{pref2}.{lang2}", 'r') as f2_lang2:
        
        sent1p = [mpn.normalize(s) for s in f1_pivot]
        sent11 = [s for s in f1_lang1]
        sent2p = [mpn.normalize(s) for s in f2_pivot]
        sent22 = [s for s in f2_lang2]

    pivot_sent = []
    for ps in set(sent1p) & set(sent2p):
        if ps != "\n" and len(ps) > 2:
            pivot_sent.append(ps)

    with open(f"{args.out_pref}.{lang1}", 'w') as fo_lang1, \
        open(f"{args.out_pref}.{lang2}", 'w') as fo_lang2:
        for ps in pivot_sent:
            indices1 = [i for i, x in enumerate(sent1p) if x == ps]
            indices2 = [i for i, x in enumerate(sent2p) if x == ps]

            candidate_sent11 = [sent11[id] for id in indices1]
            candidate_sent22 = [sent22[id] for id in indices2]

            fo_lang1.write(most_frequent(candidate_sent11))
            fo_lang2.write(most_frequent(candidate_sent22))
            print(ps.strip())
    end = time.time()
    print(f"Done: {end-start}s", file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pivot-lang", required=True, type=str, help='pivot language')
    parser.add_argument("--pref1", required=True, type=str, help='prefix of corpus 1')
    parser.add_argument("--lang1", required=True, type=str, help='the other lang of corpus 1')
    parser.add_argument("--pref2", required=True, type=str, help='prefix of corpus 2')
    parser.add_argument("--lang2", required=True, type=str, help='the other lang corpus 2')
    parser.add_argument("--out-pref", required=True, type=str, help='prefix of output file')
    main(parser.parse_args())
