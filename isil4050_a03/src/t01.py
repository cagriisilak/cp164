"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-02"
-------------------------------------------------------
"""
from functions import stack_combine
from Stack_array import Stack
source1 = Stack()
source2 = Stack()
source1.push(1)
source1.push(3)
source1.push(5)
source1.push(7)
source2.push(2)
source2.push(4)
source2.push(6)
source2.push(8)



target = stack_combine(source1, source2)
for i in target:
    print(i)