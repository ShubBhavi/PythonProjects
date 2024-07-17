set2=[1,2,3,34,4,5,5]
print(set2)

set1=set(set2)
print(set1)


num={1,2,3,4,}
num1={5,6,7,8,9}
numbers=num.union(num1)
print(numbers)


num={1,2,3,4,}
num1={5,3,2,6,7,8,9}
numbers=num.intersection(num1)
print(numbers)

num={1,2,3,4,}
num1={4,3,7,8,9}
numbers=num.difference(num1)
print(numbers)


num={1,2,3,4,5,6}
num1={5,6}
numbers=num1.issubset(num)  #is 5,6 i.e num1 is a part of num
print(numbers)