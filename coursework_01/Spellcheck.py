import os.path
print("Press 1 if you want to spell check a sentence.", "\nPress 2 if you want to spell check a file.", "\nPress 0 if you want to quit the program.")
var = int(input())
while(var > 2 or var < 0):
	print("Invalid entry. Try again!")
	var = int(input())
while(var != 0):
	if(var == 1):
		sentence = input("PLease input the sentence: ")
		print(sentence)
		break
	elif(var == 2):
		filePath = input("Please enter the file name: ")
		if(os.path.isfile(filePath)):
			sentence = open(filePath, 'r')
			print(sentence.read())
			sentence.close()
			break
		else:
			print("Invalid path. Try again!")
print("Program terminated!")