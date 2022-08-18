n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    x=n%10
    rev=rev*10+x
    n=n//10
if(temp==rev):
    print("The given number is a palindrome!")
else:
    print("The given number is not a palindrome!")