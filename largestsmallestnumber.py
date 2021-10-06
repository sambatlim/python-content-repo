#largest and smallest
x=0
largest=-1
smallest=None
while True:
    x=input("enter the number: ")
    if x=="done":
        break
    a=int(x)
    if smallest is None:
        smallest=a
    elif a<smallest:
        smallest=a

    if a>largest:
        largest=a
print(largest)
print(smallest)
