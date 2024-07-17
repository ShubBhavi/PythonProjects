#TRIANGLE CLASIFER
side1=int(input("enter the value of side1\n"))
side2=int(input("enter the value of side2\n"))
side3=int(input("enter the value of side3\n"))
if side1==side2==side3:
    print("this triangle is equilateral")
elif side1==side2 or side2==side3  or  side3==side1:
    print("this triangle is isosceles")
else:
    print("this triangle is scalene")
