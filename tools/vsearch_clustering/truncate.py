#!/usr/bine/env python

import sys


def truncate(fasta, quantity):
    """
    Truncates all the sequences of the file by quantity
    """
    fh = open(fasta, 'r')
    seq = list()
    lines = fh.readlines()
    print(lines[0][:-1])
    for line in lines[1:len(lines)]:
        if line.startswith('>'):
            print(''.join(seq)[:-quantity])
            seq = list()
            print(line[:-1])
        else:
            seq.append(line[:-1])
    print(''.join(seq)[:-quantity])
    print("\n")
    fh.close()

def __main__():
    truncate(sys.argv[1], int(sys.argv[2]))

if __main__():
    __main__
