
number = int(input("input your number: "))
highestnumber = 100000000000000000000000000000000000000000000

while( True ):

    if( highestnumber // 10 <= number ):
        break
    highestnumber = highestnumber // 10

NewNumber = 0
highestnumber = highestnumber // 10

while( highestnumber > 0):
     NewNumber = NewNumber + number % 10 * highestnumber
     number = number // 10
     highestnumber = highestnumber // 10
   
print(NewNumber)