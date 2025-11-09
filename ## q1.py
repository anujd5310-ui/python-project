## q1 factoral
n=int(input("entr num:"))
fact=1
for i in range (1,n+1):
    fact*=i
print(" your factorial ",fact)

# ##q2 armstrong
n=int(input("enter num1:"))
s=len(str(n))
copy=n
sum=0
while n>0:
    a=n%10
    p=a**s
    sum+=p
    n//=10
if copy ==sum:
    print("num hai armstrong")
else:
    print("not armstrong")

## q3 niven
n=int(input("enter num:"))
copy=n
sum=0
while n>0:
    sum+=n%10
    n//=10
if copy%sum==0:
    print("yes hai harsad")
else:
    print("nhi hai bhai ")

## q4 revrse
n=int(input("enter num"))
copy=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)

##q5 
while True:
    year=int(input("enter your year:"))
    if year%400==0 and year %100==0:
        print("leap year")
    elif year %100!=0 and year%4==0:
        print("leap year")
    else:
        print("nhi ahi leap hai")
    

