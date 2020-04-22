print("Enter data: ")
l=[]
bal=0
while True:
 x=input()
 if x:
  l.append(x)
 else:
  break
for i in l:
 s=i.split()
 if(s[0]=="D"):
  bal=bal+int(s[1])
 elif(s[0]=="W"):
  bal=bal-int(s[1])
print(bal)
