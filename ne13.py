n=int(input("enter number"))
x=10
for i in range(n):
	for j in range(0,x):
		print(end=" ")
	x=x-1
	for j in range(i+1):
		print("*",end=" ")
	print(" ")

for i in range(1,n+1):
	for j in range(n-i):
		print(" ",end=" ")
	for j in range(1,i,1):
		print(j,end=" ")
	for j in range(i,0,-1):
		print(j,end=" ")
	print(" ")
