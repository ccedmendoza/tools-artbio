#!/usr/bin/python
# python parser module to analyse sRbowtie alignments
# version 1.0.0 - argparse implementation
# Usage sRbowtieParser.py  <1:index source> <2:extraction directive> <3:outputL> <4:polarity> <5:6:7 filePath:FileExt:FileLabel> <.. ad  lib>

import sys, argparse
from smRtools import *

def Parser():
  the_parser = argparse.ArgumentParser()
  the_parser.add_argument('--IndexSource', action="store", type=str, help="Path to the index source")
  the_parser.add_argument('--ExtractDirective', action="store", type=str, choices=["fastaSource", "bowtieIndex"], help="Extract info from fasta or bowtie index")
  the_parser.add_argument('--output', action="store", type=str, help="path to the output")
  the_parser.add_argument('--polarity', choices=["forward", "reverse", "both"], help="forward, reverse or both forward an reverse reads are counted")
  the_parser.add_argument('--alignmentSource',nargs='+', help="paths to alignments files")
  the_parser.add_argument('--alignmentFormat',nargs='+', help="Format of the bowtie alignment (tabular, sam or bam)")
  the_parser.add_argument('--alignmentLabel',nargs='+', help="Label of the alignment")
  args = the_parser.parse_args()
  return args

args = Parser()

IndexSource = args.IndexSource
genomeRefFormat = args.ExtractDirective
Output = args.output
Polarity = args.polarity
MasterListOfGenomes = {}

for filePath, FileExt, FileLabel in zip (args.alignmentSource, args.alignmentFormat, args.alignmentLabel):
  MasterListOfGenomes[FileLabel] = HandleSmRNAwindows (filePath, FileExt, IndexSource, genomeRefFormat) 

header = ["gene"]
for filePath, FileExt, FileLabel in zip (args.alignmentSource, args.alignmentFormat, args.alignmentLabel):
  header.append(FileLabel)

F = open (args.output, "w")
# print >>F, args
print >> F, "\t".join(header)
for item in sorted (MasterListOfGenomes[header[1]].instanceDict.keys() ):
  line=[item]
  for sample in header[1:]:
    count = str (MasterListOfGenomes[sample].instanceDict[item].readcount(polarity=Polarity))
    line.append(count)
  print >> F,  "\t".join(line )
F.close()