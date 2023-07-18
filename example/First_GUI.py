import tkinter as tk
from tkinter import filedialog, ttk

def revSeq(seq):
    data1=seq[::-1]
    compDic={'A':'T','C':'G','G':'C','T':'A'}
    result=""
    for i in data1:
        result += compDic[i]
    return result

def DNAtoRNA(data):
    Seq_RNA=data.replace("T","U")
    return Seq_RNA

Codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
        'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W',
    }

def RNAtoProtein(data):
    protein =""
    if len(data)%3 == 0:
        for i in range(0, len(data), 3):
            codon = data[i:i + 3]
            protein+= Codon_table[codon]
    return protein

def main():
    root = tk.Tk()
    root.title("DNA to Protein Converter")
    root.geometry("500x300")  # Window size
    root.configure(bg='green')

    # Styling
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), background="blue")
    style.configure("TLabel", font=("Arial", 12))

    # Input field and button
    seq_entry = ttk.Entry(root, width=50, font=("Arial", 12))
    seq_entry.pack(pady=20)
    convert_button = ttk.Button(root, text="Convert", command=lambda: convert(seq_entry.get()))
    convert_button.pack()

    # Label for results
    global result_label
    result_label = ttk.Label(root, text="")
    result_label.pack(pady=20)

    root.mainloop()

def convert(seq):
    revComp_result = revSeq(seq)
    RNA_result = DNAtoRNA(seq)
    Protein_result = RNAtoProtein(RNA_result)

    # Display results in label
    result_label.config(text=f"Sequence: {seq}\nComplementary Sequence: {revComp_result}\nRNA Sequence: {RNA_result}\nProtein Sequence: {Protein_result}")

    # Save results to file
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    with open(file_name, "w") as file_result:
        file_result.write(f"Sequence: {seq}\nComplementary Sequence: {revComp_result}\nRNA Sequence: {RNA_result}\nProtein Sequence: {Protein_result}")

main()

