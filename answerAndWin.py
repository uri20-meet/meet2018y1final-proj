import turtle


SIZE_X=1910
SIZE_Y=1070
turtle.setup(SIZE_X, SIZE_Y)


turtle.register_shape("waterCan.gif")
turtle.register_shape("gameoverv1.gif")
turtle.register_shape("plant.gif")




gameover1=turtle.clone()
waterCan =turtle.clone()
waterCan.shape("waterCan.gif")
#waterCan.shape("circle")
#waterCan.pensize(100)
#waterCan.turtlesize(5)

                      

waterCan.showturtle()






turtle.mainloop()


                      
