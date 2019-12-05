#!/usr/bin/env python

import sys, gzip
from collections import Counter

func_categories_file = 'data/functional_categories.txt'
cog_file = sys.argv[1]
func_file = "/mirror/eggnog/eggnog_5.0/per_tax_level/2157/2157_annotations.tsv.gz"

# Initialize variables
category2description = {}
cog2category = {}
category2count = Counter()
my_cogs = set()

# Step 1: Read description of functional categories
with open(func_categories_file) as fin:
    for line in fin:
        line = line.split(" ")
        if line[0] == "":
            key = line[1][1]
            val = " ".join(line[2:-1])
            category2description[key] = val

# Step 2: Read file with OGs of interest
with open(cog_file) as fin:
    for line in skip_comments(fin):
        print(line)

# Step 3: Read file with functional annotations
input = gzip.GzipFile(func_file,'rb')
i = input.read()
j = i.decode("utf-8") 
print(j)
input.close()

# Step 4: Count and output the categories for OGs of interest
# Write file categories.txt
