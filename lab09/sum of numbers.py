number=int(input("enter the value of num "))
sum=0
while number!=0:
 a=number%10
 sum=sum+a
 number//=10


 print(sum)
