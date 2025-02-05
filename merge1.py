# marks  = [1,2,3]

# def pairing(marks):
#     new = []
#     for i in range(len(marks)):
#         for j in range(i+1,len(marks)):
#             new.append((marks[i],marks[j]))
#     return new


# print(pairing(marks))


def pal(num):
   return str(num) == str(num)[::-1]

num = 121
print(pal(num))