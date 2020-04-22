l=[]
print("Enter multiple lines: ")
while True:
 line=input()
 if line:
  l.append(line)
 else:
  break
s="\n".join(l)
print(s.upper())
