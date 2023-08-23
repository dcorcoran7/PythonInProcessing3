import random

w, a, s, d, up, down, left, right, playing, hide, auto = False, False, False, False, False, False, False, False, False, False, False
direction = 0
leftList = [0, 2, 3]
rightList = [1, 2, 3]
upList = [0, 1, 2]
downList = [0, 1, 3]

Red = "#F53457"
Blue = "#3B66D8"
Yellow = "#E3D44C"
White = "#FFFFFF"

name = "TRON"
instructions = "Press 'SPACEBAR' To Start"
playAgain = "Press 'SPACEBAR' to Play Again"

Player1 = None
Player2 = None

player1Win = False
player2Win = False

score = 1

def setup():
    global Player1, Player2
    
    size(1250, 1250)
    background(0)
    
    Player1 = Player1(50, height / 2, 25, 5, Red)
    Player2 = Player2(1200, height / 2, 25, 5, Blue)
    
def draw():
    global name, instructions, direction, leftList, rightList, upList, downList
    
    print(a)
    
    if playing == False:
        startGame()

    elif playing == True:   
        scoreCounter()
        
        if (score % 100) == 0:
            if direction == 0:
                direction = random.choice(leftList)
            if direction == 1:
                direction = random.choice(rightList)
            if direction == 2:
                direction = random.choice(upList)
            if direction == 3:
                direction = random.choice(downList)
                    
        Player1.display()
        Player1.player1Move()
        Player1.boundaries()
        Player1.updatePlayer1()
        
        Player2.display()
        if auto == False:
            Player2.player2Move()
        elif auto == True:
            Player2.computerMove()
        Player2.boundaries()
        Player2.updatePlayer2()
    
def scoreCounter():
    global score
    score = round((score + .5))
 
def startGame():
    global playing, space, instructions, White, w, a, s, d, player1Win, player2Win, hide
    
    player1Win = False
    player2Win = False
    
    playing = False
    
    textAlign(CENTER, BOTTOM)
    textSize(60)
    fill(White)
    text(name, (width / 2), (height / 2))
    textSize(30)
    text(instructions, (width / 2), (height / 2) + 60)
    
    if hide == True:
        fill(0)
        rectMode(CENTER)
        rect((width / 2), (height / 2), width, height)
        
    up = False
    down = False
    left = False
    right = False
    
    Player1.x = 50
    Player1.y = height / 2
    Player2.x = 1200
    Player2.y = height / 2
    Player1.vel = 5
    Player2.vel = 5
    
        
def endGame():
    global playing, w, a, s, d, up, down, left, right, playAgain
    
    fill(White)
    textAlign(CENTER, BOTTOM)
    textSize(60)
    text("GAME OVER", width / 2, height / 2)
    text(playAgain, (width / 2), (height / 2) + 60)

    w = False
    a = False
    s = False
    d = False
    up = False
    down = False
    left = False
    right = False
    
    if a == True:
        playing = True
    if d == True:
        playing = True        
    if w == True:
        playing = True  
    if s == True:
        playing = True
    if up == True:
        playing = True
    if left == True:
        playing = True        
    if down == True:
        playing = True  
    if right == True:
        playing = True
    
#Creates a Player class
class Player1:
    
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
        noStroke()
        rect(self.x, self.y, self.Size, self.Size)
    
    #Moves Player1 in all directions
    def player1Move(self):
        if a == True:
            self.x -= self.vel
        if d == True:
            self.x += self.vel        
        if w == True:
            self.y -= self.vel  
        if s == True:
            self.y += self.vel 
        
    #Moves Player2 in all directions
    def player2Move(self):
        if left == True:
            self.x -= self.vel
        if right == True:
            self.x += self.vel        
        if up == True:
            self.y -= self.vel  
        if down == True:
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

    #Limits where the Player can go
    def boundaries(self):
        if self.x < 0:
            self.x = width
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
            
    #Prevents from moving where Players are
    def collision(self):
        rightPlayer = (self.x + self.Size / 2)
        leftPlayer = (self.x - self.Size / 2)
        topPlayer = (self.y - self.Size / 2)
        bottomPlayer = (self.y + self.Size / 2)
        
        rightPlayer2 = (Player2.x + (Player2.Size / 2))
        leftPlayer2 = (Player2.x - (Player2.Size / 2))
        topPlayer2 = (Player2.y - (Player2.Size / 2))
        bottomPlayer2 = (Player2.y + (Player2.Size / 2))
            
        #Player2
        if rightPlayer >= leftPlayer2 and rightPlayer < (Player2.x - (Player2.Size/4)) and bottomPlayer > topPlayer2 and topPlayer < bottomPlayer2:
            self.x = (leftPlayer2 - self.Size / 2)
        elif leftPlayer <= rightPlayer2 and leftPlayer > (Player2.x + (Player2.Size/4)) and bottomPlayer > topPlayer2 and topPlayer < bottomPlayer2:
            self.x = (rightPlayer2 + self.Size / 2)
        elif bottomPlayer >= topPlayer2 and bottomPlayer < (Player2.y - (Player2.Size/4)) and rightPlayer > leftPlayer2 and leftPlayer < rightPlayer2:
            self.y = (topPlayer2 - self.Size / 2)
        elif topPlayer <= bottomPlayer2 and topPlayer > (Player2.y + (Player2.Size/4)) and rightPlayer > leftPlayer2 and leftPlayer < rightPlayer2:
            self.y = (bottomPlayer2 + self.Size / 2)
    
    def updatePlayer1(self):
        c = color(59, 102, 216)
        
        rightPlayer = get(self.x + self.Size / 2, self.y)
        leftPlayer = get(self.x - self.Size / 2, self.y)
        topPlayer = get(self.x, self.y - self.Size / 2)
        bottomPlayer = get(self.x, self.y + self.Size / 2)
        
        if rightPlayer == c:
            self.vel = 0
            Player2.vel = 0
            player2Win = True
            endGame()
        elif leftPlayer == c:
            self.vel = 0
            Player2.vel = 0
            player2Win = True
            endGame()
        elif topPlayer == c:
            self.vel = 0
            Player2.vel = 0
            player2Win = True
            endGame()
        elif bottomPlayer == c:
            self.vel = 0
            Player2.vel = 0
            player2Win = True
            endGame()
            
#Creates a Player class
class Player2:
    
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
        noStroke()
        rect(self.x, self.y, self.Size, self.Size)
        
    #Moves Player2 in all directions
    def player2Move(self):
        if left == True:
            self.x -= self.vel
        if right == True:
            self.x += self.vel        
        if up == True:
            self.y -= self.vel  
        if down == True:
            self.y += self.vel  
            
    def computerMove(self):
        scoreCounter()
        # 0 = left 
        #1 = right 
        #2 = up
        #3 = down   
        if playing == True:         
            if direction == 0:
                self.x -= 5
            elif direction == 1:
                self.x += 5
            elif direction == 2:
                self.y -= 5
            elif direction == 3:
                self.y += 5

    #Limits where the Player can go
    def boundaries(self):
        if self.x < 0:
            self.x = width
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
            
    #Prevents from moving where Players are
    def collision(self):
        rightPlayer = (self.x + self.Size / 2)
        leftPlayer = (self.x - self.Size / 2)
        topPlayer = (self.y - self.Size / 2)
        bottomPlayer = (self.y + self.Size / 2)
        
        rightPlayer2 = (Player2.x + (Player2.Size / 2))
        leftPlayer2 = (Player2.x - (Player2.Size / 2))
        topPlayer2 = (Player2.y - (Player2.Size / 2))
        bottomPlayer2 = (Player2.y + (Player2.Size / 2))
            
        #Player2
        if rightPlayer >= leftPlayer2 and rightPlayer < (Player2.x - (Player2.Size/4)) and bottomPlayer > topPlayer2 and topPlayer < bottomPlayer2:
            self.x = (leftPlayer2 - self.Size / 2)
        elif leftPlayer <= rightPlayer2 and leftPlayer > (Player2.x + (Player2.Size/4)) and bottomPlayer > topPlayer2 and topPlayer < bottomPlayer2:
            self.x = (rightPlayer2 + self.Size / 2)
        elif bottomPlayer >= topPlayer2 and bottomPlayer < (Player2.y - (Player2.Size/4)) and rightPlayer > leftPlayer2 and leftPlayer < rightPlayer2:
            self.y = (topPlayer2 - self.Size / 2)
        elif topPlayer <= bottomPlayer2 and topPlayer > (Player2.y + (Player2.Size/4)) and rightPlayer > leftPlayer2 and leftPlayer < rightPlayer2:
            self.y = (bottomPlayer2 + self.Size / 2)
    
    def updatePlayer2(self):
        c = color(245, 52, 87)
        
        rightPlayer = get(self.x + self.Size / 2, self.y)
        leftPlayer = get(self.x - self.Size / 2, self.y)
        topPlayer = get(self.x, self.y - self.Size / 2)
        bottomPlayer = get(self.x, self.y + self.Size / 2)
        
        if rightPlayer == c:
            self.vel = 0
            Player2.vel = 0
            endGame()
        elif leftPlayer == c:
            self.vel = 0
            Player2.vel = 0
            endGame()
        elif topPlayer == c:
            self.vel = 0
            Player2.vel = 0
            endGame()
        elif bottomPlayer == c:
            self.vel = 0
            Player2.vel = 0
            endGame()
        
            
#Creates a True value for the key pressed
def keyPressed():
    global w, a, s, d, up, left, down, right, hide
    
    if key == "w":
        if s == True:
            playing = True
            w = False
        else:
            w = True
            a = False
            s = False
            d = False
            playing = True
    if key == "a":
        if d == True:
            playing = True
            a == False
        else:
            a = True
            w = False
            s = False
            d = False
            playing = True
    if key == "s":
        if w == True:
            playing = True
            s = False
        else:
            s = True
            w = False
            a = False
            d = False
            playing = True
    if key == "d":
        if a == True:
            playing = True
            d = False
        else:
            d = True
            w = False
            a = False
            s = False
            playing = True

    if keyCode == UP:
        if down == True:
            playing = True
            up = False
        else:
            up = True
            left = False
            down = False
            right = False
            playing = True
    if keyCode == LEFT:
        if right == True:
            playing = True
            left = False
        else:
            up = False
            left = True
            down = False
            right = False
            playing = True
    if keyCode == DOWN:
        if up == True:
            playing = True
            down = False
        else:
            up = False
            left = False
            down = True
            right = False
            playing = True
    if keyCode == RIGHT:
        if left == True:
            playing = True
            right = False
        else:
            up = False
            left = False
            down = False
            right = True
            playing = True
        
    if key == " ":
        hide = True
            
#Causes the last key pressed to be continuous
def keyReleased():
    global w, a, s, d, up, left, down, right, playing, hide, auto
    
    if key == "w":
        if s == True:
            playing = True
            w = False
        else:
            w = True
            a = False
            s = False
            d = False
            playing = True
    if key == "a":
        if d == True:
            playing = True
            a = False
        else:
            a = True
            w = False
            s = False
            d = False
            playing = True
    if key == "s":
        if w == True:
            playing = True
            s = False
        else:
            s = True
            w = False
            a = False
            d = False
            playing = True
    if key == "d":
        if a == True:
            playing = True
            d = False
        else:
            d = True
            w = False
            a = False
            s = False
            playing = True

    if keyCode == UP:
        if down == True:
            playing = True
            up = False
        else:
            up = True
            left = False
            down = False
            right = False
            playing = True
    if keyCode == LEFT:
        if right == True:
            playing = True
            left = False
        else:
            up = False
            left = True
            down = False
            right = False
            playing = True
    if keyCode == DOWN:
        if up == True:
            playing = True
            down = False
        else:
            up = False
            left = False
            down = True
            right = False
            playing = True
    if keyCode == RIGHT:
        if left == True:
            playing = True
            right = False
        else:
            up = False
            left = False
            down = False
            right = True
            playing = True
        
    if key == " ":
        if playing == False:
            playing = True
        else:
            playing = False
            startGame()
        hide = True
        
    if key == "p":
        if auto == False:
            auto = True
        else:
            auto = False
