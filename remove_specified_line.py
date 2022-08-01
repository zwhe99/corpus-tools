# modified from https://github.com/microsoft/MASS/blob/master/MASS-unsupNMT/filter_noisy_data.py

import re
import argparse
import sys


def main(args):
    cnt_inline = 0
    cnt_outline = 0
    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1

            if line.strip() == args.pattern.strip():
                continue
            else:
                cnt_outline += 1
                print(line, end="")
    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument("--pattern", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())
