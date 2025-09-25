def edit_distance(source: str, target: str) -> int:
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
            if source[i - 1] == target[j - 1]:
                cost[i][j] = cost[i - 1][j - 1]  # no cost if same
            else:
                cost[i][j] = min(
                    cost[i - 1][j] + 1,      # deletion
                    cost[i][j - 1] + 1,      # insertion
                    cost[i - 1][j - 1] + 2   # replacement (cost 2)
                )

    return cost[sl][tl]


# Example
print(edit_distance("kitten", "sitting"))  # Output: 5
print(edit_distance("intention", "execution"))  # Output: 8
