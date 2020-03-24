file=open("soybean-small.data", "r")
data=[]
for i in range(36):
	data+=[[]]
line=file.readlines()
acc=0
for ii in range(len(line)):
	temp=line[ii].split(",")
	for i in range(35):
		data[i]+=[temp[i]]
	data[35]+=[temp[35].strip()]
n=len(data[0])
for i in range(n):
	x=[]
	#print(len(data[0]))
	for k in range(36):
		x+=[data[k].pop(0)]
	count_output1=0
	count_output2=0
	count_output3=0
	count_output4=0
	output1=[]
	output2=[]
	output3=[]
	output4=[]
	for k in range(35):
		output1+=[0]
		output2+=[0]
		output3+=[0]
		output4+=[0]
	for k in range(len(data[0])):
		if(data[35][k]=="D1"):
			count_output1+=1
			#print(count_output1)
			for j in range(35):
				if(data[j][k]==x[j]):
					output1[j]+=1
		elif(data[35][k]=="D2"):
			count_output2+=1
			for j in range(35):
				if(data[j][k]==x[j]):
					output2[j]+=1
		elif(data[35][k]=="D3"):
			count_output3+=1
			for j in range(35):
				if(data[j][k]==x[j]):
					output3[j]+=1
		else:
			count_output4+=1
			for j in range(35):
				if(data[j][k]==x[j]):
					output4[j]+=1
	for k in range(35):
		output1[k]=output1[k]/count_output1
		output2[k]=output2[k]/count_output2
		output3[k]=output3[k]/count_output3
		output4[k]=output4[k]/count_output4
	final1=1
	final2=1
	final3=1
	final4=1
	for j in range(35):
		final1*=output1[j]
		final2*=output2[j]
		final3*=output3[j]
		final4*=output4[j]
	final1*=(count_output1/n)
	final2*=(count_output2/n)
	final3*=(count_output3/n)
	final4*=(count_output4/n)
	if(x[35]=="D1"):
		a=final1
	elif(x[35]=="D2"):
		a=final2
	elif(x[35]=="D3"):
		a=final3
	else:
		a=final4
	if(final1==final2==final3==final4==0):
		t=1
	elif(max(final4,final3,final2,final1)==final1):
		t="D1"
		b=final1
	elif(max(final4,final3,final2,final1)==final2):
		t="D2"
		b=final2
	elif(max(final4,final3,final2,final1)==final3):
		t="D3"
		b=final3
	elif(max(final4,final3,final2,final1)==final4):
		t="D4"
		b=final4
	# elif(final1==final2==final3==final4==0):
	# 	continue
	if(t==x[35]):
		acc+=1
	# elif(a==b):
	# 	acc+=1
	for j in range(36):
		data[j]+=[x[j]]
		#print([x[j]])
	#print(data[35])
print("soybean")
print("Accuracy Fraction : "+ str(acc/n))
print("Accuracy Percentage : "+ str(100*(acc/n))+" %")