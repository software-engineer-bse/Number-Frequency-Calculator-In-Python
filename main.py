list1 =  [1,2,2,2,3,3,3,3]
list2 = []
list3 = []
for i in list1:
    if i not in list2:
        list2.append(i)
num = 0
for j in list2:
    num = 0
    for k in list1:
        if j==k:
            num = num + 1
    list3.append(num)
            
  
print(list2)
print(list3)