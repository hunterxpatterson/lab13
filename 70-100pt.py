#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="blue")

# Create your "enemies" here, before the class
enemy = drawpad.create_rectangle(50, 75, 100, 100, fill='red')
direction = 5

enemy1 = drawpad.create_rectangle(150, 175, 70, 200, fill='orange')
direction = 4

enemy2 = drawpad.create_rectangle(200, 250, 250, 300, fill='cyan')
direction = 3


def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy)
    if x2 > drawpad.winfo_width():
        drawpad.move(enemy, -750, 0)
    elif x1 < 0:
        direction = 5
    drawpad.move(enemy, direction, 0)
    drawpad.after(1, animate)
    
    
    
def animate1():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    if x2 > drawpad.winfo_width():
        drawpad.move(enemy1, -900, 0)
    elif x1 < 0:
        direction = 4
    drawpad.move(enemy1, direction, 0)
    drawpad.after(1, animate1)
    
    

def animate2():
    global direction
    x1, y1, x2, y2 = drawpad.coords(enemy2)
    if x2 > drawpad.winfo_width():
        drawpad.move(enemy2, -600, 0)
    elif x1 < 0:
        direction = 3
    drawpad.move(enemy2, direction, 0)
    drawpad.after(1, animate2)
        
        
        
    
class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "yellow")
       	    self.down.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "red")
       	    self.left.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "blue")
       	    self.right.grid(row=0,column=3)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    
       	    
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
		
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
		

app = MyApp(root)
animate()
animate1()
animate2()
root.mainloop()