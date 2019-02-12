import re

#Python Function that does multiplus string replace in a single pass.
def replace(string, dna_replacement):
    substrings = sorted(dna_replacement, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: dna_replacement[match.group(0)], string)

def to_rna(dna_strand):
	dna_replacement = {"C":"G", "G":"C", "T":"A", "A":"U", "": None}
	dna_strand = replace(dna_strand,dna_replacement)
	
	return dna_strand

	
	