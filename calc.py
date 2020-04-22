import math
C=50
H=30
n=input("Enter values for D: ")
l=[]
l=n.split(',')
s=""
l1=[]
for i in l:
 i=int(i)
 Q=int(math.sqrt(((2*C*i)/H)))
 l1.append(str(Q))
print(','.join(l1))
