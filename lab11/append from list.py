#list
my_list=[1,2,3,4]
print("my list is :",my_list)

#indexing
print("my list is 3 is",my_list[3])

#changing of an element
my_list[3]=40
print("my new list is ",my_list)

#append
my_list.append(234)
print(my_list)

#extend
my_list.extend([8,9])
print(my_list)

#insert
my_list.insert(3,31)
print(my_list)

#remove
my_list.remove(40)
print(my_list)

#copy
hosa_list=my_list.copy()
print(hosa_list)

#clear
my_list.clear()
print(my_list)

print(hosa_list)

#sorting
hosa_list.sort()
print(hosa_list)

#reverse
hosa_list.reverse()
print(hosa_list)

print(len(hosa_list))