num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
row = [1]

for i in range(num_rows):
    print(' '.join(map(str, row)).center(num_rows * 2))
    next_row = [1]
    for j in range(len(row) - 1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)

    row = next_row
