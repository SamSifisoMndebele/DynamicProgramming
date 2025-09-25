from tabulate import tabulate

def string_alignment(seq1, seq2):
    """
    Performs string alignment using the Needleman-Wunsch algorithm.

    This function calculates the optimal alignment between two sequences
    (strings) by minimizing the edit distance. It uses dynamic programming
    to fill a score matrix and then traces back to find the alignment.

    The costs are defined as:
    - Match: 0
    - Mismatch: 2
    - Insertion/Deletion (gap): 1

    Args:
        seq1 (str): The first sequence.
        seq2 (str): The second sequence.

    Returns:
        tuple: A tuple containing:
            - score (int): The alignment score (minimum edit distance).
            - align1 (str): The first sequence with gaps inserted.
            - align2 (str): The second sequence with gaps inserted.
    """
    n, m = len(seq1), len(seq2)

    # Initialize DP table
    score = [[0] * (m + 1) for _ in range(n + 1)]
    traceback = [[None] * (m + 1) for _ in range(n + 1)]

    # First row & col initialization (+1 per step)
    for i in range(1, n + 1):
        score[i][0] = i
        traceback[i][0] = "up"
    for j in range(1, m + 1):
        score[0][j] = j
        traceback[0][j] = "left"

    # Fill DP table (forward stage)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost_diag = 0 if seq1[i-1] == seq2[j-1] else 2
            diag = score[i-1][j-1] + cost_diag
            up = score[i-1][j] + 1   # row shift
            left = score[i][j-1] + 1 # col insert

            score[i][j] = min(diag, up, left)

            if score[i][j] == diag:
                traceback[i][j] = "diag"
            elif score[i][j] == up:
                traceback[i][j] = "up"
            else:
                traceback[i][j] = "left"

    # Print Forward DP Grid
    table_forward = [[" "] + [" "] + list(seq2)]
    for i in range(n + 1):
        row_label = " " if i == 0 else seq1[i - 1]
        row = [row_label] + score[i]
        table_forward.append(row)

    print("\nForward DP Grid (Filled Costs):")
    print(tabulate(table_forward, headers="firstrow", tablefmt="grid"))


    # Traceback to build alignment
    align1 = []
    align2 = []
    path = set()
    i, j = n, m
    while i > 0 or j > 0:
        path.add((i, j))
        if traceback[i][j] == "diag":
            align1.append(seq1[i-1])
            align2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif traceback[i][j] == "up":
            align1.append(seq1[i-1])
            align2.append("-")
            i -= 1
        else:  # left
            align1.append("-")
            align2.append(seq2[j-1])
            j -= 1
    path.add((0, 0))

    align1.reverse()
    align2.reverse()

    # Print Backward Grid (traceback path)
    table_back = [[" "] + [" "] + list(seq2)]
    for i in range(n + 1):
        row_label = " " if i == 0 else seq1[i - 1]
        row = [row_label]
        for j in range(m + 1):
            val = str(score[i][j])
            if (i, j) in path:
                val = f"*{val}*"
            row.append(val)
        table_back.append(row)

    print("\nBackward DP Grid (Traceback Path):")
    print(tabulate(table_back, headers="firstrow", tablefmt="grid"))

    return score[n][m], ''.join(align1), ''.join(align2)


# Textbook Example
seq1 = "BAADDCABDDA"
seq2 = "BBADCBA"

score, align1, align2 = string_alignment(seq2, seq1)
print("\nAlignment Score:", score)
print("Align1:", align1)
print("Align2:", align2)
