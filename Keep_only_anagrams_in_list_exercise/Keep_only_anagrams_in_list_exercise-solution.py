'''
This exercise require to take a list and return it in the SAME ORDER after omitting the non-anagram elements .


L = ["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]

expected_result = ["pool", "loco", "cool", "stain", "satin", "loop"]


'''
############################################################################################################




L = ["pool","loco","cool","stain","satin","pretty","nice","loop","life","banana","file"]

# Creating 3 empty lists

sortedL = []
after_omitting_L = []
expectedL = []

#Iterating the L list , and sorting & appending each element to the sortedL list

for word in L:
    sortedL.append(sorted(word))
print(sortedL)


#Counting items in "sortedL" list & appending only items that apeares more than ONCE to "after_omitting_L" list

for word in sortedL:
    x = sortedL.count(word)
    if x>1:
        after_omitting_L.append(word)

print(after_omitting_L)


# sorting& iterating each elements again in original list(L) , then appending only items that appear in "after_omitting" list to the final "expected" list.

for word in L:
    y = (sorted(word))
    if y in after_omitting_L:
        expectedL.append(word)

print(expectedL)





