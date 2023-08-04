#1.Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Josef Král
email: josef.kralu@seznam.cz
discord: MrOptiminus#6658
"""
from random import shuffle
import time

separator = '-' * 47

#2.Program pozdraví užitele a vypíše úvodní text
print('Hi there!\n\b',separator,'\nI\'ve generated a random 4 digit number for you.')
print('Let\'s play a bulls and cows game.\n\b',separator)

#3.Program vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
z = list('0123456789')     
shuffle(z)                 	
#x = z[3:7] if z[3] != '0' else z[4:8]
x = ''.join(z[3:7] if z[3] != '0' else z[4:8])

print('Enter a number:\n\b',separator)

count=0
start_time = time.time()   
while True:
#4.Hráč hádá číslo. Program jej upozorní, pokud zadá číslo 
#kratší nebo delší než 4 čísla,pokud bude obsahovat duplicity,
#začínat nulou, příp. obsahovat nečíselné znaky '''
	try:
		y = input('>>>')
		int(y)
	except:
		print('Not a number')
		continue
	
	if len(y) != 4:
		print('Must by 4 digits')
		continue	
		
# for debuggin	
	if int(y) == 0000:		
		print ('My secret 4-digit number:', x)
		continue
				
	b = 0; c = 0			
	count+=1  
	for i in range(4):                      
		if y[i] == x[i]: 	                  
			b += 1                         
		elif y[i] in x:            
			c += 1
			
#5.Program vyhodnotí tip uživatele
#6.Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění),
#příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění).
#Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu.
#Tedy 1 bull a 2 bulls (stejně pro cow/cows).	
	print(str(b), 'bull' if b is 1 else 'bulls', str(c), 'cow' if c is 1 else 'cows')
	print(separator)
	if b == 4:                          
		print('Correct, you\'ve guessed the right number in', count, 'guesses!\n\b',separator)             
		break
		
#počítání času, za jak dlouho uživatel uhádne tajné číslo
tm= time.time() - start_time   
if count <= 5:
	print('That\'s amazing.')
elif 5 < count <=10:
	print('That\'s average.')
else:
	print('That\'s not so good.')
print("You've guessed the right number are %d min %d seconds\n" %(tm//60, tm % 60 ))	