import os.path, time
from datetime import datetime
from difflib import SequenceMatcher
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
	wordList = dictionary.readlines()
	dictionary.close()
	correct = 0
	incorrect = 0
	wordNumber = 0
	wordAdded = 0
	wordAccepted = 0
	t0 = time.time()
	timeStart = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	for letter in sentence:
		alphabetPos = 0
		if(letter != sep):
			while(letter != alphabet[alphabetPos]):
				alphabetPos += 1
				if(alphabetPos == 52):
					break
			if(alphabetPos == 52):
				continue
			if(letter.upper()):
				letter = letter.lower()
			word = word + letter
		else:
			print(word)
			wordNumber += 1
			ok = 0
			for line in wordList:
				if word in line:
					if(len(word)+1 == len(line)):
						ok = 1
						correct += 1
						break
			if(ok == 0):
				print(word + " is not a word!", "\n\nWhat would you like to do?", "\n1.Ignore", "\n2.Mark", "\n3.Add to dictionary", "\n4.Suggest likely correct spelling")
				decision = int(input())
				while(decision < 1 and decision > 4):
					print("Invalid entry. Try again!")
				else:
					if(decision == 1):
						incorrect += 1
						print("Word ignored!")
					elif(decision == 2):
						incorrect += 1
						word = "?" + word + "?"
						print("Word marked!")
					elif(decision == 3):
						dictionary = open("EnglishWords.txt", "a")
						dictionary.write(word)
						dictionary.close()
						correct += 1
						wordAdded += 1
						print("Word added to dictionary. Please open 'EnglishWords.txt' and save the file in order for the changes to take effect")
					else:
						score0 = float(round(0,1))
						for line in wordList:
							score1 = SequenceMatcher(None, line, word).ratio()
							if(score1 > score0):
								score0 = score1
								suggestion = line
						if(score0 > 0):
							print("Spelling suggestion: " + suggestion)
							answer = input("Would you like to replace the word? ")
							if answer in ("yes", "YES", "Yes", "Y", "y", "yeah", "Yeah", "YEAH", "Sure", "sure", "1", "ok", "Ok", "OK"):
								word = suggestion.rstrip()
								print("Word replaced successfully! " + word)
								correct += 1
								wordAccepted += 1
							else:
								print("Word not replaced.")
								incorrect += 1
						else:
							print("No suggestion available!")
			word = ""
	wordNumber += 1
	print(word)
	ok = 0
	for line in wordList:
		if word in line:
			if(len(word)+1 == len(line)):
				ok = 1
				correct += 1
				break
	if(ok == 0):
		print(word + " is not a word!", "\n\nWhat would you like to do?", "\n1.Ignore", "\n2.Mark", "\n3.Add to dictionary", "\n4.Suggest likely correct spelling")
		decision = int(input())
		while(decision < 1 and decision > 4):
			print("Invalid entry. Try again!")
		else:
			if(decision == 1):
				incorrect += 1
				print("Word ignored!")
			elif(decision == 2):
				incorrect += 1
				word = "?" + word + "?"
				print("Word marked!")
			elif(decision == 3):
				dictionary = open("EnglishWords.txt", "a")
				dictionary.write(word)
				dictionary.close()
				correct += 1
				wordAdded += 1
				print("Word added to dictionary. Please open 'EnglishWords.txt' and save the file in order for the changes to take effect")
			else:
				score0 = float(round(0,1))
				for line in wordList:
					score1 = SequenceMatcher(None, line, word).ratio()
					if(score1 > score0):
						score0 = score1
						suggestion = line
				if(score0 > 0):
					print("Spelling suggestion: " + suggestion)
					answer = input("Would you like to replace the word? ")
					if answer in ("yes", "YES", "Yes", "Y", "y", "yeah", "Yeah", "YEAH", "Sure", "sure", "1", "ok", "Ok", "OK"):
						word = suggestion.rstrip()
						print("Word replaced successfully! " + word)
						correct += 1
						wordAccepted += 1
					else:
						print("Word not replaced.")
						incorrect += 1
				else:
					print("No suggestion available!")
	#sentence.close()
	break
t1 = time.time() - t0
print("\nThe total number of words is: " + str(wordNumber) + ".")
print("The number of words spelt correctly is: " + str(correct) + ".")
print("The number of words spelt incorrectly is: " + str(incorrect) + ".")
print("The number of words added to dictionary is: " + str(wordAdded) + ".")
print("The number of words changed by the user is: " + str(wordAccepted) + ".")
print("The date and time the input was spellchecked was:  " + str(timeStart) + ".")
print("The amount of time elapsed to spellcheck the input is: " + str(float(round(t1,4))) + " seconds.")
print("Program terminated!")