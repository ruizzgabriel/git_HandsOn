# Sergi Soldevila and Gabriel Ruiz

# Given a DNA or RNA sequence, this code computes the percentage of each nucleotide.
import re

# We ask the user to introduce a sequence, we remove spaces inside the sequence and convert the sequence to uppercase
seq = (
    input("Introduce a DNA/RNA sequence: ")
    .strip()
    .upper()
    .replace(" ", "")
    .replace("\t", "")
    .replace("\n", "")
)

# We check if the sequence includes real nucleotides
if re.search("^[ACGTU]+$", seq):
    if re.search("^[UT]+$", seq):
        # Deal with sequences containing both U and T
        print("This is not a biological sequence, please revise it.")
        # Check if sequence is DNA
    elif re.search("[T]", seq):
        # Compute the percentage of each nucleotide in DNA sequences
        nucleotides = {"A": 0, "C": 0, "G": 0, "T": 0}
        total = len(seq)
        for n in seq:
            nucleotides[n] += 1
        for n in nucleotides:
            percent = nucleotides[n] / total * 100
            print(f"{n}: {percent:.2f}%")
    # Check if sequence is RNA
    elif re.search("[U]", seq):
        # Compute the percentage of each nucleotide in RNA sequences
        nucleotides = {"A": 0, "C": 0, "G": 0, "U": 0}
        total = len(seq)
        for n in seq:
            nucleotides[n] += 1
        for n in nucleotides:
            percent = nucleotides[n] / total * 100
            print(f"{n}: {percent:.2f}%")
    else:
        # Deal with sequences only containing ACG.
        print("This sequence can be both DNA and RNA")
else:
    print("This is not a biological sequence, please revise it.")
