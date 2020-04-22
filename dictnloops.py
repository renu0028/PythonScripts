students={"girls":["renu","simran","rakshi"],"boys":["ran","rishi","naru","nandu"]}
for i in students.keys():
 for j in students[i]:
  if 'r' in j:
   print(j,end=" ")
print()
