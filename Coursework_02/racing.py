from tkinter import *
from time import *

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
root.title("Input title here")
root.geometry("1600x900")

#Background
road = Canvas(root, width=1600, height=900)
road.pack()

road.config(bg="Black")

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

#lane = road.create_rectangle(0, 800, 30, 900, fill="white")
#lane = road.create_rectangle(314, 800, 344, 900, fill="white")
#lane = road.create_rectangle(628, 800, 658, 900, fill="white")
#lane = road.create_rectangle(942, 800, 972, 900, fill="white")
#lane = road.create_rectangle(1256, 800, 1286, 900, fill="white")
#lane = road.create_rectangle(1570, 800, 1600, 900, fill="white")

#lane = road.create_rectangle(0, 600, 30, 700, fill="white")
#lane = road.create_rectangle(0, 400, 30, 500, fill="white")
#lane = road.create_rectangle(0, 200, 30, 300, fill="white")
#lane = road.create_rectangle(0, 0, 30, 100, fill="white")
#lane.pack()



#mainMenu()

root.mainloop()