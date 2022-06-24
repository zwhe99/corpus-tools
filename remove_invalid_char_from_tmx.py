# https://stackoverflow.com/questions/8888628/how-should-i-deal-with-an-xmlsyntaxerror-in-pythons-lxml-while-parsing-a-large

import argparse
from string import punctuation
import sys
from lxml import etree
from io import StringIO 

BAD = []
for i in range(0, 1000):
    try:
        x = etree.parse(StringIO('<p>%s</p>' % chr(i)))
    except etree.XMLSyntaxError:
        BAD.append(i)
BAD.append(0xFFFE)
BAD_BASESTRING_CHARS = [chr(b) for b in BAD]
BAD_BASESTRING_CHARS.remove('&')
BAD_BASESTRING_CHARS.remove('<')
def remove_bad_chars(value):
    # Remove bad control characters.
    for char in BAD_BASESTRING_CHARS:
        value = value.replace(char, '')
    return value

def main(args):
    with open(args.input, 'r') as fin, open(args.output, 'w') as fout:
        for line in fin:
            fout.write(remove_bad_chars(line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, type=str)
    parser.add_argument("-o", "--output", required=True, type=str)
    main(parser.parse_args())
