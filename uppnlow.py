n=input("enter: ")
u=0
l=0
for i in n:
 if i.isupper():
  u+=1
 elif i.islower():
  l+=1
print("UPPER CASE {}".format(u))
print("LOWER CASE {}".format(l))
