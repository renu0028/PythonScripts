import re
n=input("Enter some passwords: ")
l=[]
l1=[]
l=n.split(',')
for i in l:
 if(len(i)>=6 and len(i)<=12):
  if(re.search("[A-Z]",i)):
   if(re.search("[a-z]",i)):
    if(re.search("[0-9]",i)):
     if(re.search("[$#@]",i)):
      l1.append(str(i))
print(','.join(l1))
