print("Demonstration of Tuple")

# Data : Heterogeneous
# ordered : Yes
# Indexed : Yes
# Mutable : no
# Duplicates : Yes

Data = (11, 21, 51, 101)

print("________________________________")
print("Output using for")
for no in Data:
    print(no, end = " ")
print()

print("________________________________")
print("Output using for with index")
for i in range(0, len(Data)):
    print(Data[i], end = " ")
print()

print("________________________________")
print("Output using while with index")
i = 0
while(i < len(Data)):
    print(Data[i], end = " ")
    i+=1
print()

