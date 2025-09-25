from tabulate import tabulate

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

    # Build grid for printing
    table = []
    header = [" "] + [" "] + list(target)  # top row: blank + target chars
    table.append(header)

    for i in range(sl + 1):
        row_label = " " if i == 0 else source[i - 1]
        row = [row_label] + cost[i]
        table.append(row)

    print(f"\nDP Grid (rows={sl}, cols={tl}): source = {source}, target = {target}")
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

    return cost[sl][tl]


distance = edit_distance("kitten", "sitting")
print("\nEdit distance:", distance)
print()


distance = edit_distance("intention", "execution")
print("\nEdit distance:", distance)
print()
