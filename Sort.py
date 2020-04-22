from operator import itemgetter
n=input("Enter data: ")
l=[]
while True:
 i=input()
 if i:
  l.append(tuple(i.split(',')))
 else:
  break
print(sorted(l,key=itemgetter(0,1,2)))
