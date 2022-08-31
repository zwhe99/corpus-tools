import unicodedata
import sys

def which_norm(s):
    all_norms = ["NFC", "NFKC", "NFD", "NFKD"]

    res_norm = []

    for norm in all_norms:
        if unicodedata.is_normalized(norm, s):
            res_norm.append(norm)

    return " ".join(res_norm)

if __name__ == "__main__":
    for line in sys.stdin:
        print(which_norm(line))