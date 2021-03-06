#1600x900

from tkinter import *								#|											
from time import *									#| Imports
from random import *								#|

#-----The main menu, the first thing the player sees-----

def MainMenu():
	global Welcome, play, leaderboard, controls, quit, nameScore, topScore

	Welcome = road.create_text(800,150, fill="white",font=("arial", 75), text="Welcome to my game!")

	play = Button(road, text="Play", font=("arial", 25), command=PlayButton)
	play.configure(width = 10, relief = FLAT)
	road.create_window(800, 350, window=play)

	leaderboard = Button(road, text="Leaderboard", font=("arial", 25), command=LeaderboardButton)
	leaderboard.configure(width = 10, relief = FLAT)
	road.create_window(800, 450, window=leaderboard)

	controls = Button(road, text="Controls", font=("arial", 25))
	controls.configure(width = 10, relief = FLAT)
	road.create_window(800, 550, window=controls)

	quit = Button(road, text="Quit", font=("arial", 25), command=QuitButton)
	quit.configure(width = 10, relief = FLAT)
	road.create_window(800, 650, window=quit)

#-----Main menu end is just a function that deletes the widgets when the game loops back to the menu----- 

def MainMenuEnd():
	backMenu, finalScore, nameTxt, nameEntry
	road.delete(finalScore,nameTxt)
	nameEntry.destroy()
	backMenu.destroy()
	MainMenu()	

#-----The play button that takes the player to the car selection menu-----

def PlayButton():

	global CarSeletion, carGreen, carRed, carPurple, carOrange

	#---Clears the screen of widgets---

	road.delete(Welcome)
	play.destroy()
	leaderboard.destroy()
	controls.destroy()
	quit.destroy()

	CarSeletion = road.create_text(800,300, fill="white",font=("arial", 75), text="Choose your car!")

	#---Each car button widget---

	photoGreen = PhotoImage(file="car_green.png")
	carGreen = Button(road, image=photoGreen, height=200, width=99, command= lambda: Game("green"))
	carGreen.image = photoGreen
	carGreen_window = road.create_window(500,630, window=carGreen)

	photoOrange = PhotoImage(file="car_orange.png")
	carOrange = Button(road, image=photoOrange, height=200, width=99, command= lambda: Game("orange"))
	carOrange.image = photoOrange
	carOrange_window = road.create_window(700,630, window=carOrange) 

	photoPurple = PhotoImage(file="car_purple.png")
	carPurple = Button(road, image=photoPurple, height=200, width=99, command= lambda: Game("purple"))
	carPurple.image = photoPurple
	carPurple_window = road.create_window(900,630, window=carPurple) 

	photoRed = PhotoImage(file="car_red.png")
	carRed = Button(road, image=photoRed, height=200, width=99, command= lambda: Game("red"))
	carRed.image = photoRed
	carRed_window = road.create_window(1100,630, window=carRed)  

#-----The leaderboard button that takes the player to the local leaderboard-----

def LeaderboardButton():

	global nameScore, topScore, back, top1, top2, top3, top4, top5, leaderboardTxt

	#---Clears the screen of widgets---

	road.delete(Welcome)
	play.destroy()
	leaderboard.destroy()
	controls.destroy()
	quit.destroy()

	leaderboardTxt = road.create_text(800,150, fill="white",font=("arial", 75), text="Leaderboard")

	#---The top scores shown in the leaderboard menu---

	top1 = road.create_text(800,300, fill="white",font=("arial", 40), text=(nameScore[0],"---",topScore[0]))
	top2 = road.create_text(800,400, fill="white",font=("arial", 40), text=(nameScore[1],"---",topScore[1]))
	top3 = road.create_text(800,500, fill="white",font=("arial", 40), text=(nameScore[2],"---",topScore[2]))
	top4 = road.create_text(800,600, fill="white",font=("arial", 40), text=(nameScore[3],"---",topScore[3]))
	top5 = road.create_text(800,700, fill="white",font=("arial", 40), text=(nameScore[4],"---",topScore[4]))

	back = Button(road, text="Back", font=("arial", 25), command=leaderboard_to_mainmenu)
	back.configure(width = 10, relief = FLAT)
	road.create_window(800, 800, window=back)

#-----A transition function that delets the widgets from the leaderboard menu when the player returns to the main menu-----

def leaderboard_to_mainmenu():
	road.delete(top1,top2,top3,top4,top5, leaderboardTxt)
	back.destroy()
	MainMenu()

#-----The control menu buttons (I did not know how to customize the controls fr the player)-----

#def ControlsButton():

#-----The quit button that simply terminates the program-----

def QuitButton():
	root.destroy()

#-----The main game function that loops until cars collide-----

def Game(car):

	def is_paused(event):						#|
												#|
		control = 0								#|
												#|
	def is_continued(event):					#|
												#|
		control = 1								#|
												#| A shot at implemnting a pause option. The pause function worked
	def controler():							#|
												#| but I did not know how to unpause and resume the game.
		if not control:							#|
			sleep(0.2)							#|
			controler()							#|
		else:									#|
			pass								#|

	def cheat(event):							#|
												#| A cheat that increases score with 100 everytime C is pressed
		global score 							#| 
		score += 100							#|

	def left(event):							#|
												#|
		carPos = road.coords(carPhoto)			#|
		if(carPos[0] > 300):					#|
			road.move(carPhoto,-314,0)			#|
			carPos = road.coords(carPhoto)		#|
												#| The movement of the player
	def right(event):							#|
												#|
		carPos = road.coords(carPhoto)			#|
		if(carPos[0] < 1200):					#|
			road.move(carPhoto,314,0)			#|
			carPos = road.coords(carPhoto)		#|

	def collisionDetection():

		playerBbox = road.bbox(carPhoto)		#|
		car1Bbox = road.bbox(obstaclePhoto)		#| Code that creates a rectangle that surrounds the player and the enemies
		car2Bbox = road.bbox(obstaclePhoto2)	#|
		car3Bbox = road.bbox(obstaclePhoto3)	#|

		if( (playerBbox[0] < car1Bbox[2] and playerBbox[2] > car1Bbox[0] and 	#|
			playerBbox[1] < car1Bbox[3] and playerBbox[3] > car1Bbox[1]) or 	#|
			(playerBbox[0] < car2Bbox[2] and playerBbox[2] > car2Bbox[0] and 	#| If collision between player and other cars
			playerBbox[1] < car2Bbox[3] and playerBbox[3] > car2Bbox[1]) or 	#|
			(playerBbox[0] < car3Bbox[2] and playerBbox[2] > car3Bbox[0] and 	#|
			playerBbox[1] < car3Bbox[3] and playerBbox[3] > car3Bbox[1]) ):		#|

			root.unbind("<c>")					# Unbinds the cheat to not be aplied when user writes his name
			gameOver()

	global carPhoto, scoreTxt, lane, obstaclePhoto, obstaclePhoto2, obstaclePhoto3, score, control, nameScore, topScore

	if (car == "green"):							
		carPNG = PhotoImage(file="car_green.png")
	elif (car == "orange"):
		carPNG = PhotoImage(file="car_orange.png")	
	elif (car == "purple"):
		carPNG = PhotoImage(file="car_purple.png")
	else:
		carPNG = PhotoImage(file="car_red.png")	

	road.delete(CarSeletion)
	carGreen.destroy()
	carOrange.destroy()
	carRed.destroy()
	carPurple.destroy()

	carPhoto = road.create_image(800,795, image=carPNG)

	root.bind("<Left>", left)			#|
	root.bind("<Right>", right)			#|
	root.bind("<Escape>", is_paused)	#| Control bind
	root.bind("<Enter>", is_continued)	#|
	root.bind("<c>", cheat)				#|

	lane = []							#|
	x=314								#|
	y=0									#| Background variable declaration
	sizex=30							#|
	sizey=100							#|

	carOnScreen=False 					#|
	carOnScreen2=False 					#| Boolean if obstacle is on screen
	carOnScreen3=False 					#|

	speed = 2							#| Variables for car speed
	scoreThreshold = 90					#|

	control = 1
	
	#---Background lanes loop---

	for i in range (4):
		for j in range(5):
			lane.append(road.create_rectangle(x, y, x+sizex, y+sizey, fill="white"))
			y += 200
		x += 314
		y = 0

	#---Side white lanes---

	road.create_rectangle(0,0,30,900,fill="white")
	road.create_rectangle(1570,0,1600,900,fill="white")

	#---Initial instance of score---

	score = 0
	scoreTxt = road.create_text(170,50, fill="white",font=("arial", 35), text=("Score:",score))
	
	#---Main game loop---

	while True:
		for i in range(len(lane)):								#|
			pos = road.coords(lane[i])							#|
			if pos[1] > 900:									#| Every time a lane reaches the bottom it is
				road.coords(lane[i], pos[0], -100, pos[2], 0)	#| teleported back up 
			road.move(lane[i],0,1)								#|
		sleep (0.001)											#|

		if (score > scoreThreshold):							#| Speed of cars increases every time score is
			speed += 1											#| a multiple of 100
			scoreThreshold += 100								#| 

		#-----car #1------
		
		if (carOnScreen == False):								# If car has passed the edge of the screen

			laneCar = randint(0,4)								#| Randomizes the colour and lane of the obstacles
			colourCar = randint(1,4)							#|

			if (colourCar == 1):								#|
				obstaclePNG = PhotoImage(file="car_green.png")	#|
			elif (colourCar == 2):								#|
				obstaclePNG = PhotoImage(file="car_orange.png")	#| Selects the colour of the car
			elif (colourCar == 3):								#| 
				obstaclePNG = PhotoImage(file="car_purple.png")	#|
			else:												#|
				obstaclePNG = PhotoImage(file="car_red.png")	#|

			obstaclePhoto = road.create_image(172 + 314 * laneCar, -75, image=obstaclePNG) #Creates car obstacle	
			carOnScreen = True

		else:													# If car is on screen

			obstaclePos = road.coords(obstaclePhoto)

			if (obstaclePos[1] < 975):							#|
				road.move(obstaclePhoto,0,speed)				#| Moves car obstacle "speed" pixels down 	
			else:												#|
				carOnScreen = False 							#|

			sleep(0.001)	

		#-----car #2-----

		if (carOnScreen2 == False):		
			laneCar = randint(0,4)
			colourCar = randint(1,4)
			if (colourCar == 1):
				obstaclePNG2 = PhotoImage(file="car_green.png")
			elif (colourCar == 2):
				obstaclePNG2 = PhotoImage(file="car_orange.png")
			elif (colourCar == 3):
				obstaclePNG2 = PhotoImage(file="car_purple.png")
			else:
				obstaclePNG2 = PhotoImage(file="car_red.png")
			obstaclePhoto2 = road.create_image(172 + 314 * laneCar, -75, image=obstaclePNG2)

			carOnScreen2 = True
		else:
			obstaclePos2 = road.coords(obstaclePhoto2)
			if (obstaclePos2[1] < 975):
				road.move(obstaclePhoto2,0,speed)
			else:
				carOnScreen2 = False

		#------ car #3------
		
		if (carOnScreen3 == False):		
			laneCar = randint(0,4)
			colourCar = randint(1,4)
			if (colourCar == 1):
				obstaclePNG3 = PhotoImage(file="car_green.png")
			elif (colourCar == 2):
				obstaclePNG3 = PhotoImage(file="car_orange.png")
			elif (colourCar == 3):
				obstaclePNG3 = PhotoImage(file="car_purple.png")
			else:
				obstaclePNG3 = PhotoImage(file="car_red.png")
			obstaclePhoto3 = road.create_image(172 + 314 * laneCar, -75, image=obstaclePNG3)

			carOnScreen3 = True
		else:
			obstaclePos3 = road.coords(obstaclePhoto3)
			if (obstaclePos3[1] < 975):
				road.move(obstaclePhoto3,0,speed)
			else:
				carOnScreen3 = False

		collisionDetection()

		#-----Score-----
		
		if (carOnScreen == False):
			road.delete(scoreTxt)
			score = score +10
			scoreTxt = road.create_text(170,50, fill="white",font=("arial", 35), text=("Score:",score))

		controler()

		road.update()

def gameOver(): 												# If collision is detected

	global backMenu, finalScore, nameTxt, nameEntry, nameScore, topScore

	for i in range(len(lane)):
		road.delete(lane[i])
	road.delete(obstaclePhoto, obstaclePhoto2, obstaclePhoto3, carPhoto, scoreTxt)

	finalScore = road.create_text(800,200, fill="white",font=("arial", 75), text=("Score:",score))
	nameTxt = road.create_text(700,600, fill="white", font=("arial", 45), text="Name:")
	nameEntry = Entry(road, bd=0, font=("arial", 45), width=10, bg="Black", fg="white")
	road.create_window(960,600, window=nameEntry)

	backMenu = Button(road, text="Main Menu", font=("arial", 25), command=leaderboardStore)
	backMenu.configure(width = 10, relief = FLAT)
	road.create_window(800, 700, window=backMenu)

def leaderboardStore():											# Stores score and username
	global topScore, nameScore

	i=0
	for i in range(3):
		if (score > topScore[i]):
			for j in range(2, i, -1):
				topScore[j] = topScore[j-1]
				nameScore[j] = nameScore[j-1]
			topScore[i] = score
			nameScore[i] = nameEntry.get()
			break
	MainMenuEnd()
	
#-----Tkinter initialisation-----

root = Tk()  
root.title("????????????????   ????????????   ????????????????????")
root.geometry("1600x900")

road = Canvas(root, width=1600, height=900)
road.pack()

road.config(bg="Black")

topScore = [0,0,0,0,0]
nameScore=["no_name", "no_name", "no_name", "no_name", "no_name"]

MainMenu()

root.mainloop()