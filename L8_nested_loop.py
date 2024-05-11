rows = int(input("how many row?:"))
column = int(input("how many column?:"))
symbol = input("Enter the special char: ")

for i in range(rows):
    for j in range(column):
        print(symbol, end ="")
    print("#")