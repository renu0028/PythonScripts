sentence=input("enter something: ").strip().lower()
words=sentence.split()
W=[]
for i in words:
 if i[0] in "aeiou":
  new=i+"yay"
 else:
  position=0
  for j in i:
   if j not in "aeiou":
    position=position+1
   else:
    break
  x=i[position:]
  y=i[:position]
  z="ay"
  new=x+y+z
 W.append(new)
output=" ".join(W)
print(output)
