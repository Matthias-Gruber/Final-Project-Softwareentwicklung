#!/usr/bin/env python

import sys
from collections import Counter

func_categories_file = 'functional_categories.txt'

cog_file = sys.argv[1]
func_file = sys.stdin #sys.argv[2]

# Initialize variables
category2description = {}
cog2category = {}
category2count = Counter()
my_cogs = set()


# Step 1: Read description of functional categories
with open(func_categories_file) as fin:
    pass


# Step 2: Read file with OGs of interest
with open(cog_file) as fin:
    pass


# Step 3: Read file with functional annotations
#with open(func_file) as fin:
for line in func_file:
    pass


# Step 4: Count and output the categories for OGs of interest
