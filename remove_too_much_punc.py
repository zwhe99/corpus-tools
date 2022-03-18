# modified from https://github.com/pytorch/fairseq/blob/main/examples/m2m_100/process_data/remove_too_much_punc.py


import argparse
from string import punctuation
import sys

def len_no_punc(s, punc):
    return len([ch for ch in s if ch in punc])

def filter_overpunc(len_npunc, len_sen):
    return len_npunc < 0.5*len_sen

def main(args):
    punc = punctuation + "—|–"
    cnt_inline = 0
    cnt_outline = 0
    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1
            fields = line.split('\t')
            src, tgt = fields[0].strip(), fields[1].strip()      

            nchar_npunc_src = len_no_punc(src, punc)
            nchar_npunc_tgt = len_no_punc(tgt, punc)

            if filter_overpunc(nchar_npunc_src, len(src)) and filter_overpunc(nchar_npunc_tgt, len(tgt)):
                cnt_outline += 1
                print(f"{src}\t{tgt}")
    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())
