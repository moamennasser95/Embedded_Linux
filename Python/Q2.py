
Num = int(input("Please enter any number: "))
Sum = 0
Avg = 0

for i in range(Num):  
    Sum += i+1

Avg = float(Sum) / Num

print("The Sum of Natural Numbers from 1 to {} = {}".format(Num, Sum))

print("The Average of natural numbers from 1 to {} = {}".format(Num, Avg))