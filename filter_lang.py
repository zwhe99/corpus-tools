# modified from https://github.com/microsoft/MASS/blob/master/MASS-unsupNMT/filter_noisy_data.py

import argparse
import sys
from langdetect import detect
from polyglot.detect import Detector
from polyglot.detect.base import logger as polyglot_logger
polyglot_logger.setLevel("ERROR")

def detect_lang(text, lang):
    try:
        for i, l in enumerate(Detector(text, quiet=True).languages):
            if l.code == lang and i == 0:
                return True
        if detect(text) == lang:
            return True
        return False
    except:
        return False

def main(args):
    cnt_inline = 0
    cnt_outline = 0
    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1
            fields = line.split('\t')
            src, tgt = fields[0].strip(), fields[1].strip()      

            if detect_lang(src, args.src) and detect_lang(tgt, args.tgt) :
                cnt_outline += 1
                print(f"{src}\t{tgt}")

    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    parser.add_argument('--src', type=str, help='Source language')
    parser.add_argument('--tgt', type=str, help='Target language')
    main(parser.parse_args())
