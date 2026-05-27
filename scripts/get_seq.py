# get_seq.py
d = {
    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
}
sequence = ""
with open("data/6XOX_GLP1R_chainR.pdb", "r") as f:
    for line in f:
        if line.startswith("ATOM") and line[12:16].strip() == "CA":
            res = line[17:20].strip()
            sequence += d.get(res, '')
print(sequence)
