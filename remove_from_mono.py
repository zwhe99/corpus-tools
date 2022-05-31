import argparse
import sys

def main(args):
    existing_data = set()
    for ref_file in args.reference:
        with open(ref_file, 'r', encoding=args.encoding) as f:
            existing_data |= set(f.read().splitlines())

    cnt_inline = 0
    cnt_outline = 0
    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1
            line = line.strip()
            
            if line not in existing_data:
                cnt_outline += 1
                print(line)
    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument("--reference", nargs="+", required=True)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())
