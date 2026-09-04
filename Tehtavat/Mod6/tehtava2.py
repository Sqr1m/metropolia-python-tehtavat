a = input("Anna lukuja: ")
b = []
while a != "":
    b.append(int(a))

    a = input("Anna lukuja: ")

b.sort(reverse=True)

for i in range(len(b)):
    if i < 5:
        print(b[i])

