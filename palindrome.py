num=int(input("enter a number: ")
temp=num
rev=0
while temp!=0:
rev=(rev*10)+(temp%10)
temp=temp
if num==rev:
print("number is palindrome")
else:
print("number is not palindrome")
