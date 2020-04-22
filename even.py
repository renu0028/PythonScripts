l=[]
for i in range(1000,3001):
 j=i
 f=1
 while(i>0 and f==1):
  r=i%10
  i=i//10
  if(r%2==0):
   f=1
  else:
   f=0
 if(f==1):
  l.append(str(j))
print(','.join(l))
