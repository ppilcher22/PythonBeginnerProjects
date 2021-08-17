lst = [7, 4, 0, 5, 1, 8, 4, 2, 3, 10, 1]
pivot_points = []

i = len(lst) // 2
pivot_points.insert(0, i)

while i > 1:
    i = i // 2
    pivot_points.append(i)

print(pivot_points)

