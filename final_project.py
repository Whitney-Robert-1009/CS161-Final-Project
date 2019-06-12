import turtle

screen = turtle.Screen()

answer = screen.textinput("Mystic Forest", "The fog has lifted\nand your path has become clear. \nWill you leave these woods?")

if answer is None or answer.lower().startswith('y'):
    print("Escape!")
else:
    print("The Mystic Forest haunts you!")
    answer = screen.textinput("Mystic Forest", "You are unable to roll-over and die. \nDo you agree?")

    if answer is None or answer.lower().startswith('y'):
        print("Then escape! Time is fleeting...")
    else:
        print("There is a strong wind. \nThe woods call you pathetic. \nYour ego is hurt. \n\nProve the woods wrong!")
wn = turtle.Screen()
wn.setup(700,900)
wn.bgcolor("black")

#create pen
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("triangle")
    self.color("green")
    self.penup()
    self.speed(0)
    
class Player(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("circle")
    self.color("khaki3")
    self.penup()
    self.speed(0)
    
  def go_up(self):
    move_to_x=player.xcor()
    move_to_y=player.ycor() + 24
    
    if (move_to_x,move_to_y) not in trees:
        self.goto(move_to_x, move_to_y)
  
  def go_down(self):
    move_to_x=player.xcor()
    move_to_y=player.ycor() - 24
    
    if (move_to_x,move_to_y) not in trees:
        self.goto(move_to_x, move_to_y)  
        
  def go_right(self):
    move_to_x=player.xcor() + 24
    move_to_y=player.ycor()
    
    if (move_to_x,move_to_y) not in trees:
        self.goto(move_to_x, move_to_y) 
        
  def go_left(self):
    move_to_x=player.xcor() - 24
    move_to_y=player.ycor()
    
    if (move_to_x,move_to_y) not in trees:
        self.goto(move_to_x, move_to_y) 

#create Levels list
levels = [""]

#define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXX            XXXXXX",
"X       XXXXXXXX   XXXXXX",
"XXX  XX XXXXXXXX   XXXXXX",
"XXX  XX XX   XX       XXX",
"XX   XX XX X  XXXXXX  XXX",
"X   XX  XX X    XXX  XXXX",
"XX   XXXX  XXXX     XXXXX",
"XXXXX  XXX XXXXXXXX  XXXX",
"XX   XX X    XXXXXXX XXXX",
"X  X    X XX XXXXXXX XXXX",
"X  X     X X  X X  X X  X",
"X XX  XXXX XX  XXXXXXXXXX",
"X  X  XX   XX XXXXXXXXXXX",
"XX  X  XXXXXX     XX   XX",
"XX X X   XXXXXX   XXXXXXX",
"X  X X   XXXXXX   XXXXXXX",
"X XX XXX          XXXX  X",
"X  X    XXXXXXXXX    XXXX",
"XX X   XX  XXXXXX    XXXX",
"X  XXX    XXXXXXX  XXXXXX",
"X XX  XXXXXXXXX   XXX  XX",
"X  X  XX       XXX   XXXX",
"X                       X",
"XXXXXXXXXXXXXXX XXXXXXXXX",
"X    XX XXXX XX XX     XX",
"X XXXXXX XX XXX XXXX XXXX",
"X   XXXXX  XXXX XXXX XXXX",
"X XXXXXX XX XXX XXXX XXXX",
"X    XX XXXX XX XXXX XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add maze to mazes list
levels.append(level_1)

#Create Level Setup Function

def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      #Get the Character at each x,y coordinate
      #NOTE the order of the y and x in the next line
      character = level[y][x]
      #Calculate the screen x, y coordinates
      screen_x = -288 + (x * 24)
      screen_y = 288 - (y * 24)
      
      #Check if it is an X (representing a tree)
      if character == "X":
        pen.goto(screen_x, screen_y)
        pen.stamp()
        trees.append((screen_x,screen_y))
        
      if character == "P":
        player.goto(screen_x, screen_y)
        
#Create class instances
pen = Pen()
player=Player()

# trees
trees=[]
print(trees)

#Set up the level
setup_maze(levels[1])
print(trees)


#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")


#Turn off screen upates
wn.tracer(0)


#Main Game Loop
while True:
  # Update Screen
    wn.update()
