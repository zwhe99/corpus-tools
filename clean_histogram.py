# modified from https://github.com/pytorch/fairseq/blob/main/examples/m2m_100/process_data/clean_histogram.py

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--src', type=str, help='Source language')
parser.add_argument('--tgt', type=str, help='Target language')
parser.add_argument('--input', type=str, help='Input source file')
parser.add_argument('--threshold', type=float, default=0.5, help='Threshold')
parser.add_argument('--threshold-character', type=str, default=']', help='Threshold character')
parser.add_argument('--histograms', type=str, help='Path to histograms')

args = parser.parse_args()

def read_hist(f):
    ch = []
    for line in f:
        c = line[0]
        if c == args.threshold_character:
            break
        ch.append(c)
    return ch

with(open("{}/{}".format(args.histograms, args.src), 'r', encoding='utf8')) as f:
    ch1 = read_hist(f)

with(open("{}/{}".format(args.histograms, args.tgt), 'r', encoding='utf8')) as f:
    ch2 = read_hist(f)

print("Accepted characters for {}: {}".format(args.src, ch1), file=sys.stderr)
print("Accepted characters for {}: {}".format(args.tgt, ch2), file=sys.stderr)

with open(args.input, 'r', encoding='utf8') as infile:
    for line in infile:
        fields = line.split('\t')
        src, tgt = fields[0].strip(), fields[1].strip()    

        cnt1 = len([c for c in src if c in ch1])
        cnt2 = len([c for c in tgt if c in ch2])

        if cnt1 / len(src) > args.threshold and cnt2 / len(tgt) > args.threshold:
            print(f"{src}\t{tgt}")