import xmltodict
import argparse
from gzip import GzipFile

def main(args):
    data = {
        args.src_lang: [],
        args.tgt_lang: [],
    }

    def get_sentence_pairs(_, tree):
        assert len(tree['tuv']) == 2
        for elem in tree['tuv']:
            lang = elem['@xml:lang']
            text = elem['seg']
            if text is None:
                text = ''
            else:
                text = f"{text} "

            assert lang in [args.src_lang, args.tgt_lang]
            data[lang].append(text)

        return True


    xmltodict.parse(
        GzipFile(args.input),
        item_depth=3, item_callback=get_sentence_pairs,
    )
    
    assert len(data[args.src_lang]) == len(data[args.tgt_lang])

    with open(f"{args.prefix}.{args.src_lang}", "w", encoding=args.encoding) as src_f, \
        open(f"{args.prefix}.{args.tgt_lang}", "w", encoding=args.encoding) as tgt_f:
            for (src_sent, tgt_sent) in zip(data[args.src_lang], data[args.tgt_lang]):
                src_f.write(f"{src_sent}\n")
                tgt_f.write(f"{tgt_sent}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str, help="tmx file")
    parser.add_argument("-s", "--src-lang", required=True, type=str, help="source language")
    parser.add_argument("-t", "--tgt-lang", required=True, type=str, help="target language")
    parser.add_argument("--prefix", required=True, type=str, help="prefix of output file")
    parser.add_argument('--encoding', default='UTF-8', help='character encoding for input/output')
    main(parser.parse_args())