ArrayNumbers = []
Number = int ( input( "input the number: " ) )
ArrayNumbers.append(Number)
Sum = Number

while(True):
    Number = int ( input( "input the number: " ) )
    Sum = Sum + Number
    ArrayNumbers.append(Number)

    if( ArrayNumbers[ len(ArrayNumbers) - 1] ==  ArrayNumbers[ len(ArrayNumbers ) - 2] ):
        break

print(Sum - Number)    



