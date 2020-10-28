import os.path
print("Press 1 if you want to spell check a sentence.", "\nPress 2 if you want to spell check a file.", "\nPress 0 if you want to quit the program.")
var = int(input())
while(var > 2 or var < 0):
	print("Invalid entry. Try again!")
	var = int(input())
while(var != 0):
	if(var == 1):
		sentence = input("Please input the sentence: ")
	elif(var == 2):
		filePath = input("Please enter the file name: ")
		while(os.path.isfile(filePath)):
			sentence = open(filePath, 'r').read()
			break
		else:
			print("Invalid path. Try again!")
			continue
	sep = " "
	word = ""
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	dictionary = open('EnglishWords.txt')
	for letter in sentence:
		alphabetPos = 0
		while(letter != sep):
			while(letter != alphabet[alphabetPos]):
				alphabetPos += 1
				if(alphabetPos == 52):
					break
			#if(letter != sep):
				#if(alphabetPos == 52):
					#continue
			if(letter.upper()):
				letter = letter.lower()
			word = word + letter
			print(word)
			break
		else:
			break
	#sentence.close()
	break
print("Program terminated!")