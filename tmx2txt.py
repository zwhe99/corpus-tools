from translate.storage.tmx import tmxfile
import argparse

def main(args):
    with open(args.input, 'rb') as fin:
        tmx_file = tmxfile(fin, args.src_lang, args.tgt_lang, encoding=args.encoding)

    with open(f"{args.prefix}.{args.src_lang}", "w", encoding=args.encoding) as src_f, \
        open(f"{args.prefix}.{args.tgt_lang}", "w", encoding=args.encoding) as tgt_f:
            for node in tmx_file.unit_iter():
                src_f.write(f"{node.source}\n")
                tgt_f.write(f"{node.target}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str, help="tmx file")
    parser.add_argument("-s", "--src-lang", required=True, type=str, help="source language")
    parser.add_argument("-t", "--tgt-lang", required=True, type=str, help="target language")
    parser.add_argument("--prefix", required=True, type=str, help="prefix of output file")
    parser.add_argument('--encoding', default='UTF-8', help='character encoding for input/output')
    main(parser.parse_args())