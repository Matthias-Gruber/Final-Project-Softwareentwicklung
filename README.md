# Final-Project-Softwareentwicklung
Final Project WS2019

The following files were edited:

* run.sh
* annotate_cogs.py
* read_members_file.py

The function  missing_taxids(cog, taxids) was not implemented.
 
# Questions:

1. Which genes are universally required for an organism to survive? Being
more precise: Which genes (OGs) occur in at least 99% of all genomes in
the eggNOG5 database in each domain of life, respectively? (The results
should be around 100-300.)
* How many such genes did you identify in each domain? [10 points]

***Archae: 175***

***Bacteria: 123***

***Eukaryota: 273***

* Provide the results as three files (one for each domain) listing the
OGs in sorted order. [15 points]

***Filenames: cogs_archaea_o99.txt cogs_bacteria_o99.txt cogs_eukaryota_o99.txt***

2. Which common bacterial genes occur almost exclusively as single-copy
genes? Being more precise: Which OGs occur in at least 50% of all bacterial
genomes, and in at least 99% thereof as single-copy?

***73***

* Provide the results as a sorted text file. [15 points]

***Filename: cogs_bacteria_o50_u99.txt***

* How many of these OGs were also identified as universal bacterial OGs
(previous question)? [10 points]

***40***

***Filename: cogs_universal_bacteria_o50_u99.txt***

3. Identify all OGs that occur as single-copy in at least 97% of all Archaea.
* How many such OGs did you identify? Provide the result as a sorted
text file. [10 points]

***121***

***Filename: cogs_archaea_os99.txt***

* It would be interesting to know if there are archaeal genomes which
substantially deviate from this “default” archaeal gene set. Are
there Archaea which lack 4 or more of these universal OGs? Which
organism (scientific name) lacks most? [15 points]

***Yes, answer in File.***

***Filename: cogs_archaea_4.txt***

4. Compile an overview of the functional categories of these 121 archaeal
OGs.
* Provide the result as a text file sorted by the number of the functional
categories. [25 points]

***Filename: overview.txt***

5. A clear and transparent project structure (folders: bin, data, doc, results) together with your notes and comments is favorable. [5 bonus points]
