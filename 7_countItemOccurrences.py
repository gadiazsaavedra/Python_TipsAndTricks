from collections import Counter

list1 = ["John", "Kelly", "Peter", "Moses", "Peter"]
count_peter = Counter(list1).get("Peter")
print(f"Peter occurs {count_peter} times in the list")
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_1 = Counter(list2).get(1)
print(f"1 occurs {count_1} times in the list")
count=0
for name in list1:
    if name == "Peter":
        count+=1
print(f"Peter occurs {count} times in the list")        