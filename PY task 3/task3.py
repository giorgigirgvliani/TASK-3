Words = input("write your words here: ")

Words1 = Words.replace("[","").replace("]"," ").replace(" ","").replace('"',"").split(",")

xmovnebi = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
ArrayForXmovnebi = []

for i in Words1:
    sum = 0
    print(i)
    for index in range( len(xmovnebi)):
        sum = sum + i.count(xmovnebi[index])
    ArrayForXmovnebi.append(sum) 


print(ArrayForXmovnebi)