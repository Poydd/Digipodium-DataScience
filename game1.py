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

# drawing on screen
def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'score: {score}',(10,10),color='white')

def update(dt):
   global score
# player control
   if keyboard.left:
     p.x -= 5
   if keyboard.right:
     p.x += 5
   if keyboard.up:
     p.y -= 5
   if keyboard.down:
     p.y += 5
   if keyboard.space:
     p.angle += 5
     


# enemy control player
   if p.x > e.x:
     e.x += 1
   if p.x < e.x:
     e.x -= 1
   if p.y > e.y:
     e.y += 1
   if p.y < e.y:
     e.y -= 1
   print(f'player{p.pos} enemy({e.pos})')

   # fruit collision
   if p.colliderect(c):
     c.x = randint(50,WIDTH-50)
     c.y = randint(50,HEIGHT-50)
     score += 10
     sounds.clap.play()



# game loop
pgzrun.go()