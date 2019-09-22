
def isWeird(num):
	if num % 2 != 0:
		print('Weird')
	elif num % 2 == 0:
		if ((2 <= num <= 5) | (num > 20)):
			print('Not Weird')
		elif 6 <= num <= 20:
			print('Weird')

def threeLines(a, b):
	if (1 <= a <= (10 ** 10)) & (1 <= b <= (10 ** 10)):
		print(a + b)
		print(a - b)
		print(a * b)
		
#threeLines(4, 5)
 
def isLeap(year):
	leap = False
	if 1900 <= year <= (10 ** 5):
		if year % 4 == 0:
			if ((year % 100 == 0) & (year % 400 != 0)):
				leap = False
			else: leap = True
	return leap
print(isLeap(2400))

def isLeap2(year):
	leap = False
	if 1900 <= year <= (10 ** 5):
		if (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)):
			leap = True
	return leap
print(isLeap2(2400))



