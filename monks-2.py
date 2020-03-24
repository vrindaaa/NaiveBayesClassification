file=open("monks-2.train", "r")
data=[[],[],[],[],[],[],[]]
line=file.readlines()
acc=0
for ii in range(len(line)):
	temp=line[ii].split()
	for i in range(6):
		data[i]+=[temp[i+1]]
	data[6]+=[temp[0].strip()]
file2=open("monks-2.test", "r")
test=[[],[],[],[],[],[],[]]
line2=file2.readlines()
acc=0
for ii in range(len(line2)):
	temp=line2[ii].split()
	for i in range(6):
		test[i]+=[temp[i+1]]
	test[6]+=[temp[0].strip()]
n2=len(test[0])
n=len(data[0])
for i in range(n2):
	x=[]
	#print(len(data[0]))
	for k in range(7):
		x+=[test[k].pop(0)]
	count_output1=0
	count_output2=0
	output1=[]
	output2=[]
	for k in range(6):
		output1+=[0]
		output2+=[0]
	for k in range(len(data[0])):
		#print(data[9][i]=="positive")
		#print(len(data))
		if(data[6][k]=="1"):
			count_output1+=1
			#print(count_output1)
			for j in range(6):
				if(data[j][k]==x[j]):
					output1[j]+=1
		else:
			count_output2+=1
			for j in range(6):
				if(data[j][k]==x[j]):
					output2[j]+=1
	for k in range(6):
		output1[k]=output1[k]/count_output1
		output2[k]=output2[k]/count_output2
	final1=1
	final2=1
	for j in range(6):
		final1*=output1[j]
		final2*=output2[j]
	final1*=(count_output1)
	final2*=(count_output2)
	if(final1>=final2):
		t="1"
	else:
		t="0"
	if(t==x[6]):
		acc+=1
	elif(final1==final2):
		acc+=1
	for j in range(7):
		test[j]+=[x[j]]
		#print([x[j]])
	#print(ata[9])
print("monks-2")
print("Accuracy Fraction : "+ str(acc/n2))
print("Accuracy Percentage : "+ str(100*(acc/n2))+" %")