import random

w, s, up, down, playing, ballUp, ballDown, ballLeft, ballRight = False, False, False, False, False, False, True, False, False

Red = "#F53457"
Blue = "#3B66D8"
Yellow = "#E3D44C"
White = "#FFFFFF"

name = "Pong"
instructions = "Press 'w' or 'a' To Start"

Player1 = None
Player2 = None
Ball1 = None

score = 0


def setup():
    global Player1, Player2, Ball1
    
    size(1000, 750)
    
    Player1 = Player(50, 375, 30, 125, 5, Red)
    Player2 = Player(950, 375, 30, 125, 5, Blue)
    Ball1 = Ball(500, 375, 30, 30, 5, White)
    
def draw():
    global name, instructions
    
    if playing == False:
        startGame()
        
    if playing == True: 
        background(0)              
        Player1.display()
        Player1.player1Move()
        Player1.boundaries()
        
        Player2.display()
        Player2.player2Move()
        Player2.boundaries()
        
        Ball1.display()
        Ball1.boundaries()
        Ball1.move()
    
def scoreCounter():
    global score
    score = (score + .1)

def startGame():
    global playing, space, instructions, White, w, a, s, d
    
    if playing == False:
        background(0)
        textAlign(CENTER, BOTTOM)
        textSize(25)
        fill(White)
        text(name, (width / 2), (height / 2))
        text(instructions, (width / 2), (height / 2) + 50)
        
    if up == True:
        playing = True
    if down == True:
        playing = True        
    if w == True:
        playing = True  
    if s == True:
        playing = True
    
#Creates a Player class
class Player:
    
    #Initializes the Player
    def __init__(self, x, y, sizeX, sizeY, vel, col):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.vel = vel
        self.col = col

    #Creates the Player's shape
    def display(self):
        fill(self.col)
        rectMode(CENTER)
        noStroke()
        rect(self.x, self.y, self.sizeX, self.sizeY)
    
    #Moves the Player in all directions
    def player1Move(self):       
        if w == True:
            self.y -= self.vel  
        if s == True:
            self.y += self.vel 
    
    def player2Move(self):
        if up == True:
            self.y -= self.vel  
        if down == True:
            self.y += self.vel 
            
    #Limits where the Player can go
    def boundaries(self):
        if self.y >= (height - self.sizeY / 2):
            self.y = (height - self.sizeY / 2)
        if self.y <= (self.sizeY / 2):
            self.y = (self.sizeY / 2)

    #Prevents from moving where Players are
    def collision(self):
        rightPlayer = (self.x + self.sizeX / 2)
        leftPlayer = (self.x - self.sizeX / 2)
        topPlayer = (self.y - self.sizeY / 2)
        bottomPlayer = (self.y + self.sizeY / 2)
        
        rightPlayer2 = (Player2.x + (Player2.sizeX / 2))
        leftPlayer2 = (Player2.x - (Player2.sizeX / 2))
        topPlayer2 = (Player2.y - (Player2.sizeY / 2))
        bottomPlayer2 = (Player2.y + (Player2.sizeY / 2))
            
        #Player2
        if rightPlayer >= leftPlayer2 and rightPlayer < (Player2.x - (Player2.sizeX/4)) and bottomPlayer > topPlayer2 and topPlayer < bottomPlayer2:
            self.x = (leftPlayer2 - self.sizeX / 2)
        elif leftPlayer <= rightPlayer2 and leftPlayer > (Player2.x + (Player2.sizeX/4)) and bottomPlayer > topPlayer2 and topPlayer < bottomPlayer2:
            self.x = (rightPlayer2 + self.sizeX / 2)
        elif bottomPlayer >= topPlayer2 and bottomPlayer < (Player2.y - (Player2.sizeY/4)) and rightPlayer > leftPlayer2 and leftPlayer < rightPlayer2:
            self.y = (topPlayer2 - self.sizeY / 2)
        elif topPlayer <= bottomPlayer2 and topPlayer > (Player2.y + (Player2.sizeY/4)) and rightPlayer > leftPlayer2 and leftPlayer < rightPlayer2:
            self.y = (bottomPlayer2 + self.sizeY / 2)
            
class Ball:
    #Initializes the Player
    def __init__(self, x, y, sizeX, sizeY, vel, col):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.vel = vel
        self.col = col

    #Creates the Player's shape
    def display(self):
        fill(self.col)
        ellipseMode(CENTER)
        noStroke()
        ellipse(self.x, self.y, self.sizeX, self.sizeY)
        
    def move(self):
        if ballUp == True:
            self.y -= self.vel
        if ballDown == True:
            self.y += self.vel
        if ballLeft == True:
            self.x -= self.vel
        if ballRight == True:
            self.x += self.vel

    def boundaries(self):
        if self.y >= (height - self.sizeY / 2):
            ballUp = True
            ballDown = False           
        if self.y <= (self.sizeY / 2):
            ballDown = True
            ballUp = False
            
#Creates a True value for the key pressed
def keyPressed():
    global w, s, up, down
    
    if key == "w":
        w = True
        playing = True
    if key == "s":
        s = True
        playing = True
    if keyCode == UP:
        up = True
        playing = True
    if keyCode == DOWN:
        down = True
        playing = True
            
#Causes the last key pressed to be continuous
def keyReleased():
    global w, s, up, down
    
    if key == "w":
        w = False
        playing = True
    if key == "s":
        s = False
        playing = True
    if keyCode == UP:
        up = False
        playing = True
    if keyCode == DOWN:
        down = False
        playing = True
