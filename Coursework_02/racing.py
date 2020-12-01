from tkinter import *
from time import *

def PlayButton():
	road.delete(Welcome)
	play.destroy()
	leaderboard.destroy()
	controls.destroy()
	quit.destroy()

	CarSeletion = road.create_text(800,300, fill="white",font=("arial", 75), text="Choose your car!")

	photoGreen = PhotoImage(file="car_green.png")
	carGreen = Button(road, image=photoGreen, height=200, width=99)
	carGreen.image = photoGreen
	carGreen_window = road.create_window(500,630, window=carGreen)

	photoOrange = PhotoImage(file="car_orange.png")
	carOrange = Button(road, image=photoOrange, height=200, width=99)
	carOrange.image = photoOrange
	carOrange_window = road.create_window(700,630, window=carOrange) 

	photoPurple = PhotoImage(file="car_purple.png")
	carPurple = Button(road, image=photoPurple, height=200, width=99)
	carPurple.image = photoPurple
	carPurple_window = road.create_window(900,630, window=carPurple) 

	photoRed = PhotoImage(file="car_red.png")
	carRed = Button(road, image=photoRed, height=200, width=99)
	carRed.image = photoRed
	carRed_window = road.create_window(1100,630, window=carRed)  

	#Game()

#def LeaderboardButton():

#def ControlsButton():


def QuitButton():
	root.destroy()


def Game():
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
		sleep (0.002)
		road.update()

#def mainMenu():
	#NA_menu = Frame(root, width=800, height=640, bg="red")
	#NA_menu.pack(side="top", fill="both", expand=True)
#
#	region = Label(root, text="Choose a region", font=("arial", 45))
#	NorthAmerica = Button(root, text="North America", font=("arial", 25), command=NA)
#	Europe = Button(root, text="Europe", font=("arial", 25))
#	Asia = Button(root, text="Asia", font=("arial", 25))
#
#	region.pack(padx=50, pady=100)
#	NorthAmerica.pack(pady=20)
#	Europe.pack(pady=20)
#	Asia.pack(pady=20)

#def showFrame(frame):
#	frame.pack()
#	frame.tkraise()

#def NA():
#	NA_menu = Frame(root, width=800, height=640, bg="red")
#	NA_menu.pack(fill="both", expand=1)
#	NA_menu.grid_row
#	text = Label(NA_menu, text="!!!!!!")
#	text.pack()
	#NA_menu = Frame(root, width=800, height=640, bg="red")
	#NA_menu.pack(fill="both", expand=1)


root = Tk()  
root.title("🄽🄴🄴🄳   🄵🄾🅁   🅂🄿🄴🄴🄳")
root.geometry("1600x900")

road = Canvas(root, width=1600, height=900)
road.pack()

road.config(bg="Black")

#----Main Menu---

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

#-----------------




root.mainloop()