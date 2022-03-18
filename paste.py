import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
    for l1, l2 in zip(f1, f2):
        l1 = l1.strip()
        l2 = l2.strip()
        print("{}\t{}".format(l1, l2))
