from Bio.Seq import Seq
from Bio.Data import CodonTable
import time

start = time.time()

# 1. get sequence
filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\biopython\\NC_045512.2.fasta"
seq = ""
with open(filepath) as handle:
    _ = handle.readline()
    for line in handle:
        seq += line
print(seq[:30])

# 2. Complimentart allele
seq = Seq(seq)
seq_comp = seq.complement()
print(seq_comp[:30])

# 3. DNA to RNA
seq_RNA = seq_comp.transcribe()
print(seq_RNA[:30])

# 4. RNA to protein
standrd_table = CodonTable.unambiguous_dna_by_name["Standard"]
print(standrd_table)

protein = seq_RNA[:30].translate()
print(protein)

end = time.time()
print(end - start)
