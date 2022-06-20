import random, pygame 

class Fish:

  def __init__(self,x,y):
    self.image = pygame.image.load("fish.png") 
    scale = random.randint(1,5)*10
    self.image = pygame.transform.smoothscale(self.image,(scale,scale))
    rotation = random.randint(0,360)


    self.rect = self.image.get_rect()
    self.speed = pygame.math.Vector2(0,random.randint(2,5))
    self.rect.center = x,y

    self.speed.rotate_ip(rotation)
    self.image = pygame.transform.rotate(self.image,180-rotation)

    
  def update(self):
    global fish_image,fish_rect
    self.rect.move_ip(self.speed)
    
    screen_info = pygame.display.Info()
    current_w = screen_info.current_w
    current_h = screen_info.current_h
    
    if self.rect.left < 0 or self.rect.right > current_w:
      self.speed[0] *= -1 
      self.image = pygame.transform.flip(self.image,True,False)
      self.rect.move_ip(self.speed[0],0);
    
    if self.rect.top < 0 or self.rect.bottom > current_h:
      self.speed[1] *= -1 
      self.image = pygame.transform.flip(self.image,False,True)
      self.rect.move_ip(0,self.speed[1]);


  def draw(self,screen):
    screen.blit(self.image,self.rect)

