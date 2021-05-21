# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# turtle.speed(10)
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x/100 + 1)
#     t.forward(x)
#     t.left(59)

# import turtle
# loadWindow = turtle.Screen()
# turtle.speed(2)
 
# for i in range(100):
#     turtle.circle(5*i)
#     turtle.circle(-5*i)
#     turtle.left(i)
 
# turtle.exitonclick()

# import turtle #Inside_Out
# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")

# def sqrfunc(size):
# 	for i in range(4):
# 		skk.fd(size)
# 		skk.left(90)
# 		size = size + 5

# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)

# import turtle
# screen = turtle.Screen()
# screen.title('Triangle Spiral - PythonTurtle.Academy')
# turtle.setup(1000,1000)
# screen.setworldcoordinates(-1000,-1000,1000,1000)
# turtle.speed(0)
# turtle.hideturtle()

# for i in range(10,1550,9):
#     turtle.fd(i)
#     turtle.left(119.3)


# import turtle

# screen = turtle.Screen()
# screen.setup(800,800)
# screen.setworldcoordinates(-8,-8,8,8)
# screen.tracer(0,0)
# screen.title('Bulge Illusion - PythonTurtle.Academy')
# turtle.hideturtle()
# turtle.speed()

# color1 = 'light sky blue'
# color2 = 'firebrick'
# screen.bgcolor(color2)

# def draw_square(x,y,size,c):
#     turtle.up()
#     turtle.goto(x-size/2,y-size/2)
#     turtle.seth(0)
#     turtle.color(c)
#     turtle.begin_fill()
#     for _ in range(4):
#         turtle.fd(size)
#         turtle.left(90)
#     turtle.end_fill()
    
# def draw_board():
#     for x in range(-7,8,2):
#         for y in range(-7,8,2):
#             draw_square(x,y,1,color1)
#     for x in range(-6,8,2):
#         for y in range(-6,8,2):
#             draw_square(x,y,1,color1)
            

# def draw_diag(x,y):
#     c = color2 if (x+y)%2 == 0 else color1
#     if x*y > 0:
#         draw_square(x-0.3,y+0.3,0.3,c)
#         draw_square(x+0.3,y-0.3,0.3,c)
#     elif x*y < 0:
#         draw_square(x+0.3,y+0.3,0.3,c)
#         draw_square(x-0.3,y-0.3,0.3,c)

# def draw_straight(x,y):
#     c = color2 if (x+y)%2 == 0 else color1
#     if y>0:
#         draw_square(x-0.3,y-0.3,0.3,c)
#         draw_square(x+0.3,y-0.3,0.3,c)
#     elif y<0:
#         draw_square(x-0.3,y+0.3,0.3,c)
#         draw_square(x+0.3,y+0.3,0.3,c)
#     elif x>0:
#         draw_square(x-0.3,y-0.3,0.3,c)
#         draw_square(x-0.3,y+0.3,0.3,c)
#     elif x<0:
#         draw_square(x+0.3,y-0.3,0.3,c)
#         draw_square(x+0.3,y+0.3,0.3,c)
        
# def draw_bulge():
#     for x in range(-6,7):
#         for y in range(-6,7):
#             if abs(x)+abs(y)<=7:
#                 draw_diag(x,y)
#                 if x==0 or y==0: draw_straight(x,y)
#     x,y = -5,-3
#     for i in range(3):
#         draw_diag(x,y)
#         draw_diag(-x,-y)
#         draw_diag(x,-y)
#         draw_diag(-x,y)
#         x += 1
#         y -= 1
# draw_board()
# draw_bulge()

# screen.update()



# import turtle
# import datetime
# import math

# screen = turtle.Screen()
# screen.title('Continuous Clock - PythonTurtle.Academy')
# screen.bgcolor('sky blue')
# screen.setup(1000,1000)
# screen.setworldcoordinates(-1000,-1000,1000,1000)
# screen.tracer(0,0)


# class clock:
#     def __init__(self,hour,minute,second):
#         self.hour, self.minute, self.second = hour, minute, second
#         self.microsecond = 0
#         self.face = turtle.Turtle()
#         self.hand = turtle.Turtle()
#         self.face.hideturtle()
#         self.hand.hideturtle()

#     def draw(self):
#         self.draw_face()
#         self.draw_hand()
        
#     def draw_face(self):
#         self.face.clear()
#         self.face.up()
#         self.face.goto(0,-700)
#         self.face.pensize(4)
#         self.face.down()
#         self.face.fillcolor('white')
#         self.face.begin_fill()
#         self.face.circle(700,steps=100)
#         self.face.end_fill()
#         self.face.up()
#         self.face.goto(0,0)
#         self.face.dot(10)
#         self.face.pensize(2)
#         for angle in range(0,360,6):
#             self.face.up()
#             self.face.goto(0,0)
#             self.face.seth(90-angle)
#             self.face.fd(620)
#             self.face.down()
#             self.face.fd(30)
            
#         self.face.pensize(3)
#         for angle in range(0,360,30):
#             self.face.up()
#             self.face.goto(0,0)
#             self.face.seth(90-angle)
#             self.face.fd(600)
#             self.face.down()
#             self.face.fd(50)
            
#         self.face.pensize(4)
#         for angle in range(0,360,90):
#             self.face.up()
#             self.face.goto(0,0)
#             self.face.seth(90-angle)
#             self.face.fd(580)
#             self.face.down()
#             self.face.fd(70)
        
#     def draw_hand(self):    
#         self.hand.clear()       
#         self.hand.up()
#         self.hand.goto(0,0)
#         self.hand.seth(90-math.floor(((self.hour%12)*60*60*1000000+self.minute*60*1000000+self.second*1000000+self.microsecond)/3600000000*30))
#         self.hand.down()
#         self.hand.color('black')
#         self.hand.pensize(6)
#         self.hand.fd(300)

#         self.hand.up()
#         self.hand.goto(0,0)
#         self.hand.seth(90-math.floor((self.minute*60*1000000+self.second*1000000+self.microsecond)/60000000*6))
#         self.hand.down()
#         self.hand.color('black')
#         self.hand.pensize(4)
#         self.hand.fd(400)

#         self.hand.up()
#         self.hand.color('red')
#         self.hand.goto(0,0)
#         self.hand.dot(5)
#         self.hand.seth(90-(self.second*1000000+self.microsecond)/1000000*6)
#         self.hand.down()
#         self.hand.pensize(2)
#         self.hand.fd(570)

# def animate():
#     global c
#     d = datetime.datetime.now()
#     c.hour, c.minute, c.second, c.microsecond = d.hour, d.minute, d.second, d.microsecond
#     c.draw_hand()
#     screen.update()
#     screen.ontimer(animate,100)
    
# d = datetime.datetime.now()
# c = clock(d.hour,d.minute,d.second)
# c.draw_face()
# screen.update()
# animate()



# import turtle
# import datetime
# screen = turtle.Screen()
# screen.title('Clock - PythonTurtle.Academy')
# screen.setup(1000,1000)
# screen.setworldcoordinates(-1000,-1000,1000,1000)
# screen.tracer(0,0)
# screen.bgcolor('sky blue')

# class clock:
#     def __init__(self,hour,minute,second):
#         self.hour, self.minute, self.second = hour, minute, second
#         self.face = turtle.Turtle()
#         self.hand = turtle.Turtle()
#         self.face.hideturtle()
#         self.hand.hideturtle()

#     def draw(self):
#         self.draw_face()
#         self.draw_hand()
        
#     def draw_face(self):
#         self.face.clear()
#         self.face.up()
#         self.face.goto(0,-700)
#         self.face.pensize(5)
#         self.face.down()
#         self.face.fillcolor('white')
#         self.face.begin_fill()
#         self.face.circle(700)
#         self.face.end_fill()
#         self.face.up()
#         self.face.goto(0,0)
#         self.face.dot(10)
#         self.face.pensize(2)
#         for angle in range(0,360,6):
#             self.face.up()
#             self.face.goto(0,0)
#             self.face.seth(90-angle)
#             self.face.fd(620)
#             self.face.down()
#             self.face.fd(30)
#         self.face.pensize(4)
#         for angle in range(0,360,30):
#             self.face.up()
#             self.face.goto(0,0)
#             self.face.seth(90-angle)
#             self.face.fd(600)
#             self.face.down()
#             self.face.fd(50)
        
#     def draw_hand(self):    
#         self.hand.clear()       
#         self.hand.up()
#         self.hand.goto(0,0)
#         self.hand.seth(90-self.hour%12*360//12)
#         self.hand.down()
#         self.hand.color('black')
#         self.hand.pensize(6)
#         self.hand.fd(300)

#         self.hand.up()
#         self.hand.goto(0,0)
#         self.hand.seth(90-self.minute*6)
#         self.hand.down()
#         self.hand.color('black')
#         self.hand.pensize(4)
#         self.hand.fd(400)

#         self.hand.up()
#         self.hand.color('red')
#         self.hand.goto(0,0)
#         self.hand.dot(5)
#         self.hand.seth(90-self.second*6)
#         self.hand.down()
#         self.hand.pensize(2)
#         self.hand.fd(600)

# def animate():
#     global c
#     d = datetime.datetime.now()
#     c.hour, c.minute, c.second = d.hour, d.minute, d.second
#     c.draw_hand()
#     screen.update()
#     screen.ontimer(animate,1000)
    
# d = datetime.datetime.now()
# c = clock(d.hour,d.minute,d.second)
# c.draw_face()
# screen.update()
# animate()





# import turtle
# turtle.title('Sierpinski Tree Animation - TECH_IN_SECONDS')
# turtle.setworldcoordinates(-2000,-2000,2000,2000)
# screen = turtle.Screen()
# screen.tracer(0,0)
# turtle.speed(5)
# turtle.hideturtle()

# def sierpinski_tree(x,y,length,tilt,angle,n):
#     if n==0: return
#     turtle.up()
#     turtle.goto(x,y)
#     turtle.seth(tilt)
#     turtle.down()
#     turtle.fd(length)
#     sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)
    
#     turtle.up()
#     turtle.goto(x,y)
#     turtle.seth(tilt+angle)
#     turtle.down()
#     turtle.fd(length)
#     sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)

#     turtle.up()
#     turtle.goto(x,y)
#     turtle.seth(tilt-angle)
#     turtle.down()
#     turtle.fd(length)
#     sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)

# def animate():
#     global angle
#     turtle.clear()
#     sierpinski_tree(0,-250,1000,90,angle,7)
#     screen.update()
#     angle = 120 if angle <= 20 else angle-2
#     screen.ontimer(animate,50)

# angle = 120
# animate()
# screen.mainloop()


# import turtle
# import math

# screen = turtle.Screen()
# screen.title('Dodecagon Spiral - PythonTurtle.Academy')
# screen.setup(1000,1000)
# screen.setworldcoordinates(-1000,-1000,1000,1000)
# turtle.speed(0)
# turtle.hideturtle()

# def draw_spiral(x,y,r,direction):
#     if r < 10: return
#     d = direction
#     r2 = r*math.cos(math.radians(360/24))/math.cos(math.radians(360/24-alpha))
#     dist = r*math.sin(math.radians(360/24))-r2*math.sin(math.radians(360/24-alpha))
#     turtle.up()
#     px = x + r*math.cos(math.radians(d))
#     py = y + r*math.sin(math.radians(d))
#     turtle.goto(px,py)
#     turtle.color((1-r/900,1-r/900,1-r/900))
#     turtle.down()
#     d += 360/12
#     for _ in range(12):
#         px = x + r*math.cos(math.radians(d))
#         py = y + r*math.sin(math.radians(d))
#         turtle.goto(px,py)
#         d += 360/12
#     draw_spiral(x,y,r2,direction+alpha)
    
    
# alpha = 3
# draw_spiral(0,0,900,90)



