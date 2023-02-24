Batches = {"PPA":18000, "LB":16700, "Python":16500, "Angular":15000}

print("Data of dictionary :", Batches)

print("____________________________________")
print("Data traversal using for loop")
for x in Batches:
    print(x)

print("____________________________________")
print("Data traversal using for loop")
for x in Batches:
    print(x, Batches[x])   #(key, value)

print("____________________________________")
print("Data traversal using for loop")
for x in Batches:
    print(x, Batches.get(x))   #(key, value)

keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)

