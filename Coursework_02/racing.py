from tkinter import *
from time import *
from random import *

def MainMenu():
	global Welcome, play, leaderboard, controls, quit

	Welcome = road.create_text(800,150, fill="white",font=("arial", 75), text="Welcome to my game!")

	play = Button(road, text="Play", font=("arial", 25), command=PlayButton)
	play.configure(width = 10, relief = FLAT)
	road.create_window(800, 350, window=play)

	leaderboard = Button(road, text="Leaderboard", font=("arial", 25))
	leaderboard.configure(width = 10, relief = FLAT)
	road.create_window(800, 450, window=leaderboard)

	controls = Button(road, text="Controls", font=("arial", 25))
	controls.configure(width = 10, relief = FLAT)
	road.create_window(800, 550, window=controls)

	quit = Button(road, text="Quit", font=("arial", 25), command=QuitButton)
	quit.configure(width = 10, relief = FLAT)
	road.create_window(800, 650, window=quit)

def MainMenuEnd():
	backMenu, finalScore, nameTxt, nameEntry
	road.delete(finalScore,nameTxt)
	nameEntry.destroy()
	backMenu.destroy()
	MainMenu()	

def PlayButton():
	road.delete(Welcome)
	play.destroy()
	leaderboard.destroy()
	controls.destroy()
	quit.destroy()

	global CarSeletion, carGreen, carRed, carPurple, carOrange

	CarSeletion = road.create_text(800,300, fill="white",font=("arial", 75), text="Choose your car!")

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

#def LeaderboardButton():

#def ControlsButton():


def QuitButton():
	root.destroy()


def Game(car):

	def left(event):
		carPos = road.coords(carPhoto)
		if(carPos[0] > 300):
			road.move(carPhoto,-314,0)
			carPos = road.coords(carPhoto)

	def right(event):
		carPos = road.coords(carPhoto)
		if(carPos[0] < 1200):
			road.move(carPhoto,314,0)
			carPos = road.coords(carPhoto)

	def collisionDetection():
		playerBbox = road.bbox(carPhoto)
		car1Bbox = road.bbox(obstaclePhoto)
		car2Bbox = road.bbox(obstaclePhoto2)
		car3Bbox = road.bbox(obstaclePhoto3)
		if( (playerBbox[0] < car1Bbox[2] and playerBbox[2] > car1Bbox[0] and
			playerBbox[1] < car1Bbox[3] and playerBbox[3] > car1Bbox[1]) or
			(playerBbox[0] < car2Bbox[2] and playerBbox[2] > car2Bbox[0] and
			playerBbox[1] < car2Bbox[3] and playerBbox[3] > car2Bbox[1]) or
			(playerBbox[0] < car3Bbox[2] and playerBbox[2] > car3Bbox[0] and
			playerBbox[1] < car3Bbox[3] and playerBbox[3] > car3Bbox[1]) ):
			gameOver()

	global carPhoto, scoreTxt, lane, obstaclePhoto, obstaclePhoto2, obstaclePhoto3, score

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
	root.bind("<Left>", left)
	root.bind("<Right>", right)	

	lane = []
	x=314
	y=0
	sizex=30
	sizey=100
	carOnScreen=False
	carOnScreen2=False
	carOnScreen3=False

	for i in range (4):
		for j in range(5):
			lane.append(road.create_rectangle(x, y, x+sizex, y+sizey, fill="white"))
			y += 200
		x += 314
		y = 0

	road.create_rectangle(0,0,30,900,fill="white")
	road.create_rectangle(1570,0,1600,900,fill="white")

	score = 0
	scoreTxt = road.create_text(170,50, fill="white",font=("arial", 35), text=("Score:",score))
	
	while True:
		for i in range(len(lane)):
			pos = road.coords(lane[i])
			if pos[1] > 900:
				road.coords(lane[i], pos[0], -100, pos[2], 0)				#teleports lane up
			road.move(lane[i],0,1)
		sleep (0.001)

		#-----car #1------
		
		if (carOnScreen == False):
			laneCar = randint(0,4)
			colourCar = randint(1,4)
			if (colourCar == 1):
				obstaclePNG = PhotoImage(file="car_green.png")
			elif (colourCar == 2):
				obstaclePNG = PhotoImage(file="car_orange.png")
			elif (colourCar == 3):
				obstaclePNG = PhotoImage(file="car_purple.png")
			else:
				obstaclePNG = PhotoImage(file="car_red.png")
			obstaclePhoto = road.create_image(172 + 314 * laneCar, -75, image=obstaclePNG)	
			carOnScreen = True
		else:
			obstaclePos = road.coords(obstaclePhoto)
			if (obstaclePos[1] < 975):
				road.move(obstaclePhoto,0,3)
			else:
				carOnScreen = False
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
				road.move(obstaclePhoto2,0,3)
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
				road.move(obstaclePhoto3,0,3)
			else:
				carOnScreen3 = False

		collisionDetection()

		#-----Score-----
		#
		if (carOnScreen == False):
			road.delete(scoreTxt)
			score = score +10
			scoreTxt = road.create_text(170,50, fill="white",font=("arial", 35), text=("Score:",score))

		road.update()

def gameOver():

	global backMenu, finalScore, nameTxt, nameEntry

	for i in range(len(lane)):
		road.delete(lane[i])
	road.delete(obstaclePhoto, obstaclePhoto2, obstaclePhoto3, carPhoto, scoreTxt)

	finalScore = road.create_text(800,200, fill="white",font=("arial", 75), text=("Score:",score))
	nameTxt = road.create_text(700,600, fill="white", font=("arial", 45), text="Name:")
	nameEntry = Entry(road, bd=0, font=("arial", 45), width=10, bg="Black", fg="white")
	road.create_window(960,600, window=nameEntry)

	backMenu = Button(road, text="Main Menu", font=("arial", 25), command=MainMenuEnd)
	backMenu.configure(width = 10, relief = FLAT)
	road.create_window(800, 700, window=backMenu)
	


root = Tk()  
root.title("🄽🄴🄴🄳   🄵🄾🅁   🅂🄿🄴🄴🄳")
root.geometry("1600x900")

road = Canvas(root, width=1600, height=900)
road.pack()

road.config(bg="Black")

MainMenu()

root.mainloop()