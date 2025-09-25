from tabulate import tabulate

def edit_distance(source: str, target: str) -> int:
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is a string metric for measuring the difference
    between two sequences. Informally, the Levenshtein distance between two
    words is the minimum number of single-character edits (insertions,
    deletions or substitutions) required to change one word into the other.

    This implementation uses dynamic programming to compute the distance.
    It also prints the DP table for visualization.

    Args:
        source: The source string.
        target: The target string.

    Returns:
        The Levenshtein distance between the source and target strings.
    """
    sl, tl = len(source), len(target)

    # Create DP table
    cost = [[0] * (tl + 1) for _ in range(sl + 1)]

    # Initialize
    for i in range(1, sl + 1):
        cost[i][0] = i  # deletions
    for j in range(1, tl + 1):
        cost[0][j] = j  # insertions

    # Fill table
    for i in range(1, sl + 1):
        for j in range(1, tl + 1):
            if source[i - 1] == target[j - 1] and abs(i - j) < 2:
                cost[i][j] = cost[i - 1][j - 1]  # no cost if same
            else:
                deletion = cost[i - 1][j] + 1
                insertion = cost[i][j - 1] + 1
                replacement = cost[i - 1][j - 1] + 2
                cost[i][j] = min(
                    deletion,      # deletion
                    insertion,      # insertion
                    replacement   # replacement (cost 2)
                )

    # Traceback path
    # i, j = sl, tl
    # path = set()
    # while i > 0 or j > 0:
    #     path.add((i, j))
    #     if i > 0 and cost[i][j] == cost[i - 1][j] + 1:
    #         i -= 1  # deletion
    #     elif j > 0 and cost[i][j] == cost[i][j - 1] + 1:
    #         j -= 1  # insertion
    #     else:
    #         i -= 1
    #         j -= 1  # match or replace
    # path.add((0, 0))

    # Build table for printing
    table = []
    header = [" "] + [" "] + list(target)  # top row: blank + target chars
    table.append(header)

    for i in range(sl + 1):
        row_label = " " if i == 0 else source[i - 1]
        row = [row_label] + cost[i]
    #     row = [row_label]
    #     for j in range(tl + 1):
    #         val = str(cost[i][j])
    #         if (i, j) in path:
    #             val = f"*{val}*"   # mark path
    #         row.append(val)
        table.append(row)

    print(f"\nDP Grid (rows={sl}, cols={tl}): source = {source}, target = {target}")
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

    return cost[sl][tl]


# distance = edit_distance("kitten", "sitting")
# print("\nEdit distance:", distance)
# print()

# distance = edit_distance("intention", "execution")
# print("\nEdit distance:", distance)
# print()

# distance = edit_distance("tarp", "star")
# print("\nEdit distance:", distance)
# print()

distance = edit_distance("earth", "pearl")
print("\nEdit distance:", distance)
print()

# distance = edit_distance("saxophone", "microphone")
# print("\nEdit distance:", distance)
# print()