import argparse
import sys

def main(args):
    cnt_inline = 0
    cnt_outline = 0
    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1
            fields = line.split('\t')
            src, tgt, score = fields[0].strip(), fields[1].strip(), float(fields[2].strip())      

            if score > 0.5:
                cnt_outline += 1
                print(f"{src}\t{tgt}")
            else:
                print(f"[Remove pair] Src:{src}\tTgt:{tgt}\tScore:{score})", file=sys.stderr)
    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())
