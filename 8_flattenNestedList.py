# 8_flattenNestedList
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newlist=[]
for list2 in list1:
    for item in list2:
        newlist.append(item)
print(newlist)        
