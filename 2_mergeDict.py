# method 1
name1 = {"kelly": 21, "john": 22, "jane": 23}
name2 = {"Ravi": 45, "Mpho": 67}
names = name1 | name2
print(names)

# method 2
name1 = {"kelly": 21, "john": 22, "jane": 23}
name2 = {"Ravi": 45, "Mpho": 67}
names = {**name1 , **name2}
print(names)