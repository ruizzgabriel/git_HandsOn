# Import necessary modules
import sys, re
from argparse import ArgumentParser

# Create an argument parser object
parser = ArgumentParser(description="Classify a sequence as DNA or RNA")

# Add arguments to the parser
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# If no arguments are provided, print the help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the arguments
args = parser.parse_args()

# Convert the sequence to upper case
args.seq = args.seq.upper()

# Check if the sequence is DNA or RNA
# First condition: assess that the sequence contains nucleotides
if re.search("^[ACGTU]+$", args.seq):
    # If the sequence has "T" and it does not contain "U", it is DNA
    if re.search("^[^U]+$", args.seq) and re.search("T", args.seq):
        print("The sequence is DNA")
    # If the sequence has "U" and no "T", it is RNA
    elif re.search("^[^T]+$", args.seq) and re.search("U", args.seq):
        print("The sequence is RNA")
    # If the sequence does not contain "T" nor "U", the sequence can be DNA or RNA
    elif re.search("^[^T]+$", args.seq) and re.search("^[^U]+$", args.seq):
        print("The sequence can be DNA or RNA")
    # If the sequence is not following any of the previous conditions, the sequence is a DNA/RNA mix
    else:
        print("You introduced a RNA/DNA mix, that is not possible.")
# If the sequence contains a letter that does not correspond to nucleotide code, it is not DNA nor RNA.
else:
    print("The sequence is not DNA nor RNA")

# If a motif is provided, search for it in the sequence
if args.motif:
    # Convert the motif to upper case
    args.motif = args.motif.upper()
    print(
        f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ',
        end="",
    )
    if re.search(args.motif, args.seq):
        print("It is found")
    else:
        print("It is not found")

# Count the number of each nucleotide in the sequence
nucleotide_counts = {
    "A": args.seq.count("A"),
    "C": args.seq.count("C"),
    "G": args.seq.count("G"),
    "T": args.seq.count("T"),
    "U": args.seq.count("U")
}

# Calculate the total length of the sequence
seq_length = len(args.seq)

# Calculate the percentage of each nucleotide in the sequence
nucleotide_percentages = {
    k: (v / seq_length) * 100 for k, v in nucleotide_counts.items()
}

# Print the percentage of each nucleotide
print("Percentage of each nucleotide:")
for k, v in nucleotide_percentages.items():
    print(f"{k}: {v:.2f}%")

