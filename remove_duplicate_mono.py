import argparse
import sys
import collections


def main(args):
    cnt_inline = 0
    cnt_outline = 0

    line_set = set()

    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1
            if line not in line_set:
                cnt_outline += 1
                line_set.add(line)
                print(line, end="")

    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())
