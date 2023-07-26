import pgzrun
from random import randint

# screen size
WIDTH = 1000
HEIGHT = 500

# objects
p = Actor('hero')                                 # actor is class
e = Actor('enemy')
c = Actor('friut')

# configs
c.x = randint(50, WIDTH-50)
c.y = randint(50, HEIGHT-50)
p.POS = (WIDTH/2, HEIGHT/2)
e.pos = (-100, HEIGHT/2)
ps = 5
es = 2
score = 0

# player control
def player_control():
  if keyboard.left:
    p.x -=ps
  if keyboard.right:
            p.x +=ps
  if keyboard.up:
            p.y -=ps
        if keyboard.down:
            p.y +=ps
        if keyboard.space:
            p.angle +=ps

  randint(50,WIDTH-50)
  y = randint(50,HEIGHT-50)
def enemy_tracking():
  if p.x > e.x:
    e.x += 1
  if p.x < e.x:
    e.x -= 1
  if p.y > e.y:
    e.y += 1
  if p.y < e.y:
    e.y -= 1
def friut_eating():
  if p.colliderect(c):
    c.x = randint(50,WIDTH-50)
    c.y = randint(50,HEIGHT-50)
    score += 10
    sounds.clap.play()

# drawing on screen
def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'score: {score}',(10,10),color='white')

def update(dt):
   player_control()
   enemy_tracking()
   friut_eating()


# game loop
pgzrun.go()