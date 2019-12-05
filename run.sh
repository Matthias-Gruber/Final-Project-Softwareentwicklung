#rm -rf final_project
#clear

# Create folders

mkdir -p final_project && cd final_project
mkdir -p bin data doc results
cp ../annotate_cogs.py bin
cp ../read_members_file.py bin
cp ../project_description.pdf doc
cp ../functional_categories.txt data
cp ../README.md doc

# Permission
chmod +x bin/annotate_cogs.py
chmod +x bin/read_members_file.py

###### Use the eggNOG5.0 database to identify conserved single-copy genes.

### Set variables/file names
# base directory
DATADIR=/mirror/eggnog/eggnog_5.0/per_tax_level/
# members files
bacteria=$DATADIR/2/2_members.tsv.gz
archaea=$DATADIR/2157/2157_members.tsv.gz
eukaryota=$DATADIR/2759/2759_members.tsv.gz
# annotations files
archaea_fct=$DATADIR/2157/2157_annotations.tsv.gz

### 1. Which genes (OGs) occur in at least 99% of all genomes in the eggNOG5 database in each domain of life, respectively?

zcat $bacteria | bin/read_members_file.py -min_occurence 99 > results/cogs_bacteria_o99.txt
zcat $archaea | bin/read_members_file.py -min_occurence 99 > results/cogs_archaea_o99.txt
zcat $eukaryota | bin/read_members_file.py -min_occurence 99 > results/cogs_eukaryota_o99.txt

### 2. Which bacterial genes occur in at least 50% of all bacterial genomes, and in at least 99% thereof as single-copy?

zcat $bacteria | ./bin/read_members_file.py -min_occurence 50 -min_uniqueness 99 > results/cogs_bacteria_o50_u99.txt

# How many of these OGs were also identified as universal bacterial OGs (previous question)?
comm -12 results/cogs_bacteria_o99.txt results/cogs_bacteria_o50_u99.txt > results/cogs_universal_bacteria_o50_u99.txt

### 3. Identify all OGs that occur as single-copy in at least 97% of all archaea

zcat $archaea | ./bin/read_members_file.py -min_occurence_as_singlecopy 97 > results/cogs_archaea_os99.txt
# Are there archaea which lack 4 or more of those universal OGs?
zcat $archaea | ./bin/read_members_file.py -min_occurence_as_singlecopy 97 -missing 4 > results/cogs_archaea_4.txt

### 4. Compile an overview of the functional categories of these 121 archaeal OGs
./bin/annotate_cogs.py results/cogs_archaea_os99.txt
