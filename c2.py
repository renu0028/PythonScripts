import os
import csv
rows=[]
fields=['kernel-name','nodename','kernel-release','kernel-version','machine','processor','hardware-platform','operating-system']
file1=os.system('uname -a>file1')
#file1='oo'
with open(file1,'r') as csvfile:
 csvreader=csv.reader(csvfile)
 for i in csvreader:
  rows.append(i)
print("\nField names are: "+','.join(i for i in fields))
print("\n")
for j in rows:
 print(j) 
