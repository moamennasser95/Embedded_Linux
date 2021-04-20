
Pyramid_height = int(input("Please enter pyramid height: "))
spaces = 0
asterisks = 0

for height in range(Pyramid_height):
        
    spaces = (Pyramid_height - 1) - height

    for i in range(spaces):
        print(" ",end=" ")

    asterisks = (height * 2) + 1

    for i in range(asterisks):
        print("*", end=" ")

    for i in range(spaces):
        print(" ", end=" ")

    print("\n")