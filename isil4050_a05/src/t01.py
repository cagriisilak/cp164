"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
from List_array import List

list = List()
list.append(1)
list.append(2)
list.append(3)
list.append(3)
list.append(3)
list.append(2)
list.clean()

for i in list:
    print(i)
    
list1 = List()
list2 = List()
list1.append(1)
list1.append(3)
list2.append(2)
list2.append(4)
list3 = List()
print(list3.is_empty())
list3.combine(list1,list2)
for i in list3:
    print(i)
    

print(list.__getitem__(2))
list4=List()
list4.intersection(list, list3)
print("spacer")
for i in list4:
    print(i)
b = list.is_identical(list4)
print(b)

list4.prepend(0)
for i in list4:
    print(i)
    
list4.remove_front()
for i in list4:
    print(i)

list3.remove_many(3)
for i in list3:
    print(i)





