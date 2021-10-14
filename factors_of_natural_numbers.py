# This function prints all factors of a natural number

def factors_of_natural_numbers(n):
	import math
	for i in range(1,math.ceil(math.sqrt(n))+1):
	    if(n%i==0):
	        if (n/i==i):                      # Because squrt has to be printed once only
	            print(i)
	        else:
	            print(i, n/i)