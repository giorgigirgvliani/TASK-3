numbers = input("input numbers ")
numbers = numbers.strip(" ")
numbers = numbers.split(",")

ArrayNumbers = []

for i in range( len(numbers) ):
    ArrayNumbers.append(int(numbers[i]))

Sum = ArrayNumbers[0]

for i in range (1,len(ArrayNumbers)):

    if( ArrayNumbers[i] == ArrayNumbers[i - 1]):
        break
    Sum = Sum + ArrayNumbers[i]


print(Sum)    