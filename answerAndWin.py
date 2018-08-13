import turtle


SIZE_X=1910
SIZE_Y=1070
turtle.setup(SIZE_X, SIZE_Y)


turtle.register_shape("waterCan.gif")
turtle.register_shape("gameoverv1.gif")
turtle.register_shape("plant.gif")
turtle.hideturtle()


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





























#BSHARA IS HERE
a=turtle.clone()
a.hideturtle()
a.penup()
a.goto(-550,300)
a.write("how much trees cut down each day for toilet paper?", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 6,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 27,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 80,0000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 1,000,000", move=True, align="center", font=('arial', 15, 'bold'))

a.goto(-550,300)
a.write("How many years take to a glass bottle to decompose?", move = True, align = "center", font = ('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 1 year", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 800 years", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 4,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 10,000", move=True, align="center", font=('arial', 15, 'bold'))

a.goto(-550,300)
a.write("How much percent from our planets water supply can be used?", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 1%", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 97%", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 2%" , move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 10%", move=True, align="center", font=('arial', 15, 'bold'))

a.goto(-550,300)
a.write("The world's oldest trees are more then _________ years old", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 9,800", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 7,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 600", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 4,600", move=True, align="center", font=('arial', 15, 'bold'))

a.goto(-550,300)
a.write("Pollution has killed more then __________ people", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 10 million", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 100 million", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 100,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 1 trillion", move=True, align="center", font=('arial', 15, 'bold'))




a.goto(-550,300)
a.write("every __________ of recycled paper saves___________ trees", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 1,00 , 2", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 10,000 , 1", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 20 tons , 2", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 1 ton , 7", move=True, align="center", font=('arial', 15, 'bold'))

a.goto(-550,300)
a.write("how many aluminium cans do we consume every year? ", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 8,000,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) over 800,000,000", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) over 8 trillion", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) over 80 trillion ", move=True, align="center", font=('arial', 15, 'bold'))


a.goto(-550,300)
a.write("how many liters of water do we use when we flush the toilets", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-750,200)
a.write("A) 6 liters", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-650,200)
a.write("B) 10 liters ", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-550,200)
a.write("C) 1 liter", move=True, align="center", font=('arial', 15, 'bold'))
a.goto(-425,200)
a.write("D) 40 liters ", move=True, align="center", font=('arial', 15, 'bold'))











turtle.mainloop()


                      
