
import argparse
import sys
import time
import kenlm

def main(args):
    start = time.time()
    model = kenlm.Model(args.language_model)

    with open(args.output_file, 'w') as fout:
        for line in sys.stdin:
            line = line.strip()

            #EOS BOS
            sent_len = len(line.split()) + 2
    
            #normalized score
            fout.write(str(model.score(line, bos=True, eos=True)/sent_len) + '\n')

    end = time.time()
    print(f"Done: {end-start}s")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-lm", "--language-model", required=True, type=str, help='path to kenlm model')
    parser.add_argument("-o", "--output-file", required=True, type=str, help='path to output file')
    main(parser.parse_args())
