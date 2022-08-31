import argparse
import nltk

def get_freqs(line):
    words = line.split()
    unigrams = list(nltk.ngrams(words, 1))
    bigrams = list(nltk.ngrams(words, 2))
    trigrams = list(nltk.ngrams(words, 3))

    unigram_freqs = nltk.FreqDist(unigrams)
    bigram_freqs = nltk.FreqDist(bigrams)
    trigram_freqs = nltk.FreqDist(trigrams)

    return unigram_freqs, bigram_freqs, trigram_freqs

def get_counts(unigram_freqs, bigram_freqs, trigram_freqs):
    counts = []
    for freqs in [unigram_freqs, bigram_freqs, trigram_freqs]:
        if len(freqs) > 0:
            _, most_common_gram_count =  freqs.most_common(1)[0]
        else:
            most_common_gram_count = 0
        counts.append(most_common_gram_count)
    return counts

def is_repeat(src_line, hyp_line):
    hyp_unigram_freqs, hyp_bigram_freqs, hyp_trigram_freqs = get_freqs(hyp_line)
    hyp_counts = get_counts(hyp_unigram_freqs, hyp_bigram_freqs, hyp_trigram_freqs)

    if max(hyp_counts) <= 3:
        return False
    else:
        src_unigram_freqs, src_bigram_freqs, src_trigram_freqs = get_freqs(src_line)
        src_counts = get_counts(src_unigram_freqs, src_bigram_freqs, src_trigram_freqs)
        if abs(max(src_counts) - max(hyp_counts)) <= 2:
            return False
        else:
            return True

def main(args):
    with open(args.src_file) as sf, open(args.hyp_file) as hf , open(args.no_repeat_hyp_file) as nrhf: 
        for (src_line, hyp_line, no_repeat_hyp_line) in zip(sf, hf, nrhf):
            if is_repeat(src_line, hyp_line):
                print(no_repeat_hyp_line, end="")
            else:
                print(hyp_line, end="")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src-file", required=True, type=str)
    parser.add_argument("--hyp-file", required=True, type=str)
    parser.add_argument("--no-repeat-hyp-file", required=True, type=str)
    parser.add_argument('--encoding', default='utf-8', help='character encoding for input/output')
    main(parser.parse_args())