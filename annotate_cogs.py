#!/usr/bin/env python

import sys, gzip
from collections import Counter, defaultdict
import pandas as pd

func_categories_file = 'data/functional_categories.txt'
cog_file = sys.argv[1]
func_file = "/mirror/eggnog/eggnog_5.0/per_tax_level/2157/2157_annotations.tsv.gz"

# Initialize variables
category2description = {}
cog2category = {}
category2count = Counter()
my_cogs = set()
cog = []
mycogs2code = defaultdict(int)
cog2cat_count = defaultdict(int)
overview = defaultdict(int)


def skip_comments(file):
    for line in file:
        if not line.strip().startswith('#'):
            yield line
            
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
        cog.append(line.split("\t")[0])

mycogs = set(cog)

# Step 3: Read file with functional annotations
input = gzip.GzipFile(func_file,'rb')
i = input.read()
func_annotations = i.decode("utf-8") 
input.close()

with open("results/annotation.txt", 'w') as fout:
    fout.write(func_annotations)

with open("results/annotation.txt") as fin:
    for line in fin:
        line = line.split("\t")
        key = line[0:-1][1]
        val = line[0:-1][2]
        cog2category[key] = val
        
# Step 4: Count and output the categories for OGs of interest
   
for cog in mycogs:
    if cog != "2157"and cog != "Missing COGs!\n":
        mycogs2code[cog] = cog2category[cog]
        
for entry in mycogs2code:   
    if len(mycogs2code[entry]) == 1:
        cog2cat_count[mycogs2code[entry]] +=1
    else:
        for i in range(len(mycogs2code[entry])):
            cog2cat_count[mycogs2code[entry][i]] +=1

for key in category2description:
    overview[category2description[key]] = cog2cat_count[key]

df = pd.DataFrame.from_dict(overview, orient='index')
df.to_csv("results/overview.csv") 
