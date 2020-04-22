n=input("Enter 4 digit binary nos. :")
l=[]
l=n.split(',')
l1=[]
for i in l:
 base=1
 j=i
 i=int(i)
 s=0
 while(i>0):
  r=int(i%10)
  i=i/10
  s=s+(r*base)
  base*=2
 if(s%5==0):
  l1.append(j)
print(','.join(l1)) 
