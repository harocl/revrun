# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Harry Oclarit
# David Lloyd
# Austin Thames 
# Section: 507
# Assignment: LAB: Topic 13
# Date: 3/12/23
import turtle
from ursina import *
import random as r


screen = turtle.Screen() 
screen.setup(width=1.0, height=1.0) # Make the window fullscreen
screen.bgpic('Reveille_Run\\stuff\\menu_back.png')

def draw_image():
  '''Draws the turtle graphics ("REV RUN") at the beginning
  of the program'''
  t = turtle.Turtle()
  # Set the pen color to maroon
  # Hide the turtle
  t.hideturtle()
  t.pencolor("maroon")
  t.pensize(10)
  t.speed(7)

  #R
  t.penup()
  t.goto(-627, 160)
  t.pendown()
  t.right(-90)
  t.forward(205)
  t.right(90)
  t.forward(60)
  t.circle(-50, 180)
  t.forward(60)
  t.penup()
  t.goto(-575, 263)
  t.pendown()
  t.right(240)
  t.forward(115)

  #E
  t.penup()
  t.goto(-350, 160)
  t.pendown()
  t.right(120)
  t.forward(105)
  t.right(90)
  t.forward(205)
  t.right(90)
  t.forward(105)
  t.penup()
  t.goto(-454, 266)
  t.pendown()
  t.forward(60)

  #V
  t.penup()
  t.goto(-284, 365)
  t.pendown()
  t.right(70)
  t.forward(210)
  t.right(215)
  t.forward(205)

  #R
  t.penup()
  t.right(75)
  t.goto(36, 160)
  t.pendown()
  t.right(-90)
  t.forward(205)
  t.right(90)
  t.forward(60)
  t.circle(-50, 180)
  t.forward(60)
  t.penup()
  t.goto(92, 263)
  t.pendown()
  t.right(240)
  t.forward(115)

  #U
  t.penup()
  t.goto(212, 365)
  t.pendown()
  t.right(30)
  t.forward(145)
  t.circle(60,180)
  t.forward(145)

  #N
  t.penup()
  t.goto(416, 160)
  t.pendown()
  t.forward(205)
  t.right(150)
  t.forward(235)
  t.left(150)
  t.forward(205)

# Call the function to draw the image
# draw_image()

app=Ursina()
# Plane (Maroon background)
plane = Entity(model='quad', scale=(20, 10), color=color.rgb(36, 3, 8), z=10)
# Middle White Background for transparent clouds
middle = Entity(parent=plane, model='quad', scale=(1.5,0.8), position=(0, 0, -.99), color=color.white)
window.fullscreen = True

#Main Menu Background
background=Entity(
    model='quad',
    texture='stuff\menu.png',
    scale=(16, 9),
    z=1,
)
'''Reveille Entity (with collider)'''
reveille=Animation('stuff\\reveille',
                 collider='box',
                 scale=(1, 0.6, 1),
                 position=(1,-3, 1),
                 x=-3,
                 z=2
                 )

offset_ground=0
'''first half of the background'''
ground1=Entity(
  model='quad',
  texture='stuff\ground',
  scale=(70, 4.7, 1),
  position=(0,-1.8, 5),
  z=4
)

offset_sky=0
'''sky backdrop'''
sky=Entity(
  model='quad',
  texture='stuff\sky',
  scale=(70, 4.7, 1),
  position=(0, 1.9, 0),
  z=7
)

'''plane entity'''
plane=Entity(
  model='quad',
  texture='stuff\plane',
  x=20,
  y=3,
  scale=(2.2, 1, 1),
  z=6
)
planes= []
def newPlane():
  '''Duplicates the entity Plane'''
  n=0
  new=duplicate(plane,
                  x=n + r.randint(10, 15))
  planes.append(new)
  n += 30
  invoke(newPlane, delay=40)

newPlane()

'''water tower entity'''
water_tower=Entity(
  model='quad',
  texture='stuff\watertower',
  x=20,
  y=1.6,
  scale=(2, 3.5, 1),
  z=5
)

watertower=[]
def newWaterTower():
  '''Duplicates the entity Water Tower'''
  new=duplicate(water_tower,
                  x=20)
  watertower.append(new)
  invoke(newWaterTower, delay=24)

newWaterTower()

'''academic building entity'''
academic_bldg=Entity(
  model='quad',
  texture='stuff\\academic',
  x=20,
  y=.9,
  scale=(4.7, 1.5, 1),
  z=5
)

academics=[]
def newAcademicBldg():
  '''Duplicates the entity Academic Building'''
  new=duplicate(academic_bldg,
                  x=23.5)
  academics.append(new)
  invoke(newAcademicBldg, delay=24)

newAcademicBldg()

'''zachry building entity'''
zach_bldg=Entity(
  model='quad',
  texture='stuff\\zach',
  x=35,
  y=.9,
  scale=(4.7, 1.5, 1),
  z=5
)
zachs=[]
def newZachryBldg():
  '''Duplicates the entity Zachry Building'''
  new=duplicate(zach_bldg,
                  x=35)
  zachs.append(new)
  invoke(newZachryBldg, delay=24)

newZachryBldg()

#field goal entity
goal_1=Entity(
  model='quad',
  texture='stuff\goal_1',
  position=(20, -1.7, 3),
  scale=(1.5, 2.5, 0)
)
goal_2=Entity(
  model='quad',
  texture='stuff\goal_2',
  position=(20, -1.9, 0),
  scale=(1.5, 2, 0)
)
goal_0=Entity(
  model='quad',
  texture='stuff\goal',
  position=(20, -3, 1),
  scale=(0.4, 0.8, 0),
)
#fiel goal with collider
goal_1b=Entity(
  model='quad',
  texture='stuff\goal_1b',
  position=(20, -3.2, 2),
  scale=(0.3, 0.5, 0),
  collider='box'
)
goal1=[]
goal1b=[]
goal2=[]
goal0=[]

def newGoal():
  '''Duplicates field goals as obstacles'''
  r_num=r.randint(0,5)
  new1=duplicate(goal_1, 
                  x=20 + r_num)
  new1b=duplicate(goal_1b,
                  x=20.298 + r_num)
  new2=duplicate(goal_2,
                  x=20 + r_num)
  new0=duplicate(goal_0,
                  x=20.3 + r_num)

  goal1.append(new1)
  goal2.append(new2)
  goal0.append(new0)
  goal1b.append(new1b)

  invoke(newGoal, delay=2)
newGoal()

bevo=Entity(
      model='quad',
      texture='stuff\\bevo',
      position=(20, -3, 2),
      scale=(1.4, .8, 0),
    )
bevo_hit=Entity(
      model='quad',
      texture='stuff\\bevo',
      position=(20, -3, 2),
      scale=(.6, .5, 0),
      collider='box',
      visible=False
    )
bevo_1 = []
bevo_hits = []
def Bevo():
    '''Duplicates Entity Bevo
    and creates a hit entity for collision detection
    
    Also makes sure that the entity Bevo, doesn't
    duplicate at the same x-coordinates as the goal entity'''
    new = duplicate(bevo, x=33)
    new1=duplicate(bevo_hit, x=33)
    bevo_1.append(new)
    bevo_hits.append(new1)
    bevo_x = new.x  # Get the X coordinate of the newly created Bevo
    bevo_hitx = new1.x
    goal_x_coords = [g.x for g in goal1] + [g.x for g in goal1b] + [g.x for g in goal2] + [g.x for g in goal0]
    # Combine all x coordinates from goals into a single list

    while bevo_x in goal_x_coords:  # Check if Bevo's X coordinate matches any goal's X coordinate
      new.x += 3
      new1.x += 3  # If there's a match, increment Bevo's X coordinate by 3 units
      bevo_x = new.x
      bevo_hitx = new1.x  # Update the Bevo's X coordinate

    bevo_1[-1].x = new.x
    bevo_hits[-1].x = new1.x  # Assign the updated X coordinate to the Bevo entity
    invoke(Bevo, delay=2)
Bevo()

# points text
label=Text(
  text=(f'Points: {0}'),
  color=color.rgb(128,0,0),
  font='stuff\Minecraft.ttf',
  position=(.6, 0.45),
  scale=(2, 1.5, 0)
)

# beep sfx
sound=Audio(
  'stuff\\beep',
  autoplay=False
)

# pauses game if key 'p' is pressed
pause_handler=Entity(ignore_paused=True)
def pause_handler_input(key):
  if key == 'p':
    application.paused= not application.paused
    exit.enabled = True
pause_handler.input=pause_handler_input

has_jumped = False  

def input(key):
  global has_jumped
  if not has_jumped:  # Check if the player hasn't already jumped
    if key == 'space':
      if reveille.y < -2.3:
          sound.play()
          reveille.animate_y(
              -1,
              duration=0.3,
              curve=curve.out_sine
          )
          reveille.animate_y(
              -3,
              duration=0.3,
              delay=0.3,
              curve=curve.in_sine
          )
          has_jumped = True  # Set the flag to indicate the player has jumped

# Reset the has_jumped flag when the player lands on the ground
    has_jumped = False

# Camera fov
camera.orthographic=True
camera.fov=9

def start_game():
    '''Function that hides the main menu buttons when the play button is clicked'''
    app.paused = False 
    background.enabled = False
    highscore.enabled = False
    play.enabled = False
    instruction.enabled = False
    exit.enabled = False
    label.enabled = True
    application.paused = False

# '''Menu commands'''
play = Button(
    text = 'PLAY',
    color=color.green,
    text_color = color.rgb(128,0,0),
    position = (-.05,.02),
    scale = (.30,.15),
    z=2,
    on_click=start_game  # Set the function to be called when the button is clicked
)
play.text_entity.font = 'stuff\Minecraft.ttf'
play.text_entity.scale = 13,18

def instruct_clicked():
  '''Hides the main menu button when
  the instruction button is clicked'''
  background.texture = 'stuff\\menu_back.png'  # Change to the path of your new image
  highscore.enabled = False
  play.enabled = False
  instruction.enabled = False
  exit.enabled = False
  back_button.enabled = True


#Game Over text
game_over = Text(text="GAME OVER",
              position=(-.5,.3,0),
              color=color.rgb(128,0,0),
              font='stuff\Minecraft.ttf',
              scale=(5,7),
              enabled = False
              )

txt = Text('')
def on_instruct_click():
  '''Shows the instructions texts after instructions button is clicked'''
  instruct_clicked()
  global txt, credits
  txt = Text(text="It's the day of the big T.U. game, and Rev needs your help to run across the field!\nCan you help her score some field goals for the Aggies and avoid Bevo?\n\n\nControl:\n\nSpace = Jump",
              position=(-.5,.25,0),
              color=color.rgb(128,0,0),
              font='stuff\Minecraft.ttf'
              )
  credits = Text(text="Created by:\nHarry Oclarit\nDavid Lloyd\nAustin Thames",
                position=(-.77,-.20,0),
                color=color.rgb(128,0,0),
                font='stuff\Minecraft.ttf'
                )

instruction = Button(
  text = (f'INSTRUCTIONS'),
  color = color.rgb(128,0,0),
  font ='stuff\Minecraft.ttf',
  position = (-0.37,-0.18),
  scale = (.8, .08),
  z=2,
  collider='box',
  on_click=on_instruct_click,
)
instruction.text_entity.font = 'stuff\Minecraft.ttf'
instruction.text_entity.scale = 5,27

def go_back():
    '''Shows the main menu buttons when back button is clicked'''
    background.texture = 'stuff\menu.png'
    highscore.enabled = True
    play.enabled = True
    instruction.enabled = True
    exit.enabled = True
    back_button.enabled = False
    scores.enabled = False
    highscoretxt.enabled = False
    txt.enabled = False
    credits.enabled = False

def on_exit_click():
  '''Exits the application when the exit buttons is clicked'''
  application.quit()

exit = Button(
  text = (f'EXIT'),
  color = color.rgb(128,0,0),
  font ='stuff\Minecraft.ttf',
  position = (-0.62,-0.38),
  scale = (.3, .08),
  z=2,
  collider='box',
  on_click=on_exit_click,
)
exit.text_entity.font = 'stuff\Minecraft.ttf'
exit.text_entity.scale = 15,27

def on_click():
    '''Calls the function: scores_clicked'''
    scores_clicked()

def on_back_click():
    '''Calls the function: go_back'''
    go_back()

highscore = Button(
    text = (f'SCORES'),
    color = color.rgb(128, 0, 0),
    font ='stuff\Minecraft.ttf',
    position = (-0.52, -0.28),
    scale = (.5, .08),
    z=2,
    collider='box',
    on_click=on_click,
)
highscore.text_entity.font = 'stuff\Minecraft.ttf'
highscore.text_entity.scale = 9,27

def scores_clicked():
    '''Hides the main menu buttons and shows 
    the high scores when the scores button is clicked'''
    background.texture = 'stuff\\menu_back.png'
    highscore.enabled = False
    play.enabled = False
    instruction.enabled = False
    exit.enabled = False
    back_button.enabled = True
    scores.enabled = True
    highscoretxt.enabled = True

#Read highscore.txt to display recent scores
with open('Reveille_Run\\stuff\\highscore.txt', 'r') as highscore_file:
  highscore_list = highscore_file.readlines()
  try:
    for i in range(len(highscore_list)):
      highscore_list[i] = int(highscore_list[i][0:-1])
  except:
    pass
highscore_list.sort()
if len(highscore_list) >= 15:
  hs_text = list(range(15))
  for i in range(15):
      hs_text[i] = str(highscore_list[-i - 1])
elif len(highscore_list) < 15:
    hs_text = list(range(len(highscore_list)))
    for i in range(len(highscore_list)):
        hs_text[i] = str(highscore_list[-i - 1])
hs_string = ''
for j in range(len(hs_text)):
    hs_string += hs_text[j] + '\n'


scores = Text(
    text=hs_string,
    color = color.rgb(128,0,0),
    font='stuff\Minecraft.ttf',
    position=(-0.05,0.3),
    scale=(2,2),
    enabled=False
)
highscoretxt = Text(
    text='HIGH SCORES',
    color = color.rgb(128,0,0),
    font='stuff\Minecraft.ttf',
    position=(-0.35,0.4),
    scale=(4,4),
    enabled=False,
)

back_button = Button(
    text="Back",
    color=color.rgb(128, 0, 0),  # Green color, adjust as needed
    font='stuff\Minecraft.ttf',
    position=(-0.62,-0.38),  # Adjust position as needed
    scale=(.3, .08),
    z=2,
    collider='box',
    on_click=on_back_click,
    enabled= False
)
back_button.text_entity.font = 'stuff\Minecraft.ttf'
back_button.text_entity.scale = 15,27

# By default, game is paused while user is in main menu
application.paused = True 
label.enabled = False #Points is not shown while game not playing

points=0
post_speed = 5.049
b_speed=.072

def update():
  if not app.paused:
    '''Update function while game is running,
    loops subtracts x values from the 
    backgrounds and obstacles. Excluding reveille entity'''
  #POINTS
    global points
    points += 1
    label.text=f'{points}'
    #MAIN BACKGROUND, offset
    global offset_ground, post_speed, offset_sky, b_speed, bevo_spawned
    game_speed = b_speed
    offset_ground+=time.dt*game_speed
    setattr(ground1, 'texture_offset', (offset_ground, 0))
    #SKY, offset
    offset_sky+=time.dt*.01
    setattr(sky, 'texture_offset', (offset_sky, 0))
    #GOAL POST, x-value subtraction
    goal_speed = post_speed
    for g in goal1:
        g.x -= goal_speed*time.dt
    for g in goal1b:
        g.x -= goal_speed*time.dt
    for g in goal2:
        g.x -= goal_speed*time.dt
    for g in goal0:
        g.x -= goal_speed*time.dt
    #BEVO, x-value subtraction
    if points > 5600:
      for b in bevo_1:
        b.x -= goal_speed*time.dt
      for b in bevo_hits:
        b.x -= goal_speed*time.dt
    #BACKGROUND ENTITIES
    for w in watertower:
      w.x -= 1.5*time.dt
    for p in planes:
      p.x -= 0.5*time.dt
    for a in academics:
      a.x -= 1.5*time.dt
    for z in zachs:
      z.x -= 1.5*time.dt
    #Speeds up the game
    if points % 2500 == 0:
      b_speed += .03
      post_speed += 2.095
    #If collision happens, the following code will run
    if reveille.intersects().hit:
      reveille.texture='stuff\\reveille_1'
      application.pause() #Pauses the game 
      with open('Reveille_Run\\stuff\\highscore.txt', 'a') as high_score: #Adds score to 'highscore.txt' 
        high_score.write(str(points) + '\n')
      Audio(
      'stuff\\warhymn',
      autoplay=True,
      )
      exit.enabled = True
      game_over.enabled = True
    pass

app.run()

