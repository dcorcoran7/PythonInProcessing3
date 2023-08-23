#screen dimentsions: 1920 1080
#gs = gamescreen
#gs0 = starting room image (gamescreen 0)
#ggs =good game screen 
#there is no gs4


homePage = True

startButton, button1, button2, button3, button4, button5, button6 = None, None, None, None, None, None, None
bgR = 255
bgG = 255
bgB = 255

btnColorR = 50
btnColoG = 50
btnColorB = 50

gs1 = False
gs2 = False
gs3 = False
#no gs4
gs5 = False
gs6 = False
gs7 = False
gs8 = False
gs9 = False
gs10 = False
gs11 = False
gs12 = False
gs13 = False
gs14 = False
gs15 = False
gs16 = False
gs17 = False
gs18 = False
gs19 = False
gs20 = False
gs21 = False

es = False
ggs = False

deathTxt = ""
deathTxt2 = ""
deathTxt3 = ""



def setup():
    global startButton, button1, button2, button3, button4, button5, button6
    
    fullScreen()
        
    startButton = Button1(width/2, 700, 300, 100, "Start", "", 75, 40, 0)
    
    button1 = Button1(274, 880, 200, 100, "Search the", "bed", 30, 0, 40)
    button2 = Button2(548, 880, 200, 100, "Read the", "poster", 30, 0, 40)
    button3 = Button3(822, 880, 200, 100, "Investigate", "the hole", 30, 0, 40)
    button4 = Button4(1096, 880, 200, 100, "Fix the", "light", 30, 0, 40)
    button5 = Button5(1370, 880, 200, 100, "Try opening", "the window", 30, 0, 40)
    button6 = Button6(1644, 880, 200, 100, "Cry", "", 30, 0, 0)
    
def draw():
    global bgR, bgG, bgB, homePage, gs1, deathTxt, deathTxt2, deathTxt3, gs2, gs3, gs4, gs5, gs6, gs7, gs8,gs9, gs10, gs11, gs12, gs13, gs14, gs15, gs16, gs17, gs18, gs19, gs20, gs21, es, ggs

    background(bgR, bgG, bgB)

    print(gs2, gs3, gs5, gs6, gs7, gs8, gs9, gs10, gs11, gs12, gs13, gs14, gs15, gs16, gs17, gs18, gs19, gs20, gs21, es, ggs, gs1, homePage)

    if (homePage == True):
        displayHomepage()

    elif (gs1 == True):
        GameScreen1()

        
    elif (gs2 == True):#complete
        GameScreen2()

        
    elif (gs3 == True):
        GameScreen3()

        
#no gs4
        
    elif (gs5 == True):
        GameScreen5()

    elif (gs6 == True):
        GameScreen6()

        
    elif (gs7 == True):
        GameScreen7()

    
    elif (gs8 == True):
        GameScreen8()

        
    elif (gs9 == True):
        GameScreen9()

        
    elif (gs10 == True):
        GameScreen10()

        
    elif (gs11 == True):
        GameScreen11()

        
    elif (gs12 == True):
        GameScreen12()

        
    elif (gs13 == True):
        GameScreen13()
        
    elif (gs14 == True):
        GameScreen14()

        
    elif (gs15 == True):
        GameScreen15()

        
    elif (gs16 == True):
        GameScreen16()

        
    elif (gs17 == True):
        GameScreen17()

        
    elif (gs18 == True):
        GameScreen18()

        
    elif (gs19 == True):
        GameScreen19()

        
    elif (gs20 == True):
        GameScreen20()

        
    elif (gs21 == True):
        GameScreen21()

    
    
    
    elif (es == True):
        EndScreen("You won", "", "")

        
    elif (ggs == True):
        GameOverScreen(deathTxt, deathTxt2, deathTxt3)

    
def displayHomepage():
        fill(0)
        textAlign(CENTER, BOTTOM)
        textSize(100)
        text("Escape", width/2 , 400)
        
        textSize(50)
        text("Goal: Escape alive, in as few attempts as possible.", width/2, 900)
        
        fill(106, 245, 195)
        textSize(75)
        startButton.display()
        
def GameScreen1():
    global bgR, bgG, bgB, btnColorR, btnColorG, btnColorB
    if (bgR > 0):
        bgR -= 2
        bgG -= 2
        bgB -= 2
    else:
        
        gs0Img = loadImage("Starting Room Image.png")
        image(gs0Img, 0, -250)
        
        textAlign(CENTER, BOTTOM)
        fill(240, 19, 19)#red
        textSize(30)
        text("You've been abducted and have been locked in this room. You see a broken light, a boarderd up window, a cot with a pillow, ", width/2, 1000)
        text("a poster, and what seems to be a hole in the ground. What will you do?", width/2, 1050)
        
        #6 buttons  
        rectMode(CENTER)
        fill(btnColorR, btnColoG, btnColorB)
        
        button1.display()
        #rect(274, 880, 200, 100)
        
        button2.display()
        #rect(548, 880, 200, 100)
        
        button3.display()
        #rect(822, 880, 200, 100)
        
        button4.display()
        #rect(1096, 880, 200, 100)
        
        button5.display()
        #rect(1370, 880, 200, 100)
        
        button6.display()
        #rect(1644, 880, 200, 100)
        
        
        
        
def GameScreen2():
    global gs2, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Starting Room Image.png")
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You searched the bed but couldn't manage to find anything in the dark.", width/2, 1000)
    text("What do you do next?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
    
def GameScreen3():
    global gs3, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Starting Room Image.png")
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("It was hard to read the poster in the dark, but you were able to make out some numbers: 3, 6, and 12", width/2, 1000)
    text("What do you do next?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    

#no gs4
    
    
    
    
def GameScreen5():
    global gs5, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Starting Room Image Light.png")
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You got the lights to turn on!", width/2, 1000)
    text("Now what?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)



def GameScreen6():
    global gs6, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Window Room No Light Image.png")
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You went through the window and found yourself in another dark room.", width/2, 1000)
    text("You see a door on the left, what do you do?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    #button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    #button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    


def GameScreen7(): #path that leads to end, after turning on light and trying hole
    global gs7, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Ladder Room With Water and Light Image.png")
    image(gs0Img, 0, -250)#wrong image, ladder room image needed
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You climbed down the hole and jumped off the ladder into a pile of water in the room. ", width/2, 1000)
    text("You see the wall is leaking and you can't reach the ladder anymore to get out, what do you do?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen8():
    global gs8, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Starting Room Image Light.png")
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("Thanks to the lights, you were able to read the whole poster and read", width/2, 1000)
    text("'6 = 3, 12 = 6, six = three, twelve = six'. What do you do next?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    


def GameScreen9():
    global gs9, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Ladder Room With Water and Light Image.png")
    image(gs0Img, 0, -250)#same ladder room image
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You stayed calm and managed to find an exit on the ceiling. You noticed it's locked by a password.", width/2, 1000)
    text("The password machine has an '8' on the screen. Enter the password: ", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen10():
    global gs10, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Starting Room Image Light.png")
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("The light made it much easier to see allowing you to find a peice of paper with the numbers: ", width/2, 1000)
    text("9472. What do you do next?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen11():
    global gs11, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Ladder Room With Water and Light Image.png")#needed water leaking ladder room 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You yelled too loudly and gained the attention of your abductor. You hear them heading towrods you quickly.", width/2, 1000)
    text("You frantically ran to the door, but it was locked by a password. The screen says 8, enter the password: ", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    button6.display()
    #rect(1644, 880, 200, 100)
    
    
def GameScreen12():
    global gs12, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Road Image.png")
    image(gs0Img, 0, -250)#guessing the password in ladder room
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You entered the correct password (the number of letters in the number if you randomly guessed), and made it to the surface.", width/2, 1000)
    text("There's a road by your side, do you cross the road or run away? ", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    #button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    #button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    

def GameScreen13():
    global gs13, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Window Room No Light Image.png")#window room with one door on left casue in dark 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You looked around but found nothing in the dark.", width/2, 1000)
    text("What do you do next?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    #button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    #button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen14():
    global gs14, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Window Room With Light Image.png")#window image with door on left and right with light 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You managed to break your way through the window and into another room. Here you see a door on ", width/2, 1000)
    text("the left and a door on the right. What do you do?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
    
def GameScreen15():
    global gs15, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Window Room With Light Image.png")#window with lihgt with door left and right 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You looked around, but found nothing.", width/2, 1000)
    text("What do you do now?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    #button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)

    
    
    
    
def GameScreen16():
    global gs16, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Locked Door and Password Image.png")#locked door and password room, window path, no water, not ladder room 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("Right is always right, but now you've found yourself in yet another room. The door locked behind you ", width/2, 1000)
    text("and now you're starting to panic. What do you do?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    #button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    #button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
    
def GameScreen17():
    global gs17, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Locked Door and Password Image.png")#light and door password, window path, no water
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("Yelling only made things worse, your abducter is now heading your way and you're faced with a locked door.", width/2, 1000)
    text("Do you know the password?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    button6.display()
    #rect(1644, 880, 200, 100)
    
    
def GameScreen18():
    global gs18, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Road Image.png")#surface image with road in front of you, bad side of road 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You frantically entered the password in time to escape the room, but your abducter is still on your tail.", width/2, 1000)
    text("There's a road ahead of you with your abducter quickly catching up. What do you do?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    #button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen19():
    global gs19, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Locked Door and Password Image.png")#lights, door and password thing, no water
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("Staying calm and quiet, allowed you to collect your thought and focus, thus allowing you to reach the locked", width/2, 1000)
    text("door. You can get through, if you know the password. Enter the password: ", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen20():
    global gs20, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Locked Door and Password Image.png")#locked door and password, not water room 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("Incorrect password. Thankfully you were given another chance.", width/2, 1000)
    text("Enter the password: ", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    button1.display()
    #rect(274, 880, 200, 100)
    
    button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    button5.display()
    #rect(1370, 880, 200, 100)
    
    button6.display()
    #rect(1644, 880, 200, 100)
    
    
    
def GameScreen21():
    global gs21, btnColorR, btnColorG, btnColorB
    
    gs0Img = loadImage("Road Thunderstorm Image.png")#surface image thunderstorm 
    image(gs0Img, 0, -250)
    
    textAlign(CENTER, BOTTOM)
    fill(240, 19, 19)#red
    textSize(30)
    text("You entered the correct password, and escaped to the surface! However, it's currently thunderstorming there.", width/2, 1000)
    text("What do you choose to do?", width/2, 1050)
    
    #6 buttons  
    rectMode(CENTER)
    fill(btnColorR, btnColoG, btnColorB)
    
    #button1.display()
    #rect(274, 880, 200, 100)
    
    #button2.display()
    #rect(548, 880, 200, 100)
    
    button3.display()
    #rect(822, 880, 200, 100)
    
    button4.display()
    #rect(1096, 880, 200, 100)
    
    #button5.display()
    #rect(1370, 880, 200, 100)
    
    #button6.display()
    #rect(1644, 880, 200, 100)

    
    
def EndScreen(txt1, txt2, txt3):
    global es
    
    ggsImg = loadImage("Game Over Image.png")
    image(ggsImg, 0, 0)
    
    startButton.display()
    
    fill(255)
    textSize(50)
    text(txt1, width/2, 500)
    text(txt2, width/2, 600)
    text(txt3, width/2, 700)

        
def GameOverScreen(txt1, txt2, txt3):
    global ggs
    
    ggsImg = loadImage("Game Over Image.png")
    image(ggsImg, 0, 0)
    
    startButton.display()
    
    fill(255)
    textSize(50)
    text(txt1, width/2, 650)
    text(txt2, width/2, 710)
    text(txt3, width/2, 880)
        
        
def mouseClicked():
    global bgR, bgG, bgB, homePage, deathTxt, deathTxt2, deathTxt3, gs1, gs2, gs3, gs4, gs5, gs6, gs7, gs8,gs9, gs10, gs11, gs12, gs13, gs14, gs15, gs16, gs17, gs18, gs19, gs20, gs21, es, ggs
    if (homePage == True):
        if (mouseX >= 810 and mouseX <= 1110 and mouseY >= 650 and mouseY <= 750):#start
            homePage = False 
            gs1 = True
            
#--------------------------------------------------------------------------------------------------------
            
    elif (gs1 == True):#story part starts here
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - search bed
            gs1 = False
            ggs = False
            gs2 = True
        
        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - read poster
            gs1 = False
            ggs = False
            gs3 = True
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #investiagte hole 3
            gs1 = False
            ggs = True
            deathTxt = "Investigating the hole in the darkness was a bad idea."
            deathTxt2 = "You opened the lid and tried to climb down but"
            deathTxt3 = "misstepped in the darkness and fell to your death. GG"
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs1 = False
            ggs = False
            gs5 = True
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs1 = False
            ggs = False
            gs6 = True
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            gs1 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
            
            
    elif (gs2 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - search bed
            gs2 = False
            gs5 = True
            ggs = False
        
        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - read poster
            gs2 = False
            gs3 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #investiagte hole 3
            gs2 = False
            ggs = True
            deathTxt = "Investigating the hole in the darkness was a bad idea."
            deathTxt2 = "You opened the lid and tried to climb down but"
            deathTxt3 = "misstepped in the darkness and fell to your death. GG"
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs2 = False
            gs6 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs2 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            #gs2 = False
            #ggs = False
            
            
            
    elif (gs3 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1
            gs3 = False
            gs5 = True
            ggs = False
        
        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2
            gs3 = False
            gs2 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs3 = False
            ggs = True
            deathTxt = "Investigating the hole in the darkness was a bad idea."
            deathTxt2 = "You opened the lid and tried to climb down but"
            deathTxt3 = "misstepped in the darkness and fell to your death. GG"
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs3 = False
            gs6 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs3 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            #gs3 = False
            #ggs = False
            
            
            
            #NO gs4
            
            
            
            
    elif (gs5 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - 
            gs5 = False
            gs7 = True
            ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - 
            gs5 = False
            gs8 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #3
            gs5 = False
            gs14 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs5 = False
            gs10 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs5 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            #gs5 = False
            #ggs = True
            
            
    
    elif (gs6 == True):
        
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1
            gs6 = False
            gs2 = True
            ggs = False
        
        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2
            gs6 = False
            gs3 = True
            ggs = False
        
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs6 = False
            ggs = True
            deathTxt = "Aparently this door lead to an endless void. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs6 = False
            gs13 = True
            ggs = False
        
        '''
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs6 = False
            ggs = False
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs6 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
        '''
        
            
            
            
            
    elif (gs7 == True):
        #if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - 
            #gs7 = False
            #gs11 = True
            #ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - 
            gs7 = False
            ggs = False
            gs11 = True
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #3
            gs7 = False
            gs9 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs7 = False
            ggs = True
            deathTxt = "Unfortunatly, you made the hole even worse, causing the room to"
            deathTxt2 = "fill so fast that you couldn't do anything but accept your demise. GG"
            deathTxt3 = ""
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs7 = False
            gs5 = True
            ggs = False
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            #gs7 = False
            #ggs = True
            
            
            
    elif (gs8 == True):
        #if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - 
            #gs8 = False
            #gs10 = True
            #ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - 
            gs8 = False
            gs10 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #
            gs8 = False
            gs7 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs8 = False
            gs14 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs8 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            #gs8 = False
            #ggs = True
            
            
        
    elif (gs9 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - 
            gs9 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - 
            gs9 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #
            gs9 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs9 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs9 = False
            gs12 = True
            ggs = False
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            gs9 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
            
            
            
    elif (gs10 == True):
        #if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - 
            #gs10 = False
            #gs8 = True
            #ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - 
            gs10 = False
            gs8 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #
            gs10 = False
            gs14 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs10 = False
            gs7 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs10 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            #gs10 = False
            #ggs = True




    elif (gs11 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - 
            gs11 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - 
            gs11 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #
            gs11 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs11 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            gs11 = False
            gs18 = True
            ggs = False
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            gs11 = False
            ggs = True
            deathTxt = "Incorrect password."
            deathTxt2 = ""
            deathTxt3 = ""




    elif (gs12 == True):#story part starts here
        
        #if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): #button1 - search bed
            #gs12 = False
            #gs2 = True
            #ggs = False
        
        #if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): #button2 - read poster
            #gs12 = False
            #gs3 = True
            #ggs = False
        
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  #investiagte hole 3
            gs12 = False
            es = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): #light 4
            gs12 = False
            ggs = True
            deathTxt = "Unfortunatly, there was a car speeding by the moment you chose"
            deathTxt2 = "to cross the road. GG."
            deathTxt3 = ""
            
        
        #if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): #window 5 
            #gs12 = False
            #gs6 = True
            #ggs = False
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): #cry 6
            #gs12 = False
            #ggs = True
            
        
    
    elif (gs13 == True):
        '''
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs13 = False
            gs11 = True
            ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs13 = False
            ggs = True
        '''
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs13 = False
            ggs = True
            deathTxt = "Aparently this door lead to an endless void. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs13 = False
            gs1 = True
            ggs = False
        '''
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs13 = False
            gs5 = True
            ggs = False
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs13 = False
            ggs = True
        '''
        
        
    elif (gs14 == True):
        #if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            #gs14 = False
            #gs11 = True
            #ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs14 = False
            gs15 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs14 = False
            ggs = True
            deathTxt = "Aparently this door lead to an endless void. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs14 = False
            gs16 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs14 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            #gs14 = False
            #ggs = True
            
            
            
    elif (gs15 == True):
        '''
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs15 = False
            gs11 = True
            ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs15 = False
            ggs = True
        '''
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs15 = False
            ggs = True
            deathTxt = "Aparently this door lead to an endless void. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs15 = False
            gs16 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs15 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
            
        #if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            #gs15 = False
            #ggs = True
            
            
            
    elif (gs16 == True):
        '''
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs16 = False
            gs11 = True
            ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs16 = False
            ggs = True
        '''
    
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs16 = False
            gs19 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs16 = False
            gs17 = True
            ggs = False
        
        '''
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs16 = False
            ggs = True
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs16 = False
            ggs = True
        '''
        
    
    
    elif (gs17 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs17 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs17 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs17 = False
            gs18 = True
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs17 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs17 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs17 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
    
    
    elif (gs18 == True):
        #if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            #gs18 = False
            #gs11 = True
            #ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs18 = False
            ggs = True
            deathTxt = "I'm not sure what you expected the man to say, but they killed you instantly. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs18 = False
            ggs = True
            deathTxt = "Never run across a road. A car hit you, GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs18 = False
            ggs = True
            deathTxt = "You avoided death by looking for cars, however the delay"
            deathTxt2 = "allowed your abductor to catch up. They killed you, GG"
            deathTxt3 = ""
            
        '''
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs18 = False
            ggs = True
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs18 = False
            ggs = True
        '''
    
    
    elif (gs19 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs19 = False
            gs20 = True
            ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs19 = False
            gs20 = True
            ggs = False
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs19 = False
            gs21 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs19 = False
            gs20 = True
            ggs = False
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs19 = False
            gs20 = True
            ggs = False
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs19 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""

    
    elif (gs20 == True):
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs20 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs20 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs20 = False
            gs21 = True
            ggs = False
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs20 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs20 = False
            ggs = True
            deathTxt = "Incorrect password. GG"
            deathTxt2 = ""
            deathTxt3 = ""
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs20 = False
            ggs = True
            deathTxt = "You cried for many hours and eventually"
            deathTxt2 = "ended up drowning in your own tears. GG"
            deathTxt3 = ""
    
    
    elif (gs21 == True):
        '''
        if (mouseX >= 74 and mouseX <= 474 and mouseY <= 980 and mouseY >= 780): # 1 
            gs21 = False
            gs11 = True
            ggs = False

        if (mouseX >= 348 and mouseX <= 748 and mouseY <= 980 and mouseY >= 780): # 2 
            gs21 = False
            ggs = True
        '''
        
        if (mouseX >= 622 and mouseX <= 1022 and mouseY <= 980 and mouseY >= 780):  # 3
            gs21 = False
            ggs = True
            deathTxt = "You waited for the thunderstorm to pass by inside the room,"
            deathTxt2 = "unfortunatly the storm was really long, and eventually your"
            deathTxt3 = "abductor came down, saw you trying to escape, and killed you. GG"
        
        if (mouseX >= 896 and mouseX <= 1296 and mouseY <= 980 and mouseY >= 780): # 4
            gs21 = False
            ggs = True
            deathTxt = "All was going well until you were struck by lightning. GG"
            deathTxt2 = ""
            deathTxt3 = ""
        '''
        if (mouseX >= 1170 and mouseX <= 1570 and mouseY <= 980 and mouseY >= 780): # 5 
            gs21 = False
            ggs = True
            
        if (mouseX >= 1444 and mouseX <= 1844 and mouseY <= 980 and mouseY >= 780): # 6
            gs21 = False
            ggs = True
        '''
    
    elif (ggs == True):
        if (mouseX >= 810 and mouseX <= 1110 and mouseY <= 1100 and mouseY >= 900):#button1
            ggs = False
            homePage = False                      


#----------------------------------------------------------------------------------------------------------------

class Button1():
    def __init__(self, x, y, sizeX, sizeY, txt, txt2, txtSize, txtAlign, txt2Align):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.txt = txt
        self.txt2 = txt2
        self.txtSize = txtSize
        self.txtAlign = txtAlign
        self.txt2Align = txt2Align
        
    def display(self):
        global bgR, bgG, bgB, homePage, deathTxt, deathTxt2, deathTxt3, gs1, gs2, gs3, gs4, gs5, gs6, gs7, gs8,gs9, gs10, gs11, gs12, gs13, gs14, gs15, gs16, gs17, gs18, gs19, gs20, gs21, es, ggs

        if (gs2 == True):
            self.txt = "Turn on"
            self.txt2 = "the light"
        elif (gs3 == True):
            self.txt = "Turn on"
            self.txt2 = "the light" 
        elif (gs5 == True):
            self.txt = "Investigate"
            self.txt2 = "the hole"
        elif (gs6 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs7 == True):
            self.txt = "Yell for"
            self.txt2 ="help"
        elif (gs8 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs9 == True):
            self.txt = "37"
            self.txt2 = ""
        elif (gs12 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs10 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs11 == True):
            self.txt = "37"
            self.txt2 = ""
        elif (gs13 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs14 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs15 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs16 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs17 == True):
            self.txt = "4979"
            self.txt2 = ""
        elif (gs18 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs19 == True):
            self.txt = "4979"
            self.txt2 = ""
        elif (gs20 == True):
            self.txt = "4979"
            self.txt2 = ""
        elif (gs21 == True):
            self.txt = ""
            self.txt2 = ""
        elif (ggs == True):
            self.txt = "Try again"
            self.txtAlign = 25
            self.y = 920
            self.txtSize = 50
    
            gs1 = False
            gs2 = False
            gs3 = False
            gs5 = False
            gs6 = False
            gs7 = False
            gs8 = False
            gs9 = False
            gs10 = False
            gs11 = False
            gs12 = False
            gs13 = False
            gs14 = False
            gs15 = False
            gs16 = False
            gs17 = False
            gs18 = False
            gs19 = False
            gs20 = False
            gs21 = False
            es = False
            
            
            
        
        fill(50, 50, 50)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        textSize(self.txtSize)
        fill(255)
        text(self.txt, self.x, self.y + self.txtAlign)
        text(self.txt2, self.x, self.y + self.txt2Align)
        
        
        
class Button2():
    def __init__(self, x, y, sizeX, sizeY, txt, txt2, txtSize, txtAlign, txt2Align):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.txt = txt
        self.txt2 = txt2
        self.txtSize = txtSize
        self.txtAlign = txtAlign
        self.txt2Align = txt2Align
        
    def display(self):
        if (gs2 == True):
            self.txt = "Read the"
            self.txt2 = "poster"
        elif (gs3 == True):
            self.txt = "Search the"
            self.txt2 = "bed"
        elif (gs5 == True):
            self.txt = "Read the"
            self.txt2 = "poster"
        elif (gs6 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs7 == True):
            self.txt = "Yell for"
            self.txt2 ="help"
        elif (gs8 == True):
            self.txt = "Search the"
            self.txt2 = "bed"
        
        elif (gs9 == True):
            self.txt = "15"
            self.txt2 = ""
            
        
        elif (gs10 == True):
            self.txt = "Read the"
            self.txt2 = "poster"
        elif (gs11 == True):
            self.txt = "15"
            self.txt2 = ""
        elif (gs12 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs13 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs14 == True):
            self.txt = "Look"
            self.txt2 = "around"
        elif (gs15 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs16 == True):
            self.txt = ""
            self.txt2 = ""
        elif (gs17 == True):
            self.txt = "37"
            self.txt2 = ""
        elif (gs18 == True):
            self.txt = "Talk to"
            self.txt2 = "the man"
        elif (gs19 == True):
            self.txt = "37"
            self.txt2 = ""
        elif (gs20 == True):
            self.txt = "37"
            self.txt2 = ""
        elif (gs21 == True):
            self.txt = ""
            self.txt2 = ""
            
        fill(50, 50, 50)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        textSize(self.txtSize)
        fill(255)
        text(self.txt, self.x, self.y + self.txtAlign)
        text(self.txt2, self.x, self.y + self.txt2Align)
        
        
        
class Button3():
    def __init__(self, x, y, sizeX, sizeY, txt, txt2, txtSize, txtAlign, txt2Align):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.txt = txt
        self.txt2 = txt2
        self.txtSize = txtSize
        self.txtAlign = txtAlign
        self.txt2Align = txt2Align
        
    def display(self):
        if (gs2 == True):
            self.txt = "Investigate"
            self.txt2 = "the hole"
        if (gs3 == True):
            self.txt = "Investigate"
            self.txt2 = "the hole"
        if (gs5 == True):
            self.txt = "Try the"
            self.txt2 = "window"
        if (gs6 == True):
            self.txt = "Go through"
            self.txt2 = "left door"
        if (gs7 == True):
            self.txt = "Stay calm"
            self.txt2 =""
        if (gs8 == True):
            self.txt = "Investigate"
            self.txt2 = "the hole"
        if (gs9 == True):
            self.txt = "4"
            self.txt2 = ""
        
        if (gs12 == True):
            self.txt = "Run away"
            self.txt2 = ""
            
            
            
        if (gs10 == True):
            self.txt = "Try the"
            self.txt2 = "window"
        if (gs11 == True):
            self.txt = "4"
            self.txt2 = ""
        if (gs13 == True):
            self.txt = "Go through"
            self.txt2 = "left door"
        if (gs14 == True):
            self.txt = "Go left"
            self.txt2 = ""
        if (gs15 == True):
            self.txt = "Go left"
            self.txt2 = ""
        if (gs16 == True):
            self.txt = "Stay quiet"
            self.txt2 = ""
        if (gs17 == True):
            self.txt = "9472"
            self.txt2 = ""
        if (gs18 == True):
            self.txt = "Run across"
            self.txt2 = "the road"
        if (gs19 == True):
            self.txt = "9472"
            self.txt2 = ""
        if (gs20 == True):
            self.txt = "9472"
            self.txt2 = ""
        if (gs21 == True):
            self.txt = "Wait out"
            self.txt2 = "the storm"
        
        fill(50, 50, 50)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        textSize(self.txtSize)
        fill(255)
        text(self.txt, self.x, self.y + self.txtAlign)
        text(self.txt2, self.x, self.y + self.txt2Align)
        
        
        
class Button4():
    def __init__(self, x, y, sizeX, sizeY, txt, txt2, txtSize, txtAlign, txt2Align):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.txt = txt
        self.txt2 = txt2
        self.txtSize = txtSize
        self.txtAlign = txtAlign
        self.txt2Align = txt2Align
        
    def display(self):
        if (gs2 == True):
            self.txt = "Try opening"
            self.txt2 = "the window"
        if (gs3 == True):
            self.txt = "Try the"
            self.txt2 = "window"
        if (gs5 == True):
            self.txt = "Search"
            self.txt2 = "the bed"
        if (gs6 == True):
            self.txt = "Look around"
            self.txt2 = ""
        if (gs7 == True):
            self.txt = "Try to"
            self.txt2 ="seal leak"
        
        if (gs8 == True):
            self.txt = "Try the"
            self.txt2 = "window"
        if (gs9 == True):
            self.txt = "2"
            self.txt2 = ""
            
        
        if (gs12 == True):
            self.txt = "Cross the"
            self.txt2 = "road"
            
            
        
        if (gs10 == True):
            self.txt = "Investigate"
            self.txt2 = "the hole"
        if (gs11 == True):
            self.txt = "2"
            self.txt2 = ""
        if (gs13 == True):
            self.txt = "Go back"
            self.txt2 = "(Main room)"
        if (gs14 == True):
            self.txt = "Go right"
            self.txt2 = ""
        if (gs15 == True):
            self.txt = "Go right"
            self.txt2 = ""
        if (gs16 == True):
            self.txt = "Yell for"
            self.txt2 = "help"
        if (gs17 == True):
            self.txt = "5679"
            self.txt2 = ""
        if (gs18 == True):
            self.txt = "Look for cars,"
            self.txt2 = "then cross"
        if (gs19 == True):
            self.txt = "5679"
            self.txt2 = ""
        if (gs20 == True):
            self.txt = "5679"
            self.txt2 = ""
        if (gs21 == True):
            self.txt = "Make a run"
            self.txt2 = "for it"
            
        fill(50, 50, 50)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        textSize(self.txtSize)
        fill(255)
        text(self.txt, self.x, self.y + self.txtAlign)
        text(self.txt2, self.x, self.y + self.txt2Align)
        
        
        
        
class Button5():
    def __init__(self, x, y, sizeX, sizeY, txt, txt2, txtSize, txtAlign, txt2Align):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.txt = txt
        self.txt2 = txt2
        self.txtSize = txtSize
        self.txtAlign = txtAlign
        self.txt2Align = txt2Align
        
    def display(self):
        if (gs2 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs3 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs5 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs6 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs7 == True):
            self.txt = "Use water to"
            self.txt2 = "reach ladder"
        if (gs8 == True):
            self.txt = "cry"
            self.txt2 = ""
        
        if (gs9 == True):
            self.txt = "5"
            self.txt2 = ""
            
        
        
        if (gs10 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs11 == True):
            self.txt = "5"
            self.txt2 = ""
        if (gs12 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs13 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs14 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs15 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs16 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs17 == True):
            self.txt = "6437"
            self.txt2 = ""
        if (gs18 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs19 == True):
            self.txt = "6437"
            self.txt2 = ""
        if (gs20 == True):
            self.txt = "6437"
            self.txt2 = ""
        if (gs21 == True):
            self.txt = ""
            self.txt2 = ""
        
        fill(50, 50, 50)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        textSize(self.txtSize)
        fill(255)
        text(self.txt, self.x, self.y + self.txtAlign)
        text(self.txt2, self.x, self.y + self.txt2Align)
        
        
        
        
class Button6():
    def __init__(self, x, y, sizeX, sizeY, txt, txt2, txtSize, txtAlign, txt2Align):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.txt = txt
        self.txt2 = txt2
        self.txtSize = txtSize
        self.txtAlign = txtAlign
        self.txt2Align = txt2Align
        
    def display(self):
        if (gs2 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs3 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs5 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs6 == True):
            self.txt = "6"
            self.txt2 = ""
            
            
        if (gs9 == True):
            self.txt = "16"
            self.txt2 = ""
            
            
            
        if (gs10 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs11 == True):
            self.txt = "16"
            self.txt2 = ""
        if (gs13 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs14 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs15 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs16 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs17 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs18 == True):
            self.txt = ""
            self.txt2 = ""
        if (gs19 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs20 == True):
            self.txt = "cry"
            self.txt2 = ""
        if (gs21 == True):
            self.txt = ""
            self.txt2 = ""
            
        fill(50, 50, 50)
        rectMode(CENTER)
        rect(self.x, self.y, self.sizeX, self.sizeY)
        textSize(self.txtSize)
        fill(255)
        text(self.txt, self.x, self.y + self.txtAlign)
        text(self.txt2, self.x, self.y + self.txt2Align)
        
        
