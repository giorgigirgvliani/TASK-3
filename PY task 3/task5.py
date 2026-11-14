

numbers = input("input numbers ")
numbers = numbers.replace("(", "").replace(")", "").replace(" ","").replace('"',"").split(",")


ArrayNumbers = ()
ArrayNumbersFake = ()

for i in (numbers):
    ArrayNumbers = (*ArrayNumbers, + int(i))
    if( int(i) not in ArrayNumbersFake ):
        ArrayNumbersFake = (*ArrayNumbersFake, + int(i))

counter = 0
number = 0

for i in (ArrayNumbersFake):
    if( ArrayNumbers.count(i) > counter ):
        counter = ArrayNumbers.count(i)
        number = i


ind = ArrayNumbers.index(number)      
print(ArrayNumbers[ind])