import random

w, a, s, d, space = False, False, False, False, False

Red = "#CE6269"
Blue = "#1260C9"
Yellow = "#E3D44C"
White = "#FFFFFF"
Green = "#A0C19E"
Grey = "#74696A"

Player = None
Monster1 = None
Fog = None
Finish = None

Block1, Block2, Block3, Block4 = None, None, None, None
Block5, Block6, Block7, Block8 = None, None, None, None

monster1Direction = 4
timer = 0

lives = 3
status = "home"


def setup():
    global Player, Monster1, Fog, Finish
    global Block1, Block2, Block3, Block4
    global Block5, Block6, Block7, Block8
    
    size(1250, 1250)
    
    Player = Player(60, 60, 25, 5, Green)
    Monster1 = Monster(100, 200, 25, 5, Red)
    Fog = Fog(Player.x, Player.y, 2500, 2500)
    Finish = Block(1198, 1198, 25, 25, Blue)
    
    Block1 = Block(20, height/2, 40, height, Grey) #left wall
    Block2 = Block(width/2, 20, width - 80, 40,Grey) #top wall
    Block3 = Block(1230, height/2, 40, height, Grey) #right wall
    Block4 = Block(width/2, height - 20, width - 80, 40, Grey) #bottom wall
    
    Block5 = Block(110, 183, 40, 285, Grey)
    Block6 = Block(110, 520, 40, 285, Grey)
    Block7 = Block(273, 397, 285, 40, Grey)
    Block8 = Block(273, 305, 285, 40, Grey)
    
def draw():
    background("#83A0CE")
    
    if status == "home":
        Home()
        
    if status == "game":
        Game()
        
    if status == "win":
        Win()
        
    if status == "lose":
        Lose()
        
def Home():
    Player.x = 60
    Player.y = 60
    Monster1.x = 60
    Monster1.y = 300
    textSize(100)
    fill(0)
    textAlign(CENTER, BOTTOM)
    text("MAZE", width/2, height/2)
    textSize(50)
    text("Press 'Spacebar' To Play", width/2, height/2 + 50)
    
def Win():
    textSize(100)
    fill(0)
    textAlign(CENTER, BOTTOM)
    text("YOU WIN", width/2, height/2)
    textSize(50)
    text("Press 'Spacebar' To Play Again", width/2, height/2 + 50)
    
def Lose():
    textSize(100)
    fill(0)
    textAlign(CENTER, BOTTOM)
    text("YOU LOSE", width/2, height/2)
    textSize(50)
    text("Press 'Spacebar' To Play Again", width/2, height/2 + 50)
    
def Game():
    global status
    
    timeCounter()
    Player.display()
    Player.move()
    Player.collision()
    
    Monster1.display()
    Monster1.move()
    Monster1.collision()
    
    Finish.display()
    
    Block1.display()
    Block2.display()
    Block3.display()
    Block4.display()
    Block5.display()
    Block6.display()
    Block7.display()
    Block8.display()
    
    Player.colorDetection()
    
    #Fog.display()
    
    textSize(25)
    fill(0)
    textAlign(CENTER, BOTTOM)
    text("Lives: " + str(lives), 100, 35)
    
    if lives == 0:
        status = "lose"
    
def timeCounter():
    global timer
    timer = timer + 1    
    
#Creates a Player class
class Player:
    
    #Initializes the Player
    def __init__(self, x, y, Size, vel, col):
        self.x = x
        self.y = y
        self.Size = Size
        self.vel = vel
        self.col = col

    #Creates the Player's shape
    def display(self):
        fill(self.col)
        rectMode(CENTER)
        rect(self.x, self.y, self.Size, self.Size)
    
    #Moves Player1 in all directions
    def move(self):
        if a == True:
            self.x -= self.vel
        if d == True:
            self.x += self.vel        
        if w == True:
            self.y -= self.vel  
        if s == True:
            self.y += self.vel 
            
    def computerMove(self):
        scoreCounter()
        # 0 = left 
        #1 = right 
        #2 = up
        #3 = down            
        if direction == 0:
            self.x -= 5
        elif direction == 1:
            self.x += 5
        elif direction == 2:
            self.y -= 5
        elif direction == 3:
            self.y += 5
            
    #Prevents from moving where Players are
    def collision(self):
        rightPlayer = (self.x + self.Size / 2)
        leftPlayer = (self.x - self.Size / 2)
        topPlayer = (self.y - self.Size / 2)
        bottomPlayer = (self.y + self.Size / 2)
        
        rightBlock1 = (Block1.x + (Block1.sizeX / 2))
        leftBlock1 = (Block1.x - (Block1.sizeX / 2))
        topBlock1 = (Block1.y - (Block1.sizeY / 2))
        bottomBlock1 = (Block1.y + (Block1.sizeY / 2))
            
        if leftPlayer <= rightBlock1 and leftPlayer > (Block1.x + (Block1.sizeX/4)) and bottomPlayer > topBlock1 and topPlayer < bottomBlock1:
            self.x = (rightBlock1 + self.Size / 2)
            
        rightBlock2 = (Block2.x + (Block2.sizeX / 2))
        leftBlock2 = (Block2.x - (Block2.sizeX / 2))
        topBlock2 = (Block2.y - (Block2.sizeY / 2))
        bottomBlock2 = (Block2.y + (Block2.sizeY / 2))
            
        if topPlayer <= bottomBlock2 and topPlayer > (Block2.y + (Block2.sizeY/4)) and rightPlayer > leftBlock2 and leftPlayer < rightBlock2:
            self.y = (bottomBlock2 + self.Size / 2)
            
        rightBlock3 = (Block3.x + (Block3.sizeX / 2))
        leftBlock3 = (Block3.x - (Block3.sizeX / 2))
        topBlock3 = (Block3.y - (Block3.sizeY / 2))
        bottomBlock3 = (Block3.y + (Block3.sizeY / 2))
            
        if rightPlayer >= leftBlock3 and rightPlayer < (Block3.x - (Block3.sizeX/4)) and bottomPlayer > topBlock3 and topPlayer < bottomBlock3:
            self.x = (leftBlock3 - self.Size / 2)
            
        rightBlock4 = (Block4.x + (Block4.sizeX / 2))
        leftBlock4 = (Block4.x - (Block4.sizeX / 2))
        topBlock4 = (Block4.y - (Block4.sizeY / 2))
        bottomBlock4 = (Block4.y + (Block4.sizeY / 2))
            
        if bottomPlayer >= topBlock4 and bottomPlayer < (Block4.y - (Block4.sizeY/4)) and rightPlayer > leftBlock4 and leftPlayer < rightBlock4:
            self.y = (topBlock4 - self.Size / 2)
    
        rightBlock5 = (Block5.x + (Block5.sizeX / 2))
        leftBlock5 = (Block5.x - (Block5.sizeX / 2))
        topBlock5 = (Block5.y - (Block5.sizeY / 2))
        bottomBlock5 = (Block5.y + (Block5.sizeY / 2))
            
        if rightPlayer >= leftBlock5 and rightPlayer < (Block5.x - (Block5.sizeX/4)) and bottomPlayer > topBlock5 and topPlayer < bottomBlock5:
            self.x = (leftBlock5 - self.Size / 2)
        elif leftPlayer <= rightBlock5 and leftPlayer > (Block5.x + (Block5.sizeX/4)) and bottomPlayer > topBlock5 and topPlayer < bottomBlock5:
            self.x = (rightBlock5 + self.Size / 2)
        elif bottomPlayer >= topBlock5 and bottomPlayer < (Block5.y - (Block5.sizeY/4)) and rightPlayer > leftBlock5 and leftPlayer < rightBlock5:
            self.y = (topBlock5 - self.Size / 2)
        elif topPlayer <= bottomBlock5 and topPlayer > (Block5.y + (Block5.sizeY/4)) and rightPlayer > leftBlock5 and leftPlayer < rightBlock5:
            self.y = (bottomBlock5 + self.Size / 2)
            
        rightBlock6 = (Block6.x + (Block6.sizeX / 2))
        leftBlock6 = (Block6.x - (Block6.sizeX / 2))
        topBlock6 = (Block6.y - (Block6.sizeY / 2))
        bottomBlock6 = (Block6.y + (Block6.sizeY / 2))
            
        if rightPlayer >= leftBlock6 and rightPlayer < (Block6.x - (Block6.sizeX/4)) and bottomPlayer > topBlock6 and topPlayer < bottomBlock6:
            self.x = (leftBlock6 - self.Size / 2)
        elif leftPlayer <= rightBlock6 and leftPlayer > (Block6.x + (Block6.sizeX/4)) and bottomPlayer > topBlock6 and topPlayer < bottomBlock6:
            self.x = (rightBlock6 + self.Size / 2)
        elif bottomPlayer >= topBlock6 and bottomPlayer < (Block6.y - (Block6.sizeY/4)) and rightPlayer > leftBlock6 and leftPlayer < rightBlock6:
            self.y = (topBlock6 - self.Size / 2)
        elif topPlayer <= bottomBlock6 and topPlayer > (Block6.y + (Block6.sizeY/4)) and rightPlayer > leftBlock6 and leftPlayer < rightBlock6:
            self.y = (bottomBlock6 + self.Size / 2)  
            
        rightBlock7 = (Block7.x + (Block7.sizeX / 2))
        leftBlock7 = (Block7.x - (Block7.sizeX / 2))
        topBlock7 = (Block7.y - (Block7.sizeY / 2))
        bottomBlock7 = (Block7.y + (Block7.sizeY / 2))
            
        if rightPlayer >= leftBlock7 and rightPlayer < (Block7.x - (Block7.sizeX - 5)) and bottomPlayer > topBlock7 and topPlayer < bottomBlock7:
            self.x = (leftBlock7 - self.Size / 2)
        elif leftPlayer <= rightBlock7 and leftPlayer > (Block7.x + (Block7.sizeX - 5)) and bottomPlayer > topBlock7 and topPlayer < bottomBlock7:
            self.x = (rightBlock7 + self.Size / 2)
        elif bottomPlayer >= topBlock7 and bottomPlayer < (Block7.y - (Block7.sizeY/4)) and rightPlayer > leftBlock7 and leftPlayer < rightBlock7:
            self.y = (topBlock7 - self.Size / 2)
        elif topPlayer <= bottomBlock7 and topPlayer > (Block7.y + (Block7.sizeY/4)) and rightPlayer > leftBlock7 and leftPlayer < rightBlock7:
            self.y = (bottomBlock7 + self.Size / 2) 
            
        rightBlock8 = (Block8.x + (Block8.sizeX / 2))
        leftBlock8 = (Block8.x - (Block8.sizeX / 2))
        topBlock8 = (Block8.y - (Block8.sizeY / 2))
        bottomBlock8 = (Block8.y + (Block8.sizeY / 2))
            
        if rightPlayer >= leftBlock8 and rightPlayer < (Block8.x - (Block8.sizeX-5)) and bottomPlayer > topBlock8 and topPlayer < bottomBlock8:
            self.x = (leftBlock8 - self.Size / 2)
        elif leftPlayer <= rightBlock8 and leftPlayer > (Block8.x + (Block8.sizeX-5)) and bottomPlayer > topBlock8 and topPlayer < bottomBlock8:
            self.x = (rightBlock8 + self.Size / 2)
        elif bottomPlayer >= topBlock8 and bottomPlayer < (Block8.y - (Block8.sizeY/4)) and rightPlayer > leftBlock8 and leftPlayer < rightBlock8:
            self.y = (topBlock8 - self.Size / 2)
        elif topPlayer <= bottomBlock8 and topPlayer > (Block8.y + (Block8.sizeY/4)) and rightPlayer > leftBlock8 and leftPlayer < rightBlock8:
            self.y = (bottomBlock8 + self.Size / 2)  
    
    def colorDetection(self):
        global lives, status
        c = color(206, 98, 105)
        c2 = color(18, 96, 201)
        
        rightPlayer = get(self.x + self.Size / 2, self.y)
        leftPlayer = get(self.x - self.Size / 2, self.y)
        topPlayer = get(self.x, self.y - self.Size / 2)
        bottomPlayer = get(self.x, self.y + self.Size / 2)
        
        if rightPlayer == c:
            self.x = 50
            self.y = 50
            lives -= 1
        elif leftPlayer == c:
            self.x = 50
            self.y = 50
            lives -= 1
        elif topPlayer == c:
            self.x = 50
            self.y = 50
            lives -= 1
        elif bottomPlayer == c:
            self.x = 50
            self.y = 50
            lives -= 1
        elif rightPlayer == c2:
            status = "win"
        elif leftPlayer == c2:
            status = "win"
        elif topPlayer == c2:
            status = "win"
        elif bottomPlayer == c2:
            status = "win"
            
class Monster():
    #Initializes the Player
    def __init__(self, x, y, Size, vel, col):
        self.x = x
        self.y = y
        self.Size = Size
        self.vel = vel
        self.col = col

    #Creates the Player's shape
    def display(self):
        fill(self.col)
        rectMode(CENTER)
        rect(self.x, self.y, self.Size, self.Size)
    
    #Moves Player1 in all directions
    def move(self):
        global monster1Direction
        
        if (timer % 60) == 0:
            monster1Direction = random.randint(1, 4)
            
        if monster1Direction == 1:
            self.x -= self.vel
        elif monster1Direction == 2:
            self.x += self.vel        
        elif monster1Direction == 3:
            self.y -= self.vel  
        elif monster1Direction == 4:
            self.y += self.vel
            
    def collision(self):
        rightMonster1 = (self.x + self.Size / 2)
        leftMonster1 = (self.x - self.Size / 2)
        topMonster1 = (self.y - self.Size / 2)
        bottomMonster1 = (self.y + self.Size / 2)
        
        rightBlock1 = (Block1.x + (Block1.sizeX / 2))
        leftBlock1 = (Block1.x - (Block1.sizeX / 2))
        topBlock1 = (Block1.y - (Block1.sizeY / 2))
        bottomBlock1 = (Block1.y + (Block1.sizeY / 2))
            
        if leftMonster1 <= rightBlock1 and leftMonster1 > (Block1.x + (Block1.sizeX/4)) and bottomMonster1 > topBlock1 and topMonster1 < bottomBlock1:
            self.x = (rightBlock1 + self.Size / 2)
            
        rightBlock2 = (Block2.x + (Block2.sizeX / 2))
        leftBlock2 = (Block2.x - (Block2.sizeX / 2))
        topBlock2 = (Block2.y - (Block2.sizeY / 2))
        bottomBlock2 = (Block2.y + (Block2.sizeY / 2))
            
        if topMonster1 <= bottomBlock2 and topMonster1 > (Block2.y + (Block2.sizeY/4)) and rightMonster1 > leftBlock2 and leftMonster1 < rightBlock2:
            self.y = (bottomBlock2 + self.Size / 2)
            
        rightBlock3 = (Block3.x + (Block3.sizeX / 2))
        leftBlock3 = (Block3.x - (Block3.sizeX / 2))
        topBlock3 = (Block3.y - (Block3.sizeY / 2))
        bottomBlock3 = (Block3.y + (Block3.sizeY / 2))
            
        #Block3
        if rightMonster1 >= leftBlock3 and rightMonster1 < (Block3.x - (Block3.sizeX/4)) and bottomMonster1 > topBlock3 and topMonster1 < bottomBlock3:
            self.x = (leftBlock3 - self.Size / 2)
            
        rightBlock4 = (Block4.x + (Block4.sizeX / 2))
        leftBlock4 = (Block4.x - (Block4.sizeX / 2))
        topBlock4 = (Block4.y - (Block4.sizeY / 2))
        bottomBlock4 = (Block4.y + (Block4.sizeY / 2))
            
        if bottomMonster1 >= topBlock4 and bottomMonster1 < (Block4.y - (Block4.sizeY/4)) and rightMonster1 > leftBlock4 and leftMonster1 < rightBlock4:
            self.y = (topBlock4 - self.Size / 2)
            
        rightBlock5 = (Block5.x + (Block5.sizeX / 2))
        leftBlock5 = (Block5.x - (Block5.sizeX / 2))
        topBlock5 = (Block5.y - (Block5.sizeY / 2))
        bottomBlock5 = (Block5.y + (Block5.sizeY / 2))
            
        if rightMonster1 >= leftBlock5 and rightMonster1 < (Block5.x - (Block5.sizeX/4)) and bottomMonster1 > topBlock5 and topMonster1 < bottomBlock5:
            self.x = (leftBlock5 - self.Size / 2)
        elif leftMonster1 <= rightBlock5 and leftMonster1 > (Block5.x + (Block5.sizeX/4)) and bottomMonster1 > topBlock5 and topMonster1 < bottomBlock5:
            self.x = (rightBlock5 + self.Size / 2)
        elif bottomMonster1 >= topBlock5 and bottomMonster1 < (Block5.y - (Block5.sizeY/4)) and rightMonster1 > leftBlock5 and leftMonster1 < rightBlock5:
            self.y = (topBlock5 - self.Size / 2)
        elif topMonster1 <= bottomBlock5 and topMonster1 > (Block5.y + (Block5.sizeY/4)) and rightMonster1 > leftBlock5 and leftMonster1 < rightBlock5:
            self.y = (bottomBlock5 + self.Size / 2)  
            
        rightBlock6 = (Block6.x + (Block6.sizeX / 2))
        leftBlock6 = (Block6.x - (Block6.sizeX / 2))
        topBlock6 = (Block6.y - (Block6.sizeY / 2))
        bottomBlock6 = (Block6.y + (Block6.sizeY / 2))
            
        if rightMonster1 >= leftBlock6 and rightMonster1 < (Block6.x - (Block6.sizeX/4)) and bottomMonster1 > topBlock6 and topMonster1 < bottomBlock6:
            self.x = (leftBlock6 - self.Size / 2)
        elif leftMonster1 <= rightBlock6 and leftMonster1 > (Block6.x + (Block6.sizeX/4)) and bottomMonster1 > topBlock6 and topMonster1 < bottomBlock6:
            self.x = (rightBlock6 + self.Size / 2)
        elif bottomMonster1 >= topBlock6 and bottomMonster1 < (Block6.y - (Block6.sizeY/4)) and rightMonster1 > leftBlock6 and leftMonster1 < rightBlock6:
            self.y = (topBlock6 - self.Size / 2)
        elif topMonster1 <= bottomBlock6 and topMonster1 > (Block6.y + (Block6.sizeY/4)) and rightMonster1 > leftBlock6 and leftMonster1 < rightBlock6:
            self.y = (bottomBlock6 + self.Size / 2)  
            
        rightBlock7 = (Block7.x + (Block7.sizeX / 2))
        leftBlock7 = (Block7.x - (Block7.sizeX / 2))
        topBlock7 = (Block7.y - (Block7.sizeY / 2))
        bottomBlock7 = (Block7.y + (Block7.sizeY / 2))
            
        if rightMonster1 >= leftBlock7 and rightMonster1 < (Block7.x - (Block7.sizeX/4)) and bottomMonster1 > topBlock7 and topMonster1 < bottomBlock7:
            self.x = (leftBlock7 - self.Size / 2)
        elif leftMonster1 <= rightBlock7 and leftMonster1 > (Block7.x + (Block7.sizeX/4)) and bottomMonster1 > topBlock7 and topMonster1 < bottomBlock7:
            self.x = (rightBlock7 + self.Size / 2)
        elif bottomMonster1 >= topBlock7 and bottomMonster1 < (Block7.y - (Block7.sizeY/4)) and rightMonster1 > leftBlock7 and leftMonster1 < rightBlock7:
            self.y = (topBlock7 - self.Size / 2)
        elif topMonster1 <= bottomBlock7 and topMonster1 > (Block7.y + (Block7.sizeY/4)) and rightMonster1 > leftBlock7 and leftMonster1 < rightBlock7:
            self.y = (bottomBlock7 + self.Size / 2) 
            
        rightBlock8 = (Block8.x + (Block8.sizeX / 2))
        leftBlock8 = (Block8.x - (Block8.sizeX / 2))
        topBlock8 = (Block8.y - (Block8.sizeY / 2))
        bottomBlock8 = (Block8.y + (Block8.sizeY / 2))
            
        if rightMonster1 >= leftBlock8 and rightMonster1 < (Block8.x - (Block8.sizeX/4)) and bottomMonster1 > topBlock8 and topMonster1 < bottomBlock8:
            self.x = (leftBlock8 - self.Size / 2)
        elif leftMonster1 <= rightBlock8 and leftMonster1 > (Block8.x + (Block8.sizeX/4)) and bottomMonster1 > topBlock8 and topMonster1 < bottomBlock8:
            self.x = (rightBlock8 + self.Size / 2)
        elif bottomMonster1 >= topBlock8 and bottomMonster1 < (Block8.y - (Block8.sizeY/4)) and rightMonster1 > leftBlock8 and leftMonster1 < rightBlock8:
            self.y = (topBlock8 - self.Size / 2)
        elif topMonster1 <= bottomBlock8 and topMonster1 > (Block8.y + (Block8.sizeY/4)) and rightMonster1 > leftBlock8 and leftMonster1 < rightBlock8:
            self.y = (bottomBlock8 + self.Size / 2)  
            
class Block:
    #Initializes the block
    def __init__(self, x, y, sizeX, sizeY, col):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.col = col
        
    #Creates the block's shape
    def display(self):
        fill(self.col)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        
class Fog:
    #Initializes the block
    def __init__(self, x, y, sizeX, sizeY):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        
    #Creates the block's shape
    def display(self):
        fill(0)
        rectMode(CENTER)
        rect(Player.x - 1350, Player.y, self.sizeX, self.sizeY)
        rect(Player.x + 1350, Player.y, self.sizeX, self.sizeY)
        rect(Player.x, Player.y - 1350, self.sizeX, self.sizeY)
        rect(Player.x, Player.y + 1350, self.sizeX, self.sizeY)
            
            
            
#Creates a True value for the key pressed
def keyPressed():
    global w, a, s, d
    
    if key == "w":
        w = True
    if key == "a":
        a = True
    if key == "s":
        s = True
    if key == "d":
        d = True
            
#Causes the last key pressed to be continuous
def keyReleased():
    global w, a, s, d, up, status, lives
    
    if key == "w":
        w = False
    if key == "a":
        a = False
    if key == "s":
        s = False
    if key == "d":
        d = False
    if key == " ":
        if status == "home":
            status = "game"
        if status == "win" or status == "lose":
            lives = 3
            status = "home"
