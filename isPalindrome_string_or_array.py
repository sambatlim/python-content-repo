def isPalindrome( a ):
	return a[:] == a[::-1]               # Checks with palindrome


def isPalindrome ( a ):
	for i in range(len(a)//2):
	    if (a[i]!=a[len(a)-i-1]):       # Palindrome check
	        return 0
	return 1
