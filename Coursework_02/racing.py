from tkinter import *
from time import *

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

	global carPhoto

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
	for i in range (4):
		for j in range(5):
			lane.append(road.create_rectangle(x, y, x+sizex, y+sizey, fill="white"))
			y += 200
		x += 314
		y = 0
	road.create_rectangle(0,0,30,900,fill="white")
	road.create_rectangle(1570,0,1600,900,fill="white")
	
	while True:


		for i in range(len(lane)):
			pos = road.coords(lane[i])
			if pos[1] > 900:
				road.coords(lane[i], pos[0], -100, pos[2], 0)
			road.move(lane[i],0,1)
		sleep (0.0005)
		road.update()


root = Tk()  
root.title("🄽🄴🄴🄳   🄵🄾🅁   🅂🄿🄴🄴🄳")
root.geometry("1600x900")

road = Canvas(root, width=1600, height=900)
road.pack()

road.config(bg="Black")



MainMenu()

root.mainloop()