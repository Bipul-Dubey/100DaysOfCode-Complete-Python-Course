import turtle,pandas

screen=turtle.Screen()
screen.title("India States Game")
image="India States Map.gif"
screen.setup(height=800)
screen.addshape(image)
turtle.shape(image)

# to get the coordinates (x,y)
def get_more_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_more_click_coor)
turtle.mainloop()

# screen.exitonclick()