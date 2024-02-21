x = [4, 0, 1, 0, 1]

mylist = []
people = x[0]
count = 0
for i in x:
    if x == 0:
        continue
    else:
        mylist.append(i)

print(mylist)

number = people/2
loop = 0
for i in range(len(mylist)):
    opposite = abs(i-2)
    loop+=1
    if mylist[i] == mylist[opposite]:
        count+=1
    if loop==number:
        print(count)
print(count)

