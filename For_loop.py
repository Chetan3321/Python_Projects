list = [4, 3, 2, 6, 7]
for i in range(0, len(list)):
    print(i)
print(list)

l1 = [3, 6, 7, 8, 9]
l2 = []
for i in l1:
    if i == 8:
        break
    l2.append(i)
print(l2)