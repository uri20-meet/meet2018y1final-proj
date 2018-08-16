
#Music import
from pygame import mixer # Load the required library

#imports
import turtle
import time


#Music setup

mixer.init()
mixer.music.load('bgMusic.mp3')
mixer.music.play()


#setup

level=0
SIZE_X=1910
SIZE_Y=1070
turtle.setup(SIZE_X, SIZE_Y)
turtle.delay()


#register images

turtle.register_shape("questBorder.gif")
turtle.register_shape("waterCan.gif")
turtle.register_shape("gameoverv1.gif")
turtle.register_shape("plantx.gif")
turtle.register_shape("tree.gif")
turtle.register_shape("questBorder.gif")
turtle.register_shape("waterCan2.gif")
turtle.register_shape("deadPlant.gif")
turtle.register_shape("bg.gif")


#bg and text turtle

turtle.bgpic("bg.gif")
turtle.hideturtle()
a=turtle.clone()
a.hideturtle()


#title

titleTurtle = turtle.clone()
titleTurtle.hideturtle()
titleTurtle.penup()
titleTurtle.goto(0,350)
titleTurtle.color('black')
titleTurtle.write("Answer And Win!", move=True, align="center", font=('Comic Sans MS', 100, 'bold'))
titleTurtle.hideturtle()


#PLANTS CREATING AND POSITIONING

plant1 = turtle.clone()
plant1.shape("plantx.gif")
plant1.penup()
plant1.goto(100,70)
plant1.showturtle()


plant2 = turtle.clone()
plant2.shape("plantx.gif")
plant2.penup()
plant2.goto(450,20)
plant2.showturtle()

plant3 = turtle.clone()
plant3.shape("plantx.gif")
plant3.penup()
plant3.goto(550,-150)
plant3.showturtle()

plant4 = turtle.clone()
plant4.shape("plantx.gif")
plant4.penup()
plant4.goto(450,-320)
plant4.showturtle()

plant5 = turtle.clone()
plant5.shape("plantx.gif")
plant5.penup()
plant5.goto(100,-400)
plant5.showturtle()

plant6 = turtle.clone()
plant6.shape("plantx.gif")
plant6.penup()
plant6.goto(-250,-320)
plant6.showturtle()

plant7 = turtle.clone()
plant7.shape("plantx.gif")
plant7.penup()
plant7.goto(-350,-150)
plant7.showturtle()

plant8 = turtle.clone()
plant8.shape("plantx.gif")
plant8.penup()
plant8.goto(-250,20)
plant8.showturtle()


#water can creating

waterCan =turtle.clone()
waterCan.hideturtle()
waterCan.penup()
waterCan.shape("waterCan.gif")
waterCan.goto(0, 220)
waterCan.showturtle()
questBorder = turtle.clone()
questBorder.shape("questBorder.gif")
questBorder.hideturtle()


#function that asks the question and suggest answers

def ask(question, answerA, answerB, answerC, answerD):

	a.clear()
	a.color('goldenrod')
	questBorder.penup()
	questBorder.goto(-650,150)
	questBorder.showturtle()
	a.penup()
	a.goto(-650,250)
	a.write(question, move=True, align="center", font=('arial', 15, 'bold'))
	a.goto(-800,150)
	a.write(answerA, move=True, align="left", font=('arial', 15, 'bold'))
	a.goto(-800,50)
	a.write(answerB, move=True, align="left", font=('arial', 15, 'bold'))
	a.goto(-600,150)
	a.write(answerC, move=True, align="left", font=('arial', 15, 'bold'))
	a.goto(-600,50)
	a.write(answerD, move=True, align="left", font=('arial', 15, 'bold'))
	


#no key has been pressed yet

aA= False
bA= False
cA= False
dA= False
score=0

#restart function

'''
def restart():
        global score, level
        score=0
        level=0
        plant1.shape("plantx.gif")
        plant2.shape("plantx.gif")
        plant3.shape("plantx.gif")
        plant4.shape("plantx.gif")
        plant5.shape("plantx.gif")
        plant6.shape("plantx.gif")
        plant7.shape("plantx.gif")
        plant8.shape("plantx.gif")
        waterCan.goto(0, 220)
        checkLevel()
        
        
'''








#check if the answer is correct and decides what to do

def checkAnswer():
		global level, aA, bA, cA, dA, score

		a.goto(-650,-100)
		
		if level == 1:
				
				if bA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant2.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
						
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant2.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()
		elif level == 5:
				
				if bA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant6.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
						
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant6.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()
		elif level == 2:
				
				if cA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant3.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant3.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()
		elif level == 3:
				
				if aA:
						a.color('red')
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant4.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant4.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()

		elif level == 4:
				
				if dA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant5.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant5.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()

		elif level == 6:				
				if dA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant7.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant7.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()

		elif level == 7:
				
				if dA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant8.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						checkLevel()
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant8.shape("deadPlant.gif")
						time.sleep(0.05)
						checkLevel()
		elif level == 8:
				
				if aA:
						a.color('green')
						a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
						plant1.shape("tree.gif")
						level+=1
						waterCan.shape("waterCan2.gif")
						time.sleep(0.3)
						plant1.shape("tree.gif")
						time.sleep(0.3)
						waterCan.shape("waterCan.gif")
						time.sleep(0.05)
						score+=1
						a.clear()
						a.goto(-630, 50)
						a.color('goldenrod')
						a.write("You planted \n"+ str(score) +"\8 trees!", move=True, align="center", font=('Comic Sans MS', 55, 'bold'))
						time.sleep(3)
						quit()
						'''
						a.clear()
						a.color('goldenrod')
						a.goto(-700, 50) 
						a.write("Press 'r' to restart \n or 'f' to finish!", move=True, align="center", font=('Comic Sans MS', 35, 'bold'))
						turtle.onkeypress(restart, "r")
						turtle.onkeypress(quit, "f")
						turtle.listen()
						'''
						
				else:
						a.color('red')
						a.write("Wrong!", move=True, align="center", font=('times', 35, 'bold'))
						level+=1
						time.sleep(0.3)
						plant1.shape("deadPlant.gif")
						time.sleep(0.05)
						a.clear()
						a.goto(-630, 50)
						a.color('goldenrod')
						a.write("You planted \n"+ str(score) +"\8 trees!", move=True, align="center", font=('Comic Sans MS', 55, 'bold'))
						time.sleep(3)
						quit()
						'''
						a.clear()
						a.color('goldenrod')
						a.goto(-700, 50)
						a.write("Press 'r' to restart \n or 'f' to finish!", move=True, align="center", font=('Comic Sans MS', 35, 'bold'))
						turtle.onkeypress(restart, "r")
						turtle.onkeypress(quit, "f")
						turtle.listen()
						'''
						




#define which question and answers are for each level

#first
firstQ = "how many trees are cut down \n each day for toilet paper?"
firstAnswerA = "A) 6,000"
firstAnswerB = "B) 27,000"
firstAnswerC = "C) 80,000"
firstAnswerD = "D) 1,000,000"

#second
secondQ = "How many years it takes to \n a glass bottle to decompose?"
secondAnswerA = "A) 1 year"
secondAnswerB = "B) 800 years"
secondAnswerC = "C) 4,000 years"
secondAnswerD = "D) 10,000 years"

#third
thirdQ = "How much percent from our \n planets water supply can be used?"
thirdAnswerA = "A) 1%"
thirdAnswerB = "B) 97%"
thirdAnswerC = "C) 2%"
thirdAnswerD = "D) 10%"


#fourth
fourthQ = "The world's oldest trees are \n more than _________ years old"
fourthAnswerA = "A) 9,800"
fourthAnswerB = "B) 7,000"
fourthAnswerC = "C) 600"
fourthAnswerD = "D) 4,600"


#fifth        
fifthQ = "Pollution has killed more \n than __________ people"
fifthAnswerA="A) 10 million"
fifthAnswerB="B) 100 million"
fifthAnswerC="C) 100,000 million"
fifthAnswerD="D) 1 trillion"


#sixth


sixthQ = "Every __________ of recycled \n paper saves___________ trees"
sixthAnswerA="A) 10 kilos , 1"
sixthAnswerB="B) 100 kilos  , 2"
sixthAnswerC="C) 20 tons , 2"
sixthAnswerD="D) 1 ton , 7"

#seventh

seventhQ = "How many aluminium cans \n do we consume every year? "
seventhAnswerA="A) around 8,000,000"
seventhAnswerB="B) over 800,000,000"
seventhAnswerC="C) over 8 trillion"
seventhAnswerD="D) over 80 trillion "

#eighth

eighthQ="How many liters of water do we \n use when we flush the toilets"
eighthAnswerA="A) 6 liters"
eighthAnswerB="B) 10 liters"
eighthAnswerC="C) 1 liter"
eighthAnswerD="D) 40 liters"


#what the user pressed and goes to check if correct

def userAnswerA():
	global aA, bA, cA, dA
	aA=True
	bA= False
	cA= False
	dA= False
	checkAnswer()
def userAnswerB():
	print("1")
	global aA, bA, cA, dA
	bA=True
	aA= False
	cA= False
	dA= False
	checkAnswer()
	
def userAnswerC():
	global aA, bA, cA, dA
	cA=True
	aA= False
	bA= False
	dA= False
	checkAnswer()
	
def userAnswerD():
	global aA, bA, cA, dA
	dA=True
	aA= False
	bA= False
	cA= False
	checkAnswer()
	


#levels (asking and waiting for an answer)

def levelOne():
	global level
	level=1
	ask(firstQ, firstAnswerA, firstAnswerB, firstAnswerC, firstAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()
	
def levelTwo():
	global level
	level=2
	ask(secondQ, secondAnswerA, secondAnswerB, secondAnswerC, secondAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()


def levelThree():
	global level
	level=3
	ask(thirdQ, thirdAnswerA, thirdAnswerB, thirdAnswerC, thirdAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()


def levelFour():
	global level
	level=4
	ask(fourthQ, fourthAnswerA, fourthAnswerB, fourthAnswerC, fourthAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()


def levelFive():
	global level
	level=5
	ask(fifthQ, fifthAnswerA, fifthAnswerB, fifthAnswerC, fifthAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()


def levelSix():
	global level
	level=6
	ask(sixthQ, sixthAnswerA, sixthAnswerB, sixthAnswerC, sixthAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()


def levelSeven():
	global level
	level=7
	ask(seventhQ, seventhAnswerA, seventhAnswerB, seventhAnswerC, seventhAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()


def levelEight():
	global level
	level=8
	ask(eighthQ, eighthAnswerA, eighthAnswerB, eighthAnswerC, eighthAnswerD)
	turtle.onkeypress(userAnswerA, "a")
	turtle.onkeypress(userAnswerB, "b")
	turtle.onkeypress(userAnswerC, "c")
	turtle.onkeypress(userAnswerD, "d")

	turtle.listen()

level=1


#check which level, moves the water can and links to the levels' function

def checkLevel():
		if level == 1:
				waterCan.goto(500, 170)
				levelOne()

		if level == 2:
				waterCan.goto(550, 0)
				levelTwo()

		if level == 3:
				
				waterCan.goto(450, -170)
				levelThree()

		if level == 4:
				
				waterCan.goto(100, -250)
				levelFour()

		if level == 5:
				
				waterCan.goto(-250, -170)
				levelFive()

		if level == 6:
				
				waterCan.goto(-350, 0)
				levelSix()

		if level == 7:
				
				waterCan.goto(-300, 170)
				levelSeven()

		if level == 8:
				
				waterCan.goto(100, 220)
				levelEight()
				


#call to function
				
checkLevel()


turtle.mainloop()


					  






