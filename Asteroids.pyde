import random
import time

w, a, s, d = False, False, False, False
Spaceship = None

Asteroid1 = None
Asteroid2 = None
Asteroid3 = None
Asteroid4 = None
Asteroid5 = None
Asteroid6 = None
Asteroid7 = None
Asteroid8 = None

lives = 5
score = 0
playing = False

def setup():
    global Spaceship
    
    global Asteroid1, Asteroid2, Asteroid3, Asteroid4, Asteroid5, Asteroid6, Asteroid7, Asteroid8
    
    size (1250, 1000)

    Spaceship = Player(width / 2, height - 100 , 50)
    
    Asteroid1 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid2 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid3 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid4 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid5 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid6 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid7 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    Asteroid8 = Asteroid(random.randint(0, width), 0, random.randint(75, 150), random.randint(10, 18))
    
def draw():
    background(0)
    global lives, score
    
    if playing == False and lives == 5:
        startGame()
    
    if playing == True and lives > 0:
        scoreCounter()
        
        if score < 10:
            level1()
            fill(255)
            textAlign(CENTER, BOTTOM)
            textSize(40)
            text("Asteroids: 4", 650, 50)
        elif score > 10 and score < 20:
            level2()
            fill(255)
            text("Asteroids: 5", 650, 50)
        elif score > 20 and score < 30:
            level3()
            fill(255)
            text("Asteroids: 6", 650, 50)
        elif score > 30 and score < 40:
            level4()
            fill(255)
            text("Asteroids: 7", 650, 50)
        elif score > 40:
            level5()
            fill(255)
            text("Asteroids: 8", 650, 50)
        
        Spaceship.display()
        Spaceship.move()
        Spaceship.boundaries()
        Spaceship.update()
        
    if playing == True and lives == 0:
        gameOverPage()
        
    if playing == False and lives == 0:
        lives = 5
        score = 0
        
        Asteroid1.y = 0
        Asteroid1.x = random.randint(0, width)
        Asteroid1.vel = random.randint(10, 18)
        Asteroid1.Size = random.randint(75, 150)
        
        Asteroid2.y = 0
        Asteroid2.x = random.randint(0, width)
        Asteroid2.vel = random.randint(10, 18)
        Asteroid2.Size = random.randint(75, 150)
        
        Asteroid3.y = 0
        Asteroid3.x = random.randint(0, width)
        Asteroid3.vel = random.randint(10, 18)
        Asteroid3.Size = random.randint(75, 150)
        
        Asteroid4.y = 0
        Asteroid4.x = random.randint(0, width)
        Asteroid4.vel = random.randint(10, 18)
        Asteroid4.Size = random.randint(75, 150)
        
        Asteroid5.y = 0
        Asteroid5.x = random.randint(0, width)
        Asteroid5.vel = random.randint(10, 18)
        Asteroid5.Size = random.randint(75, 150)
        
        Asteroid6.y = 0
        Asteroid6.x = random.randint(0, width)
        Asteroid6.vel = random.randint(10, 18)
        Asteroid6.Size = random.randint(75, 150)
        
        Asteroid7.y = 0
        Asteroid7.x = random.randint(0, width)
        Asteroid7.vel = random.randint(10, 18)
        Asteroid7.Size = random.randint(75, 150)
        
        Asteroid8.y = 0
        Asteroid8.x = random.randint(0, width)
        Asteroid8.vel = random.randint(10, 18)
        Asteroid8.Size = random.randint(75, 150)
        
def startGame():
    textAlign(CENTER)
    textSize(75)
    fill(255)
    text("ASTEROIDS", (width / 2), (height / 2))
    
    textSize(50)
    text("Press 'SPACEBAR' To Start", (width / 2), (height / 2) + 100)
        
def gameOverPage():  
    global score, playing, lives
    
    playing == False
      
    Asteroid1.vel = 0
    Asteroid2.vel = 0
    Asteroid3.vel = 0
    Asteroid4.vel = 0
    Asteroid5.vel = 0
    Asteroid6.vel = 0
    Asteroid7.vel = 0
    Asteroid8.vel = 0

    textAlign(CENTER)
    textSize(50)
    fill(255)
    text("Game Over", (width / 2), (height / 2))
    text("Score: " + str(score), (width / 2), (height / 1.75))
    
    textSize(40)
    text("Press 'SPACEBAR' To Home Screen", (width / 2), (height / 1.40))
    
def scoreCounter():
    global score, lives
    score = (score + .017)
    
    fill(255)
    textAlign(CENTER, BOTTOM)
    textSize(40)
    text("Score: ", 75, 50)
    text(score, 200, 50)
    text("Lives: " + str(lives), 400, 50)
    
def level1():
    Asteroid1.display()
    Asteroid1.gravity()
    Asteroid2.display()
    Asteroid2.gravity()
    Asteroid3.display()
    Asteroid3.gravity()
    Asteroid4.display()
    Asteroid4.gravity()
    
def level2():
    Asteroid1.display()
    Asteroid1.gravity()
    Asteroid2.display()
    Asteroid2.gravity()
    Asteroid3.display()
    Asteroid3.gravity()
    Asteroid4.display()
    Asteroid4.gravity()
    Asteroid5.display()
    Asteroid5.gravity()
    
def level3():
    Asteroid1.display()
    Asteroid1.gravity()
    Asteroid2.display()
    Asteroid2.gravity()
    Asteroid3.display()
    Asteroid3.gravity()
    Asteroid4.display()
    Asteroid4.gravity()
    Asteroid5.display()
    Asteroid5.gravity()
    Asteroid6.display()
    Asteroid6.gravity()
    
def level4():
    Asteroid1.display()
    Asteroid1.gravity()
    Asteroid2.display()
    Asteroid2.gravity()
    Asteroid3.display()
    Asteroid3.gravity()
    Asteroid4.display()
    Asteroid4.gravity()
    Asteroid5.display()
    Asteroid5.gravity()
    Asteroid6.display()
    Asteroid6.gravity()
    Asteroid7.display()
    Asteroid7.gravity()
    
def level5():
    Asteroid1.display()
    Asteroid1.gravity()
    Asteroid2.display()
    Asteroid2.gravity()
    Asteroid3.display()
    Asteroid3.gravity()
    Asteroid4.display()
    Asteroid4.gravity()
    Asteroid5.display()
    Asteroid5.gravity()
    Asteroid6.display()
    Asteroid6.gravity()
    Asteroid7.display()
    Asteroid7.gravity()
    Asteroid8.display()
    Asteroid8.gravity()

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
        
        
#Creates a False value for the key released
def keyReleased():
    global w, a, s, d, playing
    if key == "w":
        w = False
    if key == "a":
        a = False
    if key == "s":
        s = False
    if key == "d":
        d = False
    if key == " ":
        if playing == False:
            playing = True
        else:
            playing = False

#Creates a Player class
class Player:
    
    #Initializes the spaceship
    def __init__(self, x, y, Size):
        self.x = x
        self.y = y
        self.Size = Size
        self.vel = 10

        
    #Creates the spaceship's shape
    def display(self):
        fill(255)
        rect(self.x, self.y, self.Size, self.Size)
        #img = loadImage("spaceship.png")
        #image(img, self.x, self.y)
    
    #Moves the spaceship in all directions
    def move(self):
        if a == True:
            self.x -= self.vel
        if d == True:
            self.x += self.vel        
        if w == True:
            self.y -= self.vel        
        if s == True:
            self.y += self.vel
            
    #Limits where the spaceship can go
    def boundaries(self):
        if self.x < 0:
            self.x = width
        if self.x > width:
            self.x = 0
        if self.y >= height - (self.Size / 2):
            self.y = height - (self.Size / 2)
        if self.y <= (self.Size / 2):
            self.y = (self.Size / 2)
            
    def update(self):
        global lives
        c = color(98, 81, 95)
        
        rightPlayer = get(self.x + self.Size / 2, self.y)
        leftPlayer = get(self.x - self.Size / 2, self.y)
        topPlayer = get(self.x, self.y - self.Size / 2)
        bottomPlayer = get(self.x, self.y + self.Size / 2)
        
        if rightPlayer == c:
            lives -= 1
            self.x = width / 2
            self.y = height - 100
        elif leftPlayer == c:
            lives -= 1
            self.x = width / 2
            self.y = height - 100
        elif topPlayer == c:
            lives -= 1
            self.x = width / 2
            self.y = height - 100
        elif bottomPlayer == c:
            lives -= 1
            self.x = width / 2
            self.y = height - 100
    

class Asteroid:
    #Initializes the Asteroid
    def __init__(self, x, y, Size, vel):
        self.x = x
        self.y = y
        self.Size = Size
        self.vel = vel
        
    #Creates the Asteroid's shape
    def display(self):
        fill("#62515F")
        noStroke()
        circle(self.x, self.y, self.Size)
        
    #Moves the asteroid down the screen
    def gravity(self):
        global randPosition, randSpeed, randSize
        self.y = self.y + self.vel
        if self.y >= height:
            self.y = 0
            self.x = random.randint(0, width)
            self.vel = random.randint(10, 18)
            self.Size = random.randint(75, 150)
