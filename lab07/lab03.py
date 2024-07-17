x=10
y=23
z=12

if x>y and x>z:
    print("greater value is",x)
elif y>x and y>z:
    print("greater value is", y)
else:
    print('greater value is', z)

a=10
b=20
c=30
result=a if a>b and a>c else (b if b>c else c)
print(result)