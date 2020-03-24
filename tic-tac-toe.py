file=open("tic-tac-toe.data", "r")
data=[[],[],[],[],[],[],[],[],[],[]]
line=file.readlines()
acc=0
for ii in range(len(line)):
	temp=line[ii].split(",")
	for i in range(9):
		data[i]+=[temp[i]]
	data[9]+=[temp[9].strip()]
n=len(data[0])
for i in range(n):
	x=[]
	#print(len(data[0]))
	for k in range(10):
		x+=[data[k].pop(0)]
	count_output1=0
	count_output2=0
	output1=[]
	output2=[]
	for k in range(9):
		output1+=[0]
		output2+=[0]
	for k in range(len(data[0])):
		#print(data[9][i]=="positive")
		#print(len(data))
		if(data[9][k]=="positive"):
			count_output1+=1
			#print(count_output1)
			for j in range(9):
				if(data[j][k]==x[j]):
					output1[j]+=1
		else:
			count_output2+=1
			for j in range(9):
				if(data[j][k]==x[j]):
					output2[j]+=1
	for k in range(9):
		output1[k]=output1[k]/count_output1
		output2[k]=output2[k]/count_output2
	final1=1
	final2=1
	for j in range(9):
		final1*=output1[j]
		final2*=output2[j]
	final1*=(count_output1/n)
	final2*=(count_output2/n)
	if(final1>final2):
		t="positive"
	else:
		t="negative"
	if(t==x[9]):
		acc+=1
	for j in range(10):
		data[j]+=[x[j]]
		#print([x[j]])
	#print(data[9])
print("tic-tac-toe")
print("Accuracy Fraction : "+ str(acc/n))
print("Accuracy Percentage : "+ str(100*(acc/n))+" %")