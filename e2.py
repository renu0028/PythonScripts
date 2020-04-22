def sum(array,n):
 s=0
 for i in array:
  s=s+i
 print(s)
arr=[]
o='y'
count=0
while (o=='y'):
 print("enter:")
 count=count+1
 n=int(input())
 arr.append(n)
 print("Do you want to enter more numbers?")
 o=input().strip().lower()
 if o!='y':
  break
sum(arr,count)
