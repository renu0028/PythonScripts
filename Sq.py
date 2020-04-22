n=input("Enter: ")
l=[]
l2=[]
l=n.split(",")
for i in l:
 i=int(i)
 if(i%2==1):
  l2.append(str(i*i))
print(','.join(l2))
