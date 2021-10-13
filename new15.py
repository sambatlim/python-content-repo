n=int(input("enter number"))
t=0
s=n
while(n>0):
	r=n%10
	n=n//10
	t=t*10+r
if(s==t):
	print("yes")
else:
	print("no")
