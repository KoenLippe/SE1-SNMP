## Given gates
def Nand(p,q):
	return 0 if p&q else 1

def Or(p,q):
	return Nand(Nand(p,p),Nand(q,q))

def And(p,q):
	return Nand(Nand(p,q),Nand(p,q))

def Xor(p,q):
	r = Nand(p,q)
	return Nand(Nand(p,r),Nand(r,q))

def Not(a):
	return Nand(a,a)

def bit(b):
	return 0 if b=='0' else 1

def Nots(A):
	return [Not(a) for a in A]
	

def add(A,B):
	C=[0]*9
	S=[0]*8
	S[-1]=Xor(A[-1],B[-1])
	C[-2]=And(A[-1],B[-1])
	for i in range(-2,-9,-1):
		S[i] = Xor(Xor(A[i],B[i]),C[i])
		C[i-1] = Or(And(Xor(A[i],B[i]),C[i]),
					And(A[i],B[i]))
	return S


#Phase 1 substraction binary numbers
def sub(A, B):

	return 0




##def add(A, B){
#}

#Phase 2 addition binary numbers


## Testing method
def parse(calc):
	print()
	sign = [1,1]
	if calc[0]=='-':
		calc = calc[1:]
		sign[0] = -1
	if '+-' in calc:
		bins = calc.split('+-')
		sign[1] = -1
	elif '-' in calc:
		print("-")
		bins = calc.split('-')
		sign[1] = -1	
	else:
		print("+")
		bins = calc.split('+')

	print("First: " + bins[0])
	print("Second: " + bins[1])
	print()

	for index, bin in enumerate(bins):
		# bin = waarde in bins
		
		bins[index] = ([0]*(8-len(bin)))  + [ bit(c) for c in bin ]
		
		
		#print(bit(c) for c in bin)



		if sign[index]<0:
			# sign [0] < 0 means that only "-" is entered
			# sign [1] < 0 means that "-" is in calc or "+-" is in calc
			
			#Basicly if not x + x:
			
			bins[index]=add(Nots(bins[index]),[0,0,0,0,0,0,0,1])
			
			#[0,0,0,0,0,0,0,0] + [0,0,0,0,0,0,0,1]
			print(str(Nots(bins[index])) + " + " + str([0,0,0,0,0,0,0,1]))
			
			print(add(Nots(bins[index]),[0,0,0,0,0,0,0,1]))

	return bins

#calc = input('addition?\n')

calc = "7+7"

A,B = parse(calc)





print("A: " + str(A))
print("B: " + str(B))

print()
print()
print("--------		Substracting		--------")
#print('Substract result: ' + ''.join(str(b) for b in sub(A,B)))

print()
print()
print("--------		Adding		--------")
print('Adding result: ' + ''.join(str(b) for b in add(A,B)))

