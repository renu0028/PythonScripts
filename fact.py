l=[]
l1=[]
n=input("Enter numbers: ")
l=n.split(',')
for i in l:
 i=int(i)
 f=1
 while (i>0):
  f=f*i
  i-=1
 l1.append(str(f))
print(','.join(l1))
