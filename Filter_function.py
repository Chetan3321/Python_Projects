#filter function

a = [5,3,4,6,7,8]

def myfun(x):
    if x%2 == 0:
        return x

even = filter(myfun,a)

for i in even:
    print(i)
    