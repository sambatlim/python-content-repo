y=int(input('enter the year = '))

if y%100==0:
     if y%400==0:
         print('leap year')
     if y%400!=0:
         print('non leap year')   
if y%100!=0:
     if y%4==0:
          print('leap year')
     else :print('non leap year')   
print('done')
