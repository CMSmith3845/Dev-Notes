s = input("Enter Roman Numeral ")
num = None
s = s.upper()

def qualifier(s):
	if s not in ['I', 'V', 'X', 'L', 'C', 'D','M']:
		print('invalid')
		return False
	return True
 

def numeral(s):
	 global num
	 if s == 'I':
	 	num = 1
	 	print(num)
	 else:
	 	num = None
	 	
		 	
if qualifier(s):  # This means if qualifier is true then run numeral
	numeral(s)
	
	
def numeral(s):
	 global num
	 if s == 'V':
	 	num = 5
	 	print(num)
	 else:
	 	num = None
	 	
	 	
if qualifier(s):
	numeral(s)
	 	

def numeral(s):
	 global num
	 if s == 'X':
	 	num = 10
	 	print(num)
	 else:
	 	num = None
	 	

if qualifier(s):
	numeral(s)
	 	
	 	
def numeral(s):
	 global num
	 if s == 'L':
	 	num = 50
	 	print(num)
	 else:
	 	num = None
	 	
	 		 	
	 	
if qualifier(s):
	numeral(s)	 	
	 	
def numeral(s):
	 global num
	 if s == 'C':
	 	num = 100
	 	print(num)
	 else:
	 	num = None
	 	

	 	
if qualifier(s):
	numeral(s)
		 	
	 		 		 	
def numeral(s):
	 global num
	 if s == 'D':
	 	num = 500
	 	print(num)
	 else:
	 	num = None
	 	
	 	
	 	
if qualifier(s):
	numeral(s)
	 	
	 	
def numeral(s):
	 global num
	 if s == 'M':
	 	num = 1000
	 	print(num)
	 else:
	 	num = None
	 
	 	
if qualifier(s):
	numeral(s)
	



		



		
		

