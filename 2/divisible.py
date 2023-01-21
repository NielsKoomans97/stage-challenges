xnum = int(input("X > "))
ynum = int(input("Y > "))

for i in range(0,100):
    if i % xnum == 0:
        print("F")    
    elif i % ynum == 0:
        print("B")
    else:
        print(f"{i}")
    