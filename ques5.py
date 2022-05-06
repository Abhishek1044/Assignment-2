# taking a,b,c sides of triangle
# this prints true and false only

a=int(input("Provide sides of triangle > 0 \n \t Enter side 1 of triangle : \n \t"))
b=int(input("Enter side 2 of triangle : \n \t"))
c=int(input("Enter side 3 of triangle : \n \t"))

sum1=a+b
sum2=b+c
sum3=c+a

ans1=(c < sum1) 
ans2=(a < sum2) 
ans3=(b < sum3)

print(ans1 and ans2 and ans3)