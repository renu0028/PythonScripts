n=input("Enter something: ")
c=0
d=0
for i in n:
 if i.isalpha():
  c+=1
 elif i.isdigit():
  d+=1
print("LETTERS {}".format(c))
print("DIGITS {}".format(d))
