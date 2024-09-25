import argparse
from seqbio.calculation.SeqCal import *
from seqbio.seqMan.dnaconvert import *
from seqbio.pattern.SeqPattern import *

def main():
    parser = argparse.ArgumentParser(prog='myseq', description='Work with sequence')
    subparsers = parser.add_subparsers(dest='command')

    parser_gc = subparsers.add_parser('gcContent', help='Calculate GC content')
    parser_gc.add_argument('-s', '--seq', type=str, help='Provide sequence', required=True)

    parser_count = subparsers.add_parser('countBases', help='Count number of each base')
    parser_count.add_argument('-s', '--seq', type=str, help='Provide sequence', required=True)
    parser_count.add_argument('-r', '--revcomp', action='store_true', help='Convert DNA to reverse-complementary')

    parser_transcription = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    parser_transcription.add_argument('-s', '--seq', type=str, help='Provide sequence', required=True)
    parser_transcription.add_argument('-r', '--revcomp', action='store_true', help='Convert DNA to reverse-complementary')

    parser_translation = subparsers.add_parser('translation', help='Convert DNA->Protein')
    parser_translation.add_argument('-s', '--seq', type=str, help='Provide sequence', required=True)
    parser_translation.add_argument('-r', '--revcomp', action='store_true', help='Convert DNA to reverse-complementary')

    parser_enzyme = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    parser_enzyme.add_argument('-s', '--seq', type=str, help='Provide sequence', required=True)
    parser_enzyme.add_argument('-e', '--enz', type=str, help='Enzyme name', required=True)
    parser_enzyme.add_argument('-r', '--revcomp', action='store_true', help='Convert DNA to reverse-complementary')

    args = parser.parse_args()

    if args.command == 'gcContent':
        print(f"Input {args.seq}")
        print(f"GC content = {gcContent(args.seq)}")

    elif args.command == 'countBases':
        seq_to_use = args.seq
        if args.revcomp:
            seq_to_use = reverseComplementSeq(seq_to_use)
        print(f"Input {args.seq}")
        print(f"countBases = {countBases(seq_to_use)}")

    elif args.command == 'transcription':
        seq_to_use = args.seq
        if args.revcomp:
            seq_to_use = reverseComplementSeq(seq_to_use)
        print(f"Input {args.seq}")
        print(f"Transcription = {dna2rna(seq_to_use)}")

    elif args.command == 'translation':
        seq_to_use = args.seq
        if args.revcomp:
            seq_to_use = reverseComplementSeq(seq_to_use)
        print(f"Input {args.seq}")
        print(f"Translation = {dna2protein(seq_to_use)}")

    elif args.command == 'enzTargetsScan':
        seq_to_use = args.seq
        if args.revcomp:
            seq_to_use = reverseComplementSeq(seq_to_use)
        print(f"Input {args.seq}")
        print(f"{args.enz} sites = {enzTargetsScan(seq_to_use, args.enz)}")

if __name__ == "__main__":
    main()