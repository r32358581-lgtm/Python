number = int(input("Enter a number of rows: "))

for i in range(1, number + 1):
    print(" "*(number-i) + "*"*(2*i-1))