#--- For best results aspect-wise use full screen! ---

#--- Importing ---

import os.path, time
from datetime import datetime
from difflib import SequenceMatcher

#--- Main Menu ---

print("\nPress 1 if you want to spell check a sentence.", "\nPress 2 if you want to spell check a file.", "\nPress 0 if you want to quit the program.")
print("-------------------------------------------------")
var = int(input())
while(var > 2 or var < 0):
	print("Invalid entry. Try again!")
	var = int(input())
while(var != 0):
	if(var == 1):
		sentence = input("\nPlease input the sentence: ")
	elif(var == 2):
		filePath = input("\nPlease enter the file name: ")					#|
		while(os.path.isfile(filePath)):									#|
			fileOpen = open(filePath)										#| Verifies if the input file exist in the folder
			sentence = fileOpen.read()										#|
			fileOpen.close()												#|
			break
		else:
			print("Invalid path. Try again!")
			continue
	print(end='\n')

	#--- Variable declaration ---

	sep = " "
	word = ""
	sentenceNew = ""
	sentenceFile = ""
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"					
	dictionary = open('EnglishWords.txt')									#|
	wordList = dictionary.readlines()										#| Here is initialised the word list used for the spell check.
	dictionary.close()														#|
	correct = 0																# Number of correct words
	incorrect = 0															# Number of incorrect words
	wordNumber = 0															# Number of words
	wordAdded = 0															# Number of words added to dictioary
	wordAccepted = 0														# Number of words replaced by the sugggestion
	t0 = time.time()														# The time when the spell check started is recorded in t0
	timeStart = datetime.now().strftime("%d/%m/%Y %H:%M:%S")				# The time and date when the spell check started is recorded in timeStart

	#--- Splitting the sentence into words ---

	#--- Creating the word by going through the sentence letter by letter ---

	for letter in sentence:
		alphabetPos = 0														#|
		if(letter != sep):													#|
			while(letter != alphabet[alphabetPos]):							#| Checking if the character is a letter or not (excluding the white space)
				alphabetPos += 1											#|
				if(alphabetPos == 52):										#|
					break													
			if(alphabetPos == 52):											#| If it's not a letter, the program simply jumps it
				continue
			if(letter.upper()):					
				letter = letter.lower()										#| Any uppercase letter is transformed into a lowercase one
			word = word + letter

		#--- If the program finds white space (word separator) ---

		else:
			sentenceFile = sentenceFile + word + " "
			wordNumber += 1
			ok = 0
			for line in wordList:											#|
				if word in line:											#|
					if(len(word)+1 == len(line)):							#| THe word previously created is checked to see if it corresponds to any word from the list
						ok = 1												#|
						correct += 1										#|
						sentenceNew = sentenceNew + word + " "				# If so, the word is recorded
						break

			#--- Misspelling menu ---

			if(ok == 0):
				print("'" + word + "'" + " is not a word!", "\n\nWhat would you like to do?", "\n1.Ignore", "\n2.Mark", "\n3.Add to dictionary", "\n4.Suggest likely correct spelling")
				decision = int(input())
				while(decision < 1 and decision > 4):
					print("Invalid entry. Try again!")
				else:
					if(decision == 1):										#|
						incorrect += 1										#| 1. Ignoring the word the program records it and simply skips it
						sentenceNew = sentenceNew + word + " "				#|
						print("Word ignored!\n")
					elif(decision == 2):									#|
						incorrect += 1										#| 2. Marking the word with question marks ( ?example? )
						word = "?" + word + "?"								#|
						sentenceNew = sentenceNew + word + " "
						print("Word marked as " + word + ".\n")
					elif(decision == 3):									
						dictionary = open("EnglishWords.txt", "a")			#|
						dictionary.write(word)								#| 3. The word is added to the dictionary
						dictionary.close()									#|
						correct += 1										
						wordAdded += 1										
						sentenceNew = sentenceNew + word + " "
						print("Word added to dictionary. Please open 'EnglishWords.txt' and save the file in order for the changes to take effect.\n")
					else:

						#--- Suggestion menu ---

						print("\nLet me think for a moment...\n")			
						score0 = float(round(0,1))
						for line in wordList:
							score1 = SequenceMatcher(None, line, word).ratio()
							if(score1 > score0):							#|
								score0 = score1								#| Searching the list for the most similar word
								suggestion = line							#|
						if(score0 > 0):
							print("Spelling suggestion: " + suggestion.rstrip())
							answer = input("Would you like to replace the word? ")
							if answer in ("yes", "YES", "Yes", "Y", "y", "yeah", "Yeah", "YEAH", "Sure", "sure", "1", "ok", "Ok", "OK"):
								word = suggestion.rstrip()					#|
								print("Word replaced successfully!\n")		#| Replacing the word with the most similar one
								correct += 1								#|
								wordAccepted += 1
							else:
								print("Word not replaced.")					#| Not replacing the word
								incorrect += 1
							sentenceNew = sentenceNew + word + " "
						else:
							print("No suggestion available!")				#| No similar word found
			word = ""

	#--- The same program for the last word ---

	sentenceFile = sentenceFile + word
	wordNumber += 1
	ok = 0
	for line in wordList:
		if word in line:
			if(len(word)+1 == len(line)):
				ok = 1
				correct += 1
				sentenceNew = sentenceNew + word
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
				print("Let me think for a moment...")
				score0 = float(round(0,1))
				for line in wordList:
					score1 = SequenceMatcher(None, line, word).ratio()
					if(score1 > score0):
						score0 = score1
						suggestion = line
				if(score0 > 0):
					print("Spelling suggestion: " + suggestion.rstrip())
					answer = input("Would you like to replace the word? ")
					if answer in ("yes", "YES", "Yes", "Y", "y", "yeah", "Yeah", "YEAH", "Sure", "sure", "1", "ok", "Ok", "OK"):
						word = suggestion.rstrip()
						print("Word replaced successfully!\n")
						correct += 1
						wordAccepted += 1
					else:
						print("Word not replaced.")
						incorrect += 1
				else:
					print("No suggestion available!")
			sentenceNew = sentenceNew + word
	t1 = time.time() - t0

	#--- File creation ---

	print("-----------------------------------------------------------------------\n")
	fileName = input("Please name the text file in which the results are going to be stored: ")
	print(end='\n')
	while True:
		if(os.path.isfile(fileName) is False):
			myFile = open(fileName, 'x')
			print("\nA new file with the name: '" + fileName + "' has been succesfully created.\n")
			myFile = open(fileName, 'a')
			myFile.write("----- Summary Statistics ------\n\n")
			myFile.write("The total number of words is: " + str(wordNumber) + ".\n")
			myFile.write("The number of words spelt correctly is: " + str(correct) + ".\n")
			myFile.write("The number of words spelt incorrectly is: " + str(incorrect) + ".\n")
			myFile.write("The number of words added to dictionary is: " + str(wordAdded) + ".\n")
			myFile.write("The number of words changed by the user is: " + str(wordAccepted) + ".\n")
			myFile.write("The date and time the input was spellchecked was:  " + str(timeStart) + ".\n")
			myFile.write("The amount of time elapsed to spellcheck the input is: " + str(float(round(t1,4))) + " seconds.\n\n")
			myFile.write("The sentence that was spell checked is: '" + sentenceFile + "'\n")
			myFile.write("The new sentence is: '" + sentenceNew + "'")
			myFile.close()
			break
		else:
			print("Another file with the name '" + fileName + "' already exists. Please assign another name.")
			fileName = input()
			continue

	#--- Results ---

	print("-----------------------------------------------------------------------\n")
	print("The old sentence was: " + sentence)
	print("The new sentence is: " + sentenceNew)
	print("\n-----------------------------------------------------------------------\n")
	print("-----Statistics------\n")
	print("The total number of words is: " + str(wordNumber) + ".")
	print("The number of words spelt correctly is: " + str(correct) + ".")
	print("The number of words spelt incorrectly is: " + str(incorrect) + ".")
	print("The number of words added to dictionary is: " + str(wordAdded) + ".")
	print("The number of words changed by the user is: " + str(wordAccepted) + ".")
	print("The date and time the input was spellchecked was:  " + str(timeStart) + ".")
	print("The amount of time elapsed to spellcheck the input is: " + str(float(round(t1,4))) + " seconds.")
	break
print("\nProgram terminated!\n")