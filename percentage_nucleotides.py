# Sergi Soldevila and Gabriel Ruiz

# Given a DNA or RNA sequence, this code computes the percentage of each nucleotide.
import re
# We ask the user to introduce a sequence, we remove spaces inside the sequence and convert the sequence to uppercase
seq = input("Introduce a DNA/RNA sequence: ").strip().upper().replace(" ","").replace("\t","").replace("\n", "")

# We check if the sequence includes real nucleotides
if re.search("^[ACGTU]+$", seq):
    print("Here, my classmate will perform the percentage computation...")
else:
    print("This is not a biological sequence, please revise it.")

