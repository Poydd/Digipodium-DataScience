from random import randint
import pgzrun

class player(Actor):
    speed = 5
    if keyboard.left:
            self.x -=self.speed
    if keyboard.right:
            self.x +=self.speed
    if keyboard.up:
            self.y -=self.speed
    if keyboard.down:
            self.y +=self.speed
        if keyboard.space:
            self.angle +=self.speed

class enemy(Actor):
    speed = 2
    pos = (-100, HEIGHT/2)
    def enemy_tracking(self):
     if p.x > self.x:
      self.x += self.speed
     if p.x < self.x:
      self.x -= self.speed
     if p.y > self.y:
      self.y += self.speed
     if p.y < self.y:
      self.y -= self.speed
     print(f'player{p.pos} enemy{e.pos}')
     if self.colliderect(p):
         exit()

class friut(Actor):

    x = randint(50,WIDTH-50)
    y = randint(50,HEIGHT-50)
    def relocate(self):
        self.x = randint(50,WIDTH-50)
        self.y = randint(50,HEIGHT-50)
    