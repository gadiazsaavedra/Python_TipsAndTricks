x=[12,45,67,89,34,100,13]
max_num = max(enumerate(x,start=0),key=lambda x:x[1])
print("the index of the largest number is : ",max_num[0])
