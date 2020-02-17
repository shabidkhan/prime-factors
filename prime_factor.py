user=int(input('enter no '))
last=[]
for i in range(2,user//2+1):
	if user%i==0:
		for j in range(2,i//2+1):
			if i%j==0:
				break
		else:
			last.append(i)
print(last)
