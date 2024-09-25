def countBase(seq, base):  
    return seq.count(base)

def gcContent(seq): 
    g_count = countBase(seq, "G")
    c_count = countBase(seq, "C")
    total_bases = len(seq)
    return (g_count + c_count) / total_bases * 100

def atContent(seq):
    a_count = countBase(seq, "A")
    t_count = countBase(seq, "T")
    total_bases = len(seq)
    return (a_count + t_count) / total_bases * 100

def countBasesDict(seq):  
    basesM = {base: seq.count(base) for base in "ATGC"}
    return basesM