def isPalindrome(head):
    
    a=[]
    h=head
    while(h):
        a.append(h.data)
        h=h.next
    
    return a[:]==a[::-1]
