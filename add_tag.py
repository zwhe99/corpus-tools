# unicodedata.normalize(form, unistr)
import unicodedata
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        print(f"{sys.argv[1]} {line}", end='')