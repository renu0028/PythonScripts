import os
import csv
file1='info'
fields=[]
rows=[]
with open(file1,'r') as csvfile:
 csv_r=csv.reader(csvfile)
 fields=next(csv_r)
 for row in csv_r:
  rows.append(row)
#count=0
#for i in file1:
# count+=1
#print("No. of rows:{}".format(count))
#print(fields)
field1=[]
s=""
for i in range(len(fields[0])):
 if(fields[0][i]==" "):
  if(s!=""):
   field1.append(s)
  s=""
  pass
 else:
  s+=fields[0][i]
print("Field names are:"+",".join(i for i in field1))
print("First 20 rows are:")
for i in rows[:20]:
 for j in i:
  print("{}".format(j))
  print("\n")
