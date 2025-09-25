# Dynamic Programming Algorithms for String Comparison

This project contains Python scripts that implement two classic dynamic programming algorithms for string comparison:

1.  **Levenshtein Distance**: Calculates the difference between two strings.
2.  **Needleman-Wunsch**: Performs global sequence alignment.

Both scripts print the dynamic programming tables to the console to visualize the process.

## Algorithms

### Levenshtein Distance

The `levenshtein-distance.py` script calculates the Levenshtein distance between two strings. This distance is the minimum number of single-character edits (insertions, deletions, or substitutions) needed to change one string into the other.

**Example:**

The distance between "intention" and "execution" is 8.

### Needleman–Wunsch

The `meedleman–wunsch.py` script uses the Needleman-Wunsch algorithm to find the best global alignment between two sequences. This is widely used in bioinformatics for aligning protein or nucleotide sequences.

**Example:**

Aligning "BAADDCABDDA" and "BBADCBA" produces an optimal alignment with a score, inserting gaps ('-') to maximize similarity.

## Getting Started

To use these scripts, you can run them directly from your Python environment:

```bash
python levenshtein-distance.py
python meedleman–wunsch.py
```

The scripts will print the results and the DP tables to the console. You can modify the input strings in the `if __name__ == '__main__':` block of each file to test different sequences.
