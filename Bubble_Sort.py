lst = [7, 4, 0, 4, 1, 7, 4, 1, 1, 10, 9, 4, 8, 10, 6, 9, 4, 9, 4, 2]


#bubble sort
sort_occured = False
sort_count = 0

while True:
    sort_occured = False
    for x in range(len(lst) - 1):
        if lst[x] > lst[x + 1]:
            lst[x], lst[x + 1] = lst[x+1], lst[x]
            sort_occured = True
            sort_count += 1
    if not sort_occured:
        break

print(lst)
print(F"Sort count {sort_count}")

