'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

# We are Returning head after reversing the linked list

def reverseDLL(head):                  # We are changing the data of Linked list
    
    a=[]  # temporary array
    h=head

    while(h.next is not None):          # Traversing Linked List and storing data of Nodes
        a.append(h.data)
        h=h.next
    a.append(h.data)
    
    t=head
    while(t):                           # Traversing Linked List and changing value
        t.data=a.pop()                  # Array a will popping elements in reverse order than of linked list
        t=t.next  
    return head

def reverseDLL(head):                   # We are actually reversing the linked list
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head