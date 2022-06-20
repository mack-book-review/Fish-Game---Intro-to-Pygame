import pygame,sys
from pygame.locals import * 
import random 
from fish import Fish 

pygame.init()
size =  (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255,255,255)
WATER_BLUE = (125, 225, 232)
BLUE = (0,0,255)
RED = (255,0,0)

fishes = []

# fish_image = pygame.image.load("fish.png")
# fish_image = pygame.transform.smoothscale(fish_image,(50,80))
# fish_rect = fish_image.get_rect()
# fish_rect.center = (width//2,height//2)

# speed = pygame.math.Vector2(0,10)
# rotation = random.randint(0,360)
# speed.rotate_ip(rotation)
# fish_image = pygame.transform.rotate(fish_image,180-rotation)


# def move_fish():
#   global fish_image,fish_rect
#   fish_rect.move_ip(speed)
#   screen_info = pygame.display.Info()
#   current_w = screen_info.current_w
#   current_h = screen_info.current_h
  
#   if fish_rect.left < 0 or fish_rect.right > current_w:
#     speed[0] *= -1 
#     fish_image = pygame.transform.flip(fish_image,True,False)
#     fish_rect.move_ip(speed[0],0);
  
#   if fish_rect.top < 0 or fish_rect.bottom > current_h:
#     speed[1] *= -1 
#     fish_image = pygame.transform.flip(fish_image,False,True)
#     fish_rect.move_ip(0,speed[1]);
  
def main():
  for i in range(10):
    new_fish = Fish(random.randint(0,width),random.randint(0,height))
    fishes.append(new_fish)
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        x,y = event.pos
        fishes.append(Fish(x,y))
      if event.type == KEYDOWN:
        if event.key == K_d:
          for i in range(len(fishes)//2):
            fishes.pop(0)
        
    for fish in fishes:
      fish.update()
    screen.fill(WATER_BLUE)
    for fish in fishes:
      fish.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
  main()