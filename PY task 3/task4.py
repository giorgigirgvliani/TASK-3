numbers = input("input numbers ")
numbers = numbers.replace("[", "").replace("]", "").replace(" ","").replace('"',"").split(",")


ArrayNumbers = []

for i in (numbers):
    ArrayNumbers.append(int(i))


for i in range (len(ArrayNumbers)-1):
    ArrayNumbers[i] = ArrayNumbers[i] + ArrayNumbers[i + 1]

ArrayNumbers.pop()
print(ArrayNumbers)