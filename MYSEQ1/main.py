import re
from seqMan import reverseSeq, complementSeq, reverseComplementSeq, dna2rna, dna2protein, gcContent, countBasesDict, enzTargetsScan

def main():
    seq = 'ATGGGCCGTAGAATTCTTGCAAGCCCGT'
    seq = seq.upper()
    print(f"Original Sequence: {seq}")
    print("Transcription: ", dna2rna(seq))
    print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    print("Translation: ", dna2protein(seq))
    print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    print("GC Content:", gcContent(seq))
    print("Count Bases: ", countBasesDict(seq))
    print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

if __name__ == "__main__":
    main()
