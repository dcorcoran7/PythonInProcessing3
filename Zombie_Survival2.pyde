playing = True
space = False
jumpCount=0
zombie1, zombie2, zombie3, zombie4, zombie5, zombie6, zombie7, zombie8, zombie9, zombie10 = None, None, None, None, None, None, None, None, None, None 
militaryMan=None
w, a, s, d, f=False, False, False, False, False 
facingLeft, facingRight = False, False
firingRight, firingLeft = False, False
Block1, Block2, Block3= None, None, None 
rocket=None 
score, timer = 0, 0
rand1, rand2, rand3, rand4, rand5, rand6, rand7, rand8, rand9, rand10 = random (1485, 1900), random (20, 445), random (1485, 1900), random (20, 445), random (1485, 1900), random (20, 445), random (1485, 1900), random (20, 445), random (1485, 1900), random (20, 445)
def setup ():
    global militaryMan, Block1, Block2, Block3, zombie1, zombie2, zombie3, zombie4, zombie5, zombie6, zombie7, zombie8, zombie9, zombie10, rocket 
    size (1920, 1080)
    militaryMan=Player(width/2, 100, 107, 121, 5)
    Block1=block(width/2, 750, 1000, 30)
    Block2=block(1750, 200, 700, 30)
    Block3=block(170, 200, 700, 30)
    zombie1 = zombie (random (1485, 1900), 100, 126, 119, 3, "right", True)
    zombie2 = zombie (random (20, 445), 100, 126, 126, 3, "left", True)
    zombie3 = zombie (random (1485, 1900), 100, 126, 119, 3, "right", True)
    zombie4 = zombie (random (20, 445), 100, 126, 126, 3, "left", True)
    zombie5 = zombie (random (1485, 1900), 100, 126, 119, 3, "right", True)
    zombie6 = zombie (random (20, 445), 100, 126, 126, 3, "left", True)
    zombie7 = zombie (random (1485, 1900), 100, 126, 119, 3, "right", True)
    zombie8 = zombie (random (20, 445), 100, 126, 126, 3, "left", True)
    zombie9 = zombie (random (1485, 1900), 100, 126, 119, 3, "right", True)
    zombie10 = zombie (random (20, 445), 100, 126, 126, 3, "left", True)
    rocket = shoot (militaryMan.x, militaryMan.y, 28, 10, 16, "right")
def draw ():
    global score, playing
    background (160, 21, 21)
    fill (0)
    showScore ()
    militaryMan.display ()
    militaryMan.move ()
    militaryMan.collision ()
    militaryMan.Border()
    Block1.display ()
    Block2.display ()
    Block3.display ()

    if score < 20:
        level1 ()
    if score >= 20 and score < 100:
        level2 ()
    if score >= 40 and score < 100:
        level3 ()
    if score >= 60 and score < 100:
        level4 ()
    if score >=80:
        level5 ()
    rocket.move ()
    if playing == False:
        gameOver()
def level1 ():
    Block1.display ()
    Block2.display ()
    Block3.display ()
    zombie1.display ()
    zombie1.move ()
    zombie1.collision ()
    zombie1.Border ()
    zombie2.display ()
    zombie2.move ()
    zombie2.collision ()
    zombie2.Border ()
def level2():
    zombie1.display ()
    zombie1.move ()
    zombie1.collision ()
    zombie1.Border ()
    zombie2.display ()
    zombie2.move ()
    zombie2.collision ()
    zombie2.Border ()
    zombie3.display ()
    zombie3.move ()
    zombie3.collision ()
    zombie3.Border ()
    zombie4.display ()
    zombie4.move ()
    zombie4.collision ()
    zombie4.Border ()
def level3 ():
    zombie1.display ()
    zombie1.move ()
    zombie1.collision ()
    zombie1.Border ()
    zombie2.display ()
    zombie2.move ()
    zombie2.collision ()
    zombie2.Border ()
    zombie3.display ()
    zombie3.move ()
    zombie3.collision ()
    zombie3.Border ()
    zombie4.display ()
    zombie4.move ()
    zombie4.collision ()
    zombie4.Border ()
    zombie5.display ()
    zombie5.move ()
    zombie5.collision ()
    zombie5.Border ()
    zombie6.display ()
    zombie6.move ()
    zombie6.collision ()
    zombie6.Border ()
    
def level4 ():
    zombie1.display ()
    zombie1.move ()
    zombie1.collision ()
    zombie1.Border ()
    zombie2.display ()
    zombie2.move ()
    zombie2.collision ()
    zombie2.Border ()
    zombie3.display ()
    zombie3.move ()
    zombie3.collision ()
    zombie3.Border ()
    zombie4.display ()
    zombie4.move ()
    zombie4.collision ()
    zombie4.Border ()
    zombie5.display ()
    zombie5.move ()
    zombie5.collision ()
    zombie5.Border ()
    zombie6.display ()
    zombie6.move ()
    zombie6.collision ()
    zombie6.Border ()
    zombie7.display ()
    zombie7.move ()
    zombie7.collision ()
    zombie7.Border ()
    zombie8.display ()
    zombie8.move ()
    zombie8.collision ()
    zombie8.Border ()
def level5 ():
    zombie1.display ()
    zombie1.move ()
    zombie1.collision ()
    zombie1.Border ()
    zombie2.display ()
    zombie2.move ()
    zombie2.collision ()
    zombie2.Border ()
    zombie3.display ()
    zombie3.move ()
    zombie3.collision ()
    zombie3.Border ()
    zombie4.display ()
    zombie4.move ()
    zombie4.collision ()
    zombie4.Border ()
    zombie5.display ()
    zombie5.move ()
    zombie5.collision ()
    zombie5.Border ()
    zombie6.display ()
    zombie6.move ()
    zombie6.collision ()
    zombie6.Border ()
    zombie7.display ()
    zombie7.move ()
    zombie7.collision ()
    zombie7.Border ()
    zombie8.display ()
    zombie8.move ()
    zombie8.collision ()
    zombie8.Border ()
    zombie9.display ()
    zombie9.move ()
    zombie9.collision ()
    zombie9.Border ()
    zombie10.display ()
    zombie10.move ()
    zombie10.collision ()
    zombie10.Border ()
def gameOver():
    global space, score
    fill (0)
    textSize(100)
    textAlign(CENTER, BOTTOM)
    text("GAME OVER", width / 2, height / 2)
    zombie1.x = rand1
    zombie2.x = rand2
    zombie3.x = rand3
    zombie4.x = rand4
    zombie5.x = rand5
    zombie6.x = rand6
    zombie7.x = rand7
    zombie8.x = rand8
    zombie9.x = rand9
    zombie10.x = rand10
    zombie1.y = 100
    zombie2.y = 100
    zombie3.y = 100
    zombie4.y = 100
    zombie5.y = 100
    zombie6.y = 100
    zombie7.y = 100
    zombie8.y = 100
    zombie9.y = 100
    zombie10.y = 100
    if space == True:
        militaryMan.x = width /2 
        militaryMan.y = 150
        score=0
def showScore():
    global score, timer
    timer+=.02
    textSize (50)
    fill (0)
    textAlign (CENTER, BOTTOM)
    text("Score: "+str(score), width/8, 60)
class Player ():
    def __init__ (self, x, y, SizeX, SizeY, vel):
        self.x=x
        self.y=y
        self.SizeX=SizeX
        self.SizeY=SizeY
        self.vel = vel
    def display (self):
        global a, s, w, d, firingLeft, firingRight
        noStroke ()
        imageMode (CENTER)
        if playing == True:
            if facingLeft == True and firingLeft == False:
                img=loadImage("military man left.png")
                image(img, self.x, self.y)
                if w == True:
                    img=loadImage ("military man left.png")
                    image(img, self.x, self.y)
                if s == True:
                    img=loadImage ("military man left.png")
                    image(img, self.x, self.y)
                d = False
            if facingRight == True and firingRight == False:
                img=loadImage("military man.png")
                image(img, self.x, self.y)
                if w == True:
                    img=loadImage ("military man.png")
                    image(img, self.x, self.y)
                if s == True:
                    img=loadImage ("military man.png")
                    image(img, self.x, self.y)
                a = False
            if facingLeft == False and facingRight == False:
                img=loadImage ("military man.png")
                image(img, self.x, self.y)
            if facingLeft == True and firingLeft == True:
                img=loadImage("military man left fire.png")
                image(img, self.x, self.y)
            if facingRight == True and firingRight == True:
                img=loadImage("military man fire.png")
                image(img, self.x, self.y)
        if playing == False:
            img=loadImage("military man die.png")
            image(img, self.x, self.y)
    def move(self):
        global jumpCount
        if playing == True:
            if w == True and jumpCount < 35:
                self.y -= self.vel
                jumpCount+=1
            if w == False or jumpCount==35:
                self.y+=self.vel
            if a == True:
                self.x -= self.vel
            if d == True:
                self.x += self.vel
    def Border (self):
        global playing
        if self.y > height:
            playing = False
        if self.x < 0:
            self.x = 0
        if self.x > width:
            self.x = width  
        if self.y < 0:
            self.y = 0 
    def collision (self):
        global jumpCount
        rightPlayer=(self.x+self.SizeX/2)
        leftPlayer=(self.x-self.SizeX/2)
        topPlayer=(self.y-self.SizeY/2)
        bottomPlayer=(self.y+self.SizeY/2)
        rightBlock1=(Block1.x+Block1.SizeX/2)
        leftBlock1=(Block1.x-Block1.SizeX/2)
        topBlock1=(Block1.y-Block1.SizeY/2)
        bottomBlock1=(Block1.y+Block1.SizeY/2)
        if rightPlayer>=leftBlock1 and rightPlayer < (Block1.x - (Block1.SizeX/2.5)) and bottomPlayer > topBlock1 and topPlayer < bottomBlock1:
            self.x = (leftBlock1 - self.SizeX/2)
        elif leftPlayer <= rightBlock1 and leftPlayer > (Block1.x + (Block1.SizeX/2.5)) and bottomPlayer > topBlock1 and topPlayer < bottomBlock1:
            self.x = (rightBlock1 + self.SizeX/2)
        elif bottomPlayer >= topBlock1 and bottomPlayer < (Block1.y - (Block1.SizeY/4)) and rightPlayer > leftBlock1 and leftPlayer < rightBlock1:
            self.y = (topBlock1 - self.SizeY/2)
            jumpCount=0
        elif topPlayer <= bottomBlock1 and topPlayer > (Block1.y + (Block1.SizeY/4)) and rightPlayer > leftBlock1 and leftPlayer < rightBlock1:
            self.y = (bottomBlock1 + self.SizeY/2)
        rightBlock2=(Block2.x+Block2.SizeX/2)
        leftBlock2=(Block2.x-Block2.SizeX/2)
        topBlock2=(Block2.y-Block2.SizeY/2)
        bottomBlock2=(Block2.y+Block2.SizeY/2)
        if rightPlayer>=leftBlock2 and rightPlayer < (Block2.x - (Block2.SizeX/2.5)) and bottomPlayer > topBlock2 and topPlayer < bottomBlock2:
            self.x = (leftBlock2 - self.SizeX/2)
        elif leftPlayer <= rightBlock2 and leftPlayer > (Block2.x + (Block2.SizeX/2.5)) and bottomPlayer > topBlock2 and topPlayer < bottomBlock2:
            self.x = (rightBlock2 + self.SizeX/2)
        elif bottomPlayer >= topBlock2 and bottomPlayer < (Block2.y - (Block2.SizeY/4)) and rightPlayer > leftBlock2 and leftPlayer < rightBlock2:
            self.y = (topBlock2 - self.SizeY/2)
            jumpCount=0
        elif topPlayer <= bottomBlock2 and topPlayer > (Block2.y + (Block2.SizeY/4)) and rightPlayer > leftBlock2 and leftPlayer < rightBlock2:
            self.y = (bottomBlock2 + self.SizeY/2)
        rightBlock3=(Block3.x+Block3.SizeX/2)
        leftBlock3=(Block3.x-Block3.SizeX/2)
        topBlock3=(Block3.y-Block3.SizeY/2)
        bottomBlock3=(Block3.y+Block3.SizeY/2)
        if rightPlayer>=leftBlock3 and rightPlayer < (Block3.x - (Block3.SizeX/2.5)) and bottomPlayer > topBlock3 and topPlayer < bottomBlock3:
            self.x = (leftBlock3 - self.SizeX/2)
        elif leftPlayer <= rightBlock3 and leftPlayer > (Block3.x + (Block3.SizeX/2.5)) and bottomPlayer > topBlock3 and topPlayer < bottomBlock3:
            self.x = (rightBlock3 + self.SizeX/2)
        elif bottomPlayer >= topBlock3 and bottomPlayer < (Block3.y - (Block3.SizeY/4)) and rightPlayer > leftBlock3 and leftPlayer < rightBlock3:
            self.y = (topBlock3 - self.SizeY/2)
            jumpCount=0
        elif topPlayer <= bottomBlock3 and topPlayer > (Block3.y + (Block3.SizeY/4)) and rightPlayer > leftBlock3 and leftPlayer < rightBlock3:
            self.y = (bottomBlock3 + self.SizeY/2)
    def die (self):
        if playing==False:
            imageMode (CENTER)
            img=loadImage ("military man die.png")
            img (img, self.x, self.y)
class block ():
    def __init__ (self, x, y, SizeX, SizeY):
        self.x=x
        self.y=y
        self.SizeX=SizeX
        self.SizeY=SizeY
    def display (self):
        fill (0)
        rect (self.x, self.y, self.SizeX, self.SizeY)
        rectMode (CENTER)
        noStroke ()
class zombie ():
    def __init__ (self, x, y, SizeX, SizeY, vel, pos, falling):
        self.x=x
        self.y=y
        self.SizeX=SizeX
        self.SizeY=SizeY
        self.vel=vel
        self.pos=pos
        self.falling=falling
    def display (self):
        if self.pos=="left":
            imageMode (CENTER)
            img = loadImage ("zombie right.png")
            image (img, self.x, self.y)
        else:
            imageMode (CENTER)
            img = loadImage ("zombie.png")
            image (img, self.x, self.y)
    def move(self):
        if self.falling==True:
            self.y+=self.vel
        if self.falling==False:
            if self.pos=="right":
                self.x-=self.vel
            if self.pos=="left":
                self.x+=self.vel
    def Border (self):
        if self.pos=="right":
            if self.y > height:
                self.y=100
                self.x=random (1485, 1900)
        if self.pos=="left":
            if self.y > height:
                self.y=100
                self.x=random (20, 445)
    def collision (self):
        global playing, f, score 
        rightZombie=(self.x+self.SizeX/2)
        leftZombie=(self.x-self.SizeX/2)
        topZombie=(self.y-self.SizeY/2)
        bottomZombie=(self.y+self.SizeY/2)
        rightBlock1=(Block1.x+Block1.SizeX/2)
        leftBlock1=(Block1.x-Block1.SizeX/2)
        topBlock1=(Block1.y-Block1.SizeY/2)
        bottomBlock1=(Block1.y+Block1.SizeY/2)
        rightBlock2=(Block2.x+Block2.SizeX/2)
        leftBlock2=(Block2.x-Block2.SizeX/2)
        topBlock2=(Block2.y-Block2.SizeY/2)
        bottomBlock2=(Block2.y+Block2.SizeY/2)
        rightBlock3=(Block3.x+Block3.SizeX/2)
        leftBlock3=(Block3.x-Block3.SizeX/2)
        topBlock3=(Block3.y-Block3.SizeY/2)
        bottomBlock3=(Block3.y+Block3.SizeY/2)
        rightPlayer=(militaryMan.x+militaryMan.SizeX/2)
        leftPlayer=(militaryMan.x-militaryMan.SizeX/2)
        topPlayer=(militaryMan.y-militaryMan.SizeY/2)
        bottomPlayer=(militaryMan.y+militaryMan.SizeY/2)
        rightrocket=(rocket.x+rocket.SizeX/2)
        leftrocket=(rocket.x-rocket.SizeX/2)
        toprocket=(rocket.y-rocket.SizeY/2)
        bottomrocket=(rocket.y+rocket.SizeY/2)
        if rightZombie>=leftBlock1 and rightZombie < (Block1.x - (Block1.SizeX/2.5)) and bottomZombie > topBlock1 and topZombie < bottomBlock1:
            self.x = (leftBlock1 - self.SizeX/2)
            self.falling=False
        elif leftZombie <= rightBlock1 and leftZombie > (Block1.x + (Block1.SizeX/2.5)) and bottomZombie > topBlock1 and topZombie < bottomBlock1:
            self.x = (rightBlock1 + self.SizeX/2)
            self.falling=False
        if bottomZombie >= topBlock1 and bottomZombie < (Block1.y - (Block1.SizeY/4)) and rightZombie > leftBlock1 and leftZombie < rightBlock1:
            self.y = (topBlock1 - self.SizeY/2)
            self.falling=False
        elif topZombie <= bottomBlock1 and topZombie > (Block1.y + (Block1.SizeY/4)) and rightZombie > leftBlock1 and leftZombie < rightBlock1:
            self.y = (bottomBlock1 + self.SizeY/2)
            self.falling=False
        elif rightZombie>=leftBlock2 and rightZombie < (Block2.x - (Block2.SizeX/2.5)) and bottomZombie > topBlock2 and topZombie < bottomBlock2:
            self.x = (leftBlock2 - self.SizeX/2)
            self.falling=False
        elif leftZombie <= rightBlock2 and leftZombie > (Block2.x + (Block2.SizeX/2.5)) and bottomZombie > topBlock2 and topZombie < bottomBlock2:
            self.x = (rightBlock2 + self.SizeX/2)
            self.falling=False
        elif bottomZombie >= topBlock2 and bottomZombie < (Block2.y - (Block2.SizeY/4)) and rightZombie > leftBlock2 and leftZombie < rightBlock2:
            self.y = (topBlock2 - self.SizeY/2)
            self.falling=False
        elif topZombie <= bottomBlock2 and topZombie > (Block2.y + (Block2.SizeY/4)) and rightZombie > leftBlock2 and leftZombie < rightBlock2:
            self.y = (bottomBlock2 + self.SizeY/2)
            self.falling=False
        elif rightZombie>=leftBlock3 and rightZombie < (Block3.x - (Block3.SizeX/2.5)) and bottomZombie > topBlock3 and topZombie < bottomBlock3:
            self.x = (leftBlock3 - self.SizeX/2)
            self.falling=False
        elif leftZombie <= rightBlock3 and leftZombie > (Block3.x + (Block3.SizeX/2.5)) and bottomZombie > topBlock3 and topZombie < bottomBlock3:
            self.x = (rightBlock3 + self.SizeX/2)
            self.falling=False
        elif bottomZombie >= topBlock3 and bottomZombie < (Block3.y - (Block3.SizeY/4)) and rightZombie > leftBlock3 and leftZombie < rightBlock3:
            self.y = (topBlock3 - self.SizeY/2)
            self.falling=False
        elif topZombie <= bottomBlock3 and topZombie > (Block3.y + (Block3.SizeY/4)) and rightZombie > leftBlock3 and leftZombie < rightBlock3:
            self.y = (bottomBlock3 + self.SizeY/2)
            self.falling=False
        else:
            self.falling = True
        if rightZombie>=leftPlayer and rightZombie < (militaryMan.x - (militaryMan.SizeX/2.5)) and bottomZombie > topPlayer and topZombie < bottomPlayer:
            playing = False
        elif leftZombie <= rightPlayer and leftZombie > (militaryMan.x + (militaryMan.SizeX/2.5)) and bottomZombie > topPlayer and topZombie < bottomPlayer:
            playing = False
        elif bottomZombie >= topPlayer and bottomZombie < (militaryMan.y - (militaryMan.SizeY/4)) and rightZombie > leftPlayer and leftZombie < rightPlayer:
            playing = False
        elif topZombie <= bottomPlayer and topZombie > (militaryMan.y + (militaryMan.SizeY/4)) and rightZombie > leftPlayer and leftZombie < rightPlayer:
            playing = False
            
        if rightZombie>=leftrocket and rightZombie < (rocket.x - (rocket.SizeX/20)) and bottomZombie > toprocket and topZombie < bottomrocket:
            if self.pos == "right":
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (1485, 1900)
                self.y = 100
                f = False
                score+=1
            else:
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (20, 445)
                self.y = 100
                f = False
                score+=1
        elif leftZombie <= rightrocket and leftZombie > (rocket.x + (rocket.SizeX/10)) and bottomZombie > toprocket and topZombie < bottomrocket:
            if self.pos == "right":
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (1485, 1900)
                self.y = 100
                f = False
                score+=1
            else:
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (20, 445)
                self.y = 100
                f = False
                score+=1
        elif bottomZombie >= toprocket and bottomZombie < (rocket.y - (rocket.SizeY/10)) and rightZombie > leftrocket and leftZombie < rightrocket:
            if self.pos == "right":
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (1485, 1900)
                self.y = 100
                f = False
                score+=1
            else:
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (20, 445)
                self.y = 100
                f = False
                score+=1
        elif topZombie <= bottomrocket and topZombie > (rocket.y + (rocket.SizeY/10)) and rightZombie > leftrocket and leftZombie < rightrocket:
            if self.pos == "right":
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (1485, 1900)
                self.y = 100
                f = False
                score+=1
            else:
                img=loadImage("zombie die.png")
                image(img, self.x, self.y)
                self.x = random (20, 445)
                self.y = 100
                f = False
                score+=1
class shoot ():
    def __init__ (self, x, y, SizeX, SizeY, vel, pos, ):
        self.x=x
        self.y=y
        self.SizeX=SizeX
        self.SizeY=SizeY
        self.vel=vel
        self.pos=pos
    def move (self):
        global f, facingLeft, facingRight
        if playing == True:
            if facingLeft == False and facingRight == False:
                self.pos = "right"
            elif facingLeft == True:
                self.pos = "left"
            elif facingRight == True:
                self.pos = "right"
            if self.x > width or self.x < 0:
                img=loadImage("explosion.png")
                image(img, self.x, self.y)
                f = False
            if self.pos == "right" and f == False:
                imageMode (CENTER)
                img = loadImage ("rocket.png")
                image (img, militaryMan.x + 39, militaryMan.y - 40)
                self.x = militaryMan.x + 39
                self.y = militaryMan.y - 40
            elif self.pos == "left" and f == False:
                imageMode (CENTER)
                img = loadImage ("rocket left.png")
                image (img, militaryMan.x - 39, militaryMan.y - 40)
                self.x = militaryMan.x - 39
                self.y = militaryMan.y - 40
            elif self.pos == "right" and f == True:
                imageMode (CENTER)
                img = loadImage ("rocket.png")
                image (img, self.x, self.y)
                self.x += self.vel
            elif self.pos == "left" and f == True:
                imageMode (CENTER)
                img = loadImage ("rocket left.png")
                image (img, self.x, self.y)
                self.x -= self.vel
def keyPressed ():
    global w, a, s, d, f, facingLeft, facingRight, firingLeft, firingRight, space
    if key=="w":
        w=True
    if key=="a":
        if f == False:
            a=True
            facingLeft = True
            facingRight = False
    if key=="s":
        s=True
    if key=="d":
        if f == False:
            d=True
            facingRight = True
            facingLeft = False
    if key=="f":
        f=True
        if facingRight == True:
            firingRight = True
        elif facingLeft == True:
            firingLeft = True
    if key == " ":
        space = True
def keyReleased ():
    global w, a, s, d, playing, facingLeft, facingRight, firingLeft, firingRight, space
    if key=="w":
        w=False
    if key=="a":
        if f == False:
            a=False
            facingLeft = True
            facingRight = False
    if key=="s":
        s=False
    if key=="d":
        if f == False:
            d=False
            facingRight = True
            facingLeft = False
    if key==" ":
        space = False
        if playing == False:
            playing = True
        else:
            playing = False
    if key == "f":
        firingRight = False
        firingLeft = False
