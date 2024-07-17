#identity operators
#is returns true if both the variables in the same object
#is not returns  true if both the variables in the same object
# is operator we are going to use for list, sets,dictionary
x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)
print(id(x))
print(id(y))

print(x is not y)

a=10
b=10
print(a is  b )