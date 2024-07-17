#Use the ternary operator to find the maximum of three numbers entered by the user

a,b,c=(100,20,400)
max=a if a>b and a>c else b if b>c else c
print(max)

# develope a python script that calculates square and cube of a given number

x=int(input("enter the value of x\n"))
y=int(input("enter the raise value\n"))
z=int(input("enter the raise value\n"))
square=x**y
cube=x**z
print("the square of a " ,x, "number is ",square)
print("the cube of a " ,x, "number is ",cube)
