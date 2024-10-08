import re
def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG', seq, re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

def enzTargetsScan(seq, enz):
    resEnzyme = dict(EcoRI='GAATTC', BamHI='GGATCC', 
                     HindIII='AAGCTT', AccB2I='[AG]GCGC[CT]',
                     AasI='GAC[ATCG]{6}GTC', AceI='GC[AT]GC')

    out = []
    if enz in resEnzyme:
        pattern = resEnzyme[enz]
        for m in re.finditer(pattern, seq):
            out.append((m.group(), m.start(), m.end()))
    return out