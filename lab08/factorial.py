a=int(input("enter the number for a factorial"))
if a==0:
    print("the factorial for 0 is 1")
elif a<1:
    print("there is no factorial for negaative intgers")
else:
    fact=1
    for i in range(1,a+1):
     fact=fact*i
    print(fact)