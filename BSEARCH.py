import os
def linearsrch(mylist,n,key):
	j=0
	for i in range(n//2,n):
		if mylist[i]==key:
			print("Key Is Found At Location ",i+1," Of The Given List")
			j=1
	for i in range(0,n//2):
		if mylist[i]==key:
			print("Key Is Found At Location ",i+1," Of The Given List")
			j=1
	return j
mylist=[]
n=int(input("Enter The Size: "))
mylist=list(map(int,input("Enter the no: ").strip().split()))[:n]
print(mylist)	
key=int(input("Enter the element to be searched: "))
os.system('clear')
pos=linearsrch(mylist,n,key)
if pos==0:
	print("Key Is Not Found")
	
