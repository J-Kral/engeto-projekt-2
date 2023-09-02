"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Josef Král
email: josef.kralu@seznam.cz
discord: MrOptiminus#6658
"""

import random
import time

separator = "-" * 47

#pozdrav
print('Hi there!\n\b', separator, '\nI\'ve generated a random 4 digit number for you.')
print('Let\'s play a bulls and cows game.\n\b', separator)

#tajne cislo
posloupnost = '123456789'
nahodne_prvky = random.sample(posloupnost, 5)
tajne_cislo = ''.join([str(x) for x in nahodne_prvky])
if tajne_cislo[0] == '0':
	tajne_cislo = tajne_cislo[1:]
else: 
	tajne_cislo = tajne_cislo[0:4]

#uvod
print('Enter a number:\n\b', separator)
count=0
start_time = time.time()

while True:
	inputNumber = input('>>>')	
# start debuggin	
	if  inputNumber == '0000':		
		print ('My secret 4-digit number:', tajne_cislo)
		continue
		
#kontrola vstupu					
	if not inputNumber.isdecimal():
		print('Error: must be only numbers')
		continue
	if inputNumber[0] == '0':
		print("Error: first digit cannot be 0")
		continue
	if len(inputNumber) != 4:
		print('Error: must be 4 digits')
		continue		
	if len(set(inputNumber)) != 4:			
		print("All digits must be unique!")
		continue
		
#hodnoceni shody		
	bulls = 0; cows = 0			
	count += 1  
	for i in range(4):                      
		if inputNumber[i] == tajne_cislo[i]: 	                  
			bulls += 1                         
		elif inputNumber[i] in tajne_cislo:            
			cows += 1
			
#1 bull a 2 bulls (stejně pro cow/cows).	
	print(str(bulls), 'bull' if bulls == 1 else 'bulls', str(cows), 'cow' if cows == 1 else 'cows')
	print(separator)
	if bulls == 4:                          
		print('Correct, you\'ve guessed the right number in', count, 'guesses!\n\b', separator)             
		break
#pocitani casu, hodnoceni uživatele
tm= time.time() - start_time   
if count <= 5:
	print('That\'s amazing.')
elif 5 < count <= 10:
	print('That\'s average.')
else:
	print('That\'s not so good.')
print("You've guessed the right number are %d min %d seconds\n" %(tm//60, tm % 60 ))
