import turtle


SIZE_X=1910
SIZE_Y=1070
turtle.setup(SIZE_X, SIZE_Y)


turtle.register_shape("waterCan.gif")
turtle.register_shape("gameoverv1.gif")
turtle.register_shape("plant.gif")
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


gameover=turtle.clone()
gameover.hideturtle()
waterCan =turtle.clone()
waterCan.hideturtle()
waterCan.penup()
waterCan.shape("waterCan.gif")
waterCan.goto(0, 220)
waterCan.showturtle()

#moving the water can to every plant
if True:
    waterCan.goto(400, 170)
    #waterCan.right(90)
    #waterCan.left(90)
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



#waterCan.shape("circle")
#waterCan.pensize(100)
#waterCan.turtlesize(5)




def  ask (question, answerA, answerB, answerC, answerD) :

    a.penup()
    a.goto(-550,300)
    a.write(question, move=True, align="center", font=('arial', 15, 'bold'))
    a.goto(-750,200)
    a.write(answerA, move=True, align="center", font=('arial', 15, 'bold'))
    a.goto(-650,200)
    a.write(answerB, move=True, align="center", font=('arial', 15, 'bold'))
    a.goto(-550,200)
    a.write(answerC, move=True, align="center", font=('arial', 15, 'bold'))
    a.goto(-425,200)
    a.write(answerD, move=True, align="center", font=('arial', 15, 'bold'))

    

























#define which question and answers

#first
firstQ = "how much trees cut down each day for toilet paper?"
firstAnswerA = "A) 6,000"
firstAnswerB = "B) 27,000"
firstAnswerC = "C) 80,0000"
firstAnswerD = "D) 1,000,000"

#second
secondQ = "How many years take to a glass bottle to decompose?"
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
fourthQ = "The world's oldest trees are more then _________ years old"
fourthAnswerA = "A) 9,800"
fourthAnswerB = "B) 7,000"
fourthAnswerC = "C) 600"
fourthAnswerD = "D) 4,600"


#fifth        
fifthQ = "Pollution has killed more then __________ people"
fifthAnswerA="A) 10 million"
fifthAnswerB="B) 100 million"
fifthAnswerC="C) 100,000"
fifthAnswerD="D) 1 trillion"
#sixth




sixthQ = "every __________ of recycled paper saves___________ trees"
sixthAnswerA="A) 1,00 , 2"
sixthAnswerB="B) 10,000 , 1"
sixthAnswerC="C) 20 tons , 2"
sixthAnswerD="D) 1 ton , 7"

#seventh

seventhQ="how many aluminium cans do we consume every year? "
seventhAnswerA="A) 8,000,000"
seventhAnswerB="B) over 800,000,000"
seventhAnswerC="C) over 8 trillion"
seventhAnswerD="D) over 80 trillion "

#eighth

eighthQ="how many liters of water do we use when we flush the toilets"
eighthAnswerA="A) 6 liters"
eighthAnswerB="B) 10 liters "
eighthAnswerC="C) 1 liter"
eighthAnswerD="D) 40 liters "


#call to functions 
ask(firstQ, firstAnswerA, firstAnswerB, firstAnswerC, firstAnswerD)
ask(secondQ, secondAnswerA, secondAnswerB, secondAnswerC, secondAnswerD)
ask(thirdQ, thirdAnswerA, thirdAnswerB, thirdAnswerC, thirdAnswerD)
ask(fourthQ, fourthAnswerA, fourthAnswerB, fourthAnswerC, fourthAnswerD)
ask(fifthQ, fifthAnswerA, fifthAnswerB, fifthAnswerC, fifthAnswerD)
ask(sixthQ, sixthAnswerA, sixthAnswerB, sixthAnswerC, sixthAnswerD)
ask(seventhQ, seventhAnswerA, seventhAnswerB, seventhAnswerC, seventhAnswerD)















#noya is here

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
    




turtle.mainloop()


                      






