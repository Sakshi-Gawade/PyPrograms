
values = [10,20,30,40]

print(values)

print(type(values))

print(len(values))  #len gives number of elements

values.insert(2,11)

print("Data after insert:",values) #insert elements at perticular index

values.insert(15,89)

print("Size of list is now:",len(values))
print("Data after insert 15 is:",)

print(values[0])
print(values[1])
print(values[2])
print(values[3])

values.append(50)   #add element in list

print(values)

values.remove(20)

print(values)

values.append(50)

print(values)

print(type(values[0]))

values.append(90.89)

print(values)


