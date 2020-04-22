n=input("Enetr a sentence: ")
l=[]
l=n.split()
l1=[]
for i in l:
 if i not in l1:
  l1.append(i)
l1.sort()
print(l1)
