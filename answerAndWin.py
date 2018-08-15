import turtle
import time
level=0
SIZE_X=1910
SIZE_Y=1070
turtle.setup(SIZE_X, SIZE_Y)
turtle.delay()

turtle.register_shape("questBorder.gif")
turtle.register_shape("waterCan.gif")
turtle.register_shape("gameoverv1.gif")
turtle.register_shape("plantx.gif")
turtle.register_shape("tree.gif")
turtle.register_shape("questBorder.gif")
turtle.register_shape("waterCan2.gif")

questBorder = turtle.clone()
questBorder.shape("questBorder.gif")
questBorder.hideturtle()
turtle.hideturtle()
a=turtle.clone()
a.hideturtle()
titleTurtle = turtle.clone()
titleTurtle.hideturtle()
titleTurtle.penup()
titleTurtle.goto(0,350)
titleTurtle.color('black')
titleTurtle.write("Answer And Win!", move=True, align="center", font=('Comic Sans MS', 100, 'bold'))
titleTurtle.hideturtle()

plant1 = turtle.clone()
plant1.shape("plantx.gif")
plant1.penup()
plant1.goto(0,70)
plant1.showturtle()


plant2 = turtle.clone()
plant2.shape("plantx.gif")
plant2.penup()
plant2.goto(400,20)
plant2.showturtle()

plant3 = turtle.clone()
plant3.shape("plantx.gif")
plant3.penup()
plant3.goto(450,-150)
plant3.showturtle()

plant4 = turtle.clone()
plant4.shape("plantx.gif")
plant4.penup()
plant4.goto(350,-320)
plant4.showturtle()

plant5 = turtle.clone()
plant5.shape("plantx.gif")
plant5.penup()
plant5.goto(0,-400)
plant5.showturtle()

plant6 = turtle.clone()
plant6.shape("plantx.gif")
plant6.penup()
plant6.goto(-350,-320)
plant6.showturtle()

plant7 = turtle.clone()
plant7.shape("plantx.gif")
plant7.penup()
plant7.goto(-450,-150)
plant7.showturtle()

plant8 = turtle.clone()
plant8.shape("plantx.gif")
plant8.penup()
plant8.goto(-400,20)
plant8.showturtle()

gameover=turtle.clone()
gameover.shape("gameoverv1.gif")
gameover.hideturtle()
waterCan =turtle.clone()
waterCan.hideturtle()
waterCan.penup()
waterCan.shape("waterCan.gif")
waterCan.goto(0, 220)
waterCan.showturtle()

#moving the water can to every plant
# if True:
	
	#waterCan.right(90)
	#waterCan.left(90)

'''
if True:
	waterCan.goto(450, 0)
	#waterCan.right(90)
	#waterCan.left(90)

if True:
	waterCan.goto(350, -170)
	#waterCan.right(90)
	#waterCan.left(90)

if True:
	waterCan.goto(0, -250)
	#waterCan.right(90)
	#waterCan.left(90)

if True:
	waterCan.goto(-350, -170)
	#waterCan.right(90)
	#waterCan.left(90)
if True:
	waterCan.goto(-450, 0)
	#waterCan.right(90)
	#waterCan.left(90)

if True:
	waterCan.goto(-400, 170)
	#waterCan.right(90)
	#waterCan.left(90)
'''


#waterCan.shape("circle")
#waterCan.pensize(100)
#waterCan.turtlesize(5)




def ask(question, answerA, answerB, answerC, answerD):

        a.clear()
        questBorder.showturtle()
        a.penup()
        a.goto(-550,300)
        a.write(question, move=True, align="center", font=('arial', 15, 'bold'))
        a.goto(-800,200)
        a.write(answerA, move=True, align="center", font=('arial', 15, 'bold'))
        a.goto(-600,200)
        a.write(answerB, move=True, align="center", font=('arial', 15, 'bold'))
        a.goto(-400,200)
        a.write(answerC, move=True, align="center", font=('arial', 15, 'bold'))
        a.goto(-200,200)
        a.write(answerD, move=True, align="center", font=('arial', 15, 'bold'))
        

aA= False
bA= False
cA= False
dA= False

def checkAnswer():
	global level, aA, bA, cA, dA

	a.goto(-550,100)
	
	if level == 1 or level == 5:
		
		if bA:
			a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
			level+=1
			checkLevel()
			
		else:
			gameover.showturtle()
			quit()
	elif level == 2:
		
		if cA:
			a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
			level+=1
			checkLevel()
		else:
			gameover.showturtle()
			quit()
	elif level == 3:
		
		if aA:
			a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
			level+=1
			checkLevel()
		else:
			gameover.showturtle()
			quit()

	elif level == 4 or level == 6 or level == 7:
		
		if dA:
			a.write("Right Answer!", move=True, align="center", font=('times', 35, 'bold'))
			level+=1
			checkLevel()
		else:
			gameover.showturtle()
			quit()
	elif level == 8:
		
		if aA:
			a.write("Right Answer! \n You WON the game", move=True, align="center", font=('times', 35, 'bold'))
			plant1.shape("tree.gif")
			level+=1
			checkLevel()
		else:
			gameover.showturtle()
			quit()

	














#define which question and answers

#first
firstQ = "how many trees are cut down each day for toilet paper?"
firstAnswerA = "A) 6,000"
firstAnswerB = "B) 27,000"
firstAnswerC = "C) 80,0000"
firstAnswerD = "D) 1,000,000"

#second
secondQ = "How many years it takes to a glass bottle to decompose?"
secondAnswerA = "A) 1 year"
secondAnswerB = "B) 800 years"
secondAnswerC = "C) 4,000"
secondAnswerD = "D) 10,000"

#third
thirdQ = "How much percent from our planets water supply can be used?"
thirdAnswerA = "A) 1%"
thirdAnswerB = "B) 97%"
thirdAnswerC = "C) 2%"
thirdAnswerD = "D) 10%"


#fourth
fourthQ = "The world's oldest trees are more than _________ years old"
fourthAnswerA = "A) 9,800"
fourthAnswerB = "B) 7,000"
fourthAnswerC = "C) 600"
fourthAnswerD = "D) 4,600"


#fifth        
fifthQ = "Pollution has killed more than __________ people"
fifthAnswerA="A) 10 million"
fifthAnswerB="B) 100 million"
fifthAnswerC="C) 100,000"
fifthAnswerD="D) 1 trillion"
#sixth




sixthQ = "Every __________ of recycled paper saves___________ trees"
sixthAnswerA="A) 1,00 , 2"
sixthAnswerB="B) 10,000 , 1"
sixthAnswerC="C) 20 tons , 2"
sixthAnswerD="D) 1 ton , 7"

#seventh

seventhQ = "How many aluminium cans do we consume every year? "
seventhAnswerA="A) 8,000,000"
seventhAnswerB="B) over 800,000,000"
seventhAnswerC="C) over 8 trillion"
seventhAnswerD="D) over 80 trillion "

#eighth

eighthQ="How many liters of water do we use when we flush the toilets"
eighthAnswerA="A) 6 liters"
eighthAnswerB="B) 10 liters "
eighthAnswerC="C) 1 liter"
eighthAnswerD="D) 40 liters "

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
	print("level2")
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


def checkLevel():
        if level == 1:
                waterCan.goto(400, 170)
                levelOne()

        if level == 2:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant2.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(450, 0)
                levelTwo()

        if level == 3:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant3.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(350, -170)
                levelThree()

        if level == 4:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant4.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(0, -250)
                levelFour()

        if level == 5:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant5.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(-350, -170)
                levelFive()

        if level == 6:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant6.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(-450, 0)
                levelSix()

        if level == 7:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant7.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(-400, 170)
                levelSeven()

        if level == 8:
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant8.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)
                waterCan.goto(0, 220)
                levelEight()
                waterCan.shape("waterCan2.gif")
                time.sleep(0.3)
                plant8.shape("tree.gif")
                time.sleep(0.3)
                waterCan.shape("waterCan.gif")
                time.sleep(0.05)


checkLevel()





'''
levelTwo()
levelThree()
levelFour()
levelFive()
levelSix()
levelSeven()
levelEight()
'''
'''
ask(secondQ, secondAnswerA, secondAnswerB, secondAnswerC, secondAnswerD)

ask(thirdQ, thirdAnswerA, thirdAnswerB, thirdAnswerC, thirdAnswerD)

ask(fourthQ, fourthAnswerA, fourthAnswerB, fourthAnswerC, fourthAnswerD)

ask(fifthQ, fifthAnswerA, fifthAnswerB, fifthAnswerC, fifthAnswerD)

ask(sixthQ, sixthAnswerA, sixthAnswerB, sixthAnswerC, sixthAnswerD)

ask(seventhQ, seventhAnswerA, seventhAnswerB, seventhAnswerC, seventhAnswerD)

ask(eighthQ, eighthAnswerA,eighthAnswerB ,eighthAnswerC ,eighthAnswerD)
'''















'''
userAnswer=str(input(""))

count = "b"
if count != userAnswer:
	print('wrong answer')
elif count== userAnswer:
	print('right answer')

count = "c"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

count = "a"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

count = "d"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

count = "b"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

count = "d"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

count = "d"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

count = "a"
if count != userAnswer:
	print('wrong answer')
elif count == userAnswer:
	print('right answer')

if level==1:
	ask(firstQ, firstAnswerA, firstAnswerB ,firstAnswerC ,firstAnswerD)
elif level==2:
	ask(secondQ, secondAnswerA, secondAnswerB ,secondAnswerC ,secondAnswerD)
elif level==3:
	ask(thirdQ, thirdAnswerA, thirdAnswerB ,thirdAnswerC ,thirdAnswerD)
elif level==4:
	ask(forthQ, forthAnswerA,forthAnswerB ,forthAnswerC ,forthAnswerD)
elif level==5:
	ask(fifthQ, fifthAnswerA,fifthAnswerB ,fifthAnswerC ,fifthAnswerD)
elif level==6:
	ask(sixthQ, sixthAnswerA,sixthAnswerB ,sixthAnswerC ,sixthAnswerD)
elif level==7:
	ask(seventhQ, seventhAnswerA,seventhAnswerB ,seventhAnswerC ,seventhAnswerD)
elif level==8:
	ask(eighthQ, eighthAnswerA,eighthAnswerB ,eighthAnswerC ,eighthAnswerD)
'''






turtle.mainloop()


					  






