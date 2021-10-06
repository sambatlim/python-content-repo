name=(input('enter the name= '))
g=float(input('enter the grade= '))

if g>1 or g<0:
    print('error')
elif g>=0.9:
    print('your grade is A')    
elif g>=0.8:
    print('your grade is B')    
elif g>=0.7:
    print('your grade is C')    
elif g>=0.6:
    print('your grade is D') 
elif g<0.6:
     print('your are fail')
