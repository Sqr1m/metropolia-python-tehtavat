a = []
while True:
    b = (input("Anna numero: "))
    if b == "":
        print(f"Max: {max(a)}, Min: {min(a)}")
        break
    a.append(int(b))
    
   