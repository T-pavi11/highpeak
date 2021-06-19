def combinations(arr,data,start,end,index,r):
	if(index==r):
		combis.append(data)
		return
	i=start
	while(i<=end and end - i + 1>=r - index) :
		data[index]=arr[i]
		combinations(arr,data,i+1,end,index+1,r)
		i+=1
def min_max_diff(combin):
	mi=combin[0][1]
	ma=0
	for item in combin:
		if item[1]<mi:
			mi=item[1]
		if item[1]>ma:
			ma=item[1]
	return ma-mi
inputf=open('sample_input.txt','r+')
goodies=[]
f=0
for line in inputf:
	if line.strip()=='':
		continue
	if line.startswith("Number of employees:"):
		no_of_emp=int(line.strip().split()[-1])
	if line.startswith("Goodies and Prices:"):
		f=1
		continue
	if f==1:
		l=line.strip().split(': ')
		goodies.append([l[0],int(l[1])])
combis=[]
data=[0]*no_of_emp
combinations(goodies,data,0,len(goodies)-1,0,no_of_emp)
