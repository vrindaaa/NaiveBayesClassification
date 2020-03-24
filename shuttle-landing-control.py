file=open("shuttle-landing-control.data", "r")
data=[[],[],[],[],[],[],[]]
line=file.readlines()
acc=0
for ii in range(len(line)):
	temp=line[ii].split(",")
	for i in range(6):
		data[i]+=[temp[i+1]]
	data[6]+=[temp[0].strip()]
n=len(data[0])
for i in range(n):
	x=[]
	#print(len(data[0]))
	for k in range(7):
		x+=[data[k].pop(0)]
	count_output1=0
	count_output2=0
	output1=[]
	output2=[]
	for k in range(6):
		output1+=[0]
		output2+=[0]
	for k in range(len(data[0])):
		if(data[6][k]=="1"):
			count_output1+=1
			for j in range(6):
				if(data[j][k]==x[j]):
					output1[j]+=1
				elif(data[j][k]=="*"):
					output1[j]+=1
				elif(x[j]=="*"):
					output1[j]+=1
		else:
			count_output2+=1
			for j in range(6):
				if(data[j][k]==x[j]):
					output2[j]+=1
				elif(data[j][k]=="*"):
					output2[j]+=1
				elif(x[j]=="*"):
					output2[j]+=1
	if(count_output1!=0):
		for k in range(6):
			output1[k]=output1[k]/count_output1
	if(count_output2!=0):
		for k in range(6):
			output2[k]=output2[k]/count_output2
	final1=1
	final2=1
	for j in range(6):
		final1*=output1[j]
		final2*=output2[j]
	final1*=(count_output1/n)
	final2*=(count_output2/n)
	if(final1>=final2):
		t="1"
	else:
		t="2"
	if(t==x[6]):
		acc+=1
	for j in range(7):
		data[j]+=[x[j]]
print("shuttle-landing-control")
print("Accuracy Fraction : "+ str(acc/n))
print("Accuracy Percentage : "+ str(100*(acc/n))+" %")