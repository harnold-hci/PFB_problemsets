#!usr/bin/env python3

# create dna sequence class
# contains a sequence, its name, it's organism of origin via __init__ fxn

class dnaRecord(object):
    # takes in a sequence, the gene name, and the species
    def __init__(self, sequence, gene_name, species):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species = species
    # returns the length of the sequence
    def seq_len(self):
        return len(self.sequence)
    # returns the nucleotide composition of the sequence in a % 
    def nuc_comp(self):
        counter= {}
        for base in self.sequence:
            if base not in counter:
                counter[base] = 1
            else:
                counter[base] += 1
        return counter
    # returns the gc content of the sequence
    def gc_content(self):
        bases = self.nuc_comp()
        return((bases['C'] + bases['G']) / self.seq_len())
    # returns the sequence in FASTA format
    def fasta_format(self):
        return(f'>{self.gene_name}\t{self.species}\n{self.sequence}')

# main script
# initialize the dna object
dna1 = dnaRecord('ATCG', 'NKX2-1', 'mus')
# print the sequence, gene name, and species
print(dna1.sequence)
print(dna1.gene_name)
print(dna1.species)
# print the length of the sequence
print(dna1.seq_len())
# print the nucleotide composition of the sequence
comp_dict = dna1.nuc_comp()
for base in comp_dict:
    print(f'{base}: {(comp_dict[base] / dna1.seq_len()):.2%}')
# print the gc content of the sequence
print(f'{dna1.gc_content():.2%}')
# print the sequence in fasta format
print(dna1.fasta_format())



# challenge:
'''
Create a method that can compare two DNA Sequence records and returns True if they are the 
same or False if they are differet. Sameness is based on name, organism, and seqeunce. 
All need to be the same for two objects to be considered the same.'''

def compare_records(rec1, rec2):
    if rec1.sequence == rec2.sequence:
        if rec1.gene_name == rec2.gene_name:
            if rec1.species == rec2.species:
                return True
    else:
        return False

dna2 = dnaRecord('ATCG', 'NKX2-1', 'mus')
dna3 = dnaRecord('ATCGA', 'NKX2-1', 'mus')
dna4 = dnaRecord('ATCGA', 'NKX2-2', 'mus')
dna5 = dnaRecord('ATCGA', 'NKX2-1', 'homo')

print(compare_records(dna1, dna5))