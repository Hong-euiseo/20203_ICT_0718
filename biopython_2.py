import time

start = time.time()
# 1. get sequence data
filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\biopython\\NC_045512.2.fasta"
seq = ""
with open(filepath) as handle:
    _ = handle.readline()
    for line in handle:
        seq += line

my_seq = seq[:30]
print(f"SEQUENCE : {my_seq}")

# 2. complementary sequence
my_seq_comp = ""
for i in my_seq:
    if i == "A":
        my_seq_comp += "T"
    elif i == "T":
        my_seq_comp += "A"
    elif i == "G":
        my_seq_comp += "C"
    elif i == "C":
        my_seq_comp += "G"
print(f"COMPLEMENTARY SEQUENCE : {my_seq_comp}")

# 3. DNA to RNA
my_seq_comp_rna = ""
for i in my_seq_comp:
    if i == "T":
        my_seq_comp_rna += "U"
    else:
        my_seq_comp_rna += i
print(f"COMPLEMENTART RNA SEQUENCE : {my_seq_comp_rna}")

# 4. Coding protein
codontab = {
    "TCA": "S",  # Serina
    "TCC": "S",  # Serina
    "TCG": "S",  # Serina
    "TCT": "S",  # Serina
    "TTC": "F",  # Fenilalanina
    "TTT": "F",  # Fenilalanina
    "TTA": "L",  # Leucina
    "TTG": "L",  # Leucina
    "TAC": "Y",  # Tirosina
    "TAT": "Y",  # Tirosina
    "TAA": "*",  # Stop
    "TAG": "*",  # Stop
    "TGC": "C",  # Cisteina
    "TGT": "C",  # Cisteina
    "TGA": "*",  # Stop
    "TGG": "W",  # Triptofano
    "CTA": "L",  # Leucina
    "CTC": "L",  # Leucina
    "CTG": "L",  # Leucina
    "CTT": "L",  # Leucina
    "CCA": "P",  # Prolina
    "CCC": "P",  # Prolina
    "CCG": "P",  # Prolina
    "CCT": "P",  # Prolina
    "CAC": "H",  # Histidina
    "CAT": "H",  # Histidina
    "CAA": "Q",  # Glutamina
    "CAG": "Q",  # Glutamina
    "CGA": "R",  # Arginina
    "CGC": "R",  # Arginina
    "CGG": "R",  # Arginina
    "CGT": "R",  # Arginina
    "ATA": "I",  # Isoleucina
    "ATC": "I",  # Isoleucina
    "ATT": "I",  # Isoleucina
    "ATG": "M",  # Methionina
    "ACA": "T",  # Treonina
    "ACC": "T",  # Treonina
    "ACG": "T",  # Treonina
    "ACT": "T",  # Treonina
    "AAC": "N",  # Asparagina
    "AAT": "N",  # Asparagina
    "AAA": "K",  # Lisina
    "AAG": "K",  # Lisina
    "AGC": "S",  # Serina
    "AGT": "S",  # Serina
    "AGA": "R",  # Arginina
    "AGG": "R",  # Arginina
    "GTA": "V",  # Valina
    "GTC": "V",  # Valina
    "GTG": "V",  # Valina
    "GTT": "V",  # Valina
    "GCA": "A",  # Alanina
    "GCC": "A",  # Alanina
    "GCG": "A",  # Alanina
    "GCT": "A",  # Alanina
    "GAC": "D",  # Acido Aspartico
    "GAT": "D",  # Acido Aspartico
    "GAA": "E",  # Acido Glutamico
    "GAG": "E",  # Acido Glutamico
    "GGA": "G",  # Glicina
    "GGC": "G",  # Glicina
    "GGG": "G",  # Glicina
    "GGT": "G",  # Glicina
}
protein = ""
for i in range(0, len(my_seq_comp), 3):
    value = my_seq_comp[i : i + 3]
    protein += codontab[value]
print(f"PROTEIN : {protein}")

end = time.time()
print(f"time : {end - start}")
