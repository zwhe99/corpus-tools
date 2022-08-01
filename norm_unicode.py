# unicodedata.normalize(form, unistr)
import unicodedata
import sys

if __name__ == "__main__":
    norm_type = sys.argv[1]
    for line in sys.stdin:
        print(unicodedata.normalize(norm_type, line), end='')