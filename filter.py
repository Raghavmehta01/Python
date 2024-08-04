a = int(input("Enter number:\n"))

nl =[]
for i in range(a):
    nl.append(i)
def fn(a):
    return a>2
nnl = list(filter(fn,nl))
print(nnl)