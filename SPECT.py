file=open("SPECT.train", "r")
line=file.readlines()
file2=open("SPECT.test", "r")
line2=file2.readlines()
train=[]
test=[]
acc=0
thenthen=[]
for i in range(23):
	train+=[[]]
	test+=[[]]
	thenthen+=[[]]
for i in range(len(line)):
	temp=line[i].split(",")
	for j in range(22):
		train[j]+=[temp[j+1]]
	train[22]+=[temp[0].strip()]
for i in range(len(line2)):
	temp=line2[i].split(",")
	for j in range(22):
		test[j]+=[temp[j+1]]
	test[22]+=[temp[0].strip()]
n=len(test[0])
#acc=25
while test!=thenthen:
	x=[]
	for j in range(23):
		x+=[test[j].pop(0)]
	output1=0
	output0=0
	output1_vals=[]
	output0_vals=[]
	for i in range(22):
		output1_vals+=[0]
		output0_vals+=[0]
	for k in range(len(train[0])):
		if train[22][k]=="1":
			output1+=1
			for j in range(22):
				if(train[j][k]==x[j]):
					output1_vals[j]+=1
		else:
			output0+=1
			for j in range(22):
				if(train[j][k]==x[j]):
					output0_vals[j]+=1
	final1=output1/len(train)
	final0=output0/len(train)
	for ii in range(22):
		output1_vals[ii]=output1_vals[ii]/output1
		output0_vals[ii]=output0_vals[ii]/output0
	for k in range(22):
		final1*=output1_vals[k]
		final0*=output0_vals[k]
	if(final1>final0):
		t="1"
	else:
		t="0"
	if(t==x[-1]):
		acc+=1
	# for j in range(23):
		# test[j]+=[x[j]]
print("SPECT")
print("Accuracy Fraction : "+ str(acc/n))
print("Accuracy Percentage : "+ str(100*(acc/n))+" %")