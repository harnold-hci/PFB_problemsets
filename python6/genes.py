#!usr/bin/env python3

all_set = set()
pig_set = set()
stem_set = set()
with open('./ferret_all_genes.tsv') as all_genes, open ('./ferret_pigmentation_genes.tsv') as pig_genes, open('./ferret_stemcellproliferation_genes.tsv') as stem_genes:
    for line in all_genes:
        if line.startswith('E'):
        	line = line.rstrip()
        	all_set.add(line)
    for line in pig_genes:
        if line.startswith('E'):
        	line = line.rstrip()
        	pig_set.add(line)
    for line in stem_genes:
        if line.startswith('E'):
        	line = line.rstrip()
        	stem_set.add(line)
print(f'len all: {len(all_set)}, len pig: {len(pig_set)}, len stem: {len(stem_set)}')

# find all genes that are NOT stem genes

not_stem = (all_set | pig_set) - stem_set
# 31991 genes are NOT stem genes
print(len(not_stem))

#both stem cell genes AND pigment genes:
stem_and_pig = pig_set | stem_set
# 98 are both genes
print(len(stem_and_pig))

tf_set = set()
with open('./ferret_transcriptionFactors.tsv') as tfs:
	for line in tfs:
		line = line.rstrip()
		if line.startswith('E'):
			tf_set.add(line)

tf_prolif = tf_set & stem_set

print(f'tf set: {len(tf_set)}')
print(f'tf_prolif: {len(tf_prolif)}')