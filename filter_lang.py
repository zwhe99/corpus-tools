# modified from https://github.com/microsoft/MASS/blob/master/MASS-unsupNMT/filter_noisy_data.py

import argparse
import sys
import gcld3

detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=1000)

def detect_lang(text, lang, need_reliable):
    result = detector.FindLanguage(text=text)
    if need_reliable:
        if result.language == lang and result.is_reliable:
            return True
        else:
            return False
    else:
        if result.language == lang:
            return True
        else:
            return False

def main(args):
    cnt_inline = 0
    cnt_outline = 0
    with open(args.input, 'r', encoding=args.encoding) as infile:
        for line in infile:
            cnt_inline += 1
            fields = line.split('\t')
            src, tgt = fields[0].strip(), fields[1].strip()      

            if detect_lang(src, args.src, args.reliable) and detect_lang(tgt, args.tgt, args.reliable) :
                cnt_outline += 1
                print(f"{src}\t{tgt}")

    print(f"# Input sent. ({cnt_inline}) > # Output sent. ({cnt_outline})", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    parser.add_argument('--src', type=str, help='Source language')
    parser.add_argument('--reliable', action="store_true", help='whether language recognition is required to be reliable')
    parser.add_argument('--tgt', type=str, help='Target language')
    main(parser.parse_args())
