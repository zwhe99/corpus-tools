import argparse

def main(args):
    word2freq = dict()
    with open(args.share_vocab, 'r', encoding=args.encoding) as f:
        for line in f:
            word = line.split()[0].strip()
            word2freq[word] = 0
    
    with open(args.corpus, 'r', encoding=args.encoding) as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word in word2freq:
                    word2freq[word] += 1
    total = sum(word2freq.values())
    word2freq = {k: v / total for k, v in word2freq.items()}

    with open(args.output, 'w', encoding=args.encoding) as f:
        for k, v in word2freq.items():
            f.write(f"{k} {v}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--share-vocab", required=True, type=str)
    parser.add_argument("--corpus", required=True, type=str)
    parser.add_argument("--output", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())
