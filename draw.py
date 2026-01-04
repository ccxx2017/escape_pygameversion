import pygame,json
from settings import Settings
from utilities.resource_manager import ResourceManager
class DrawRoom:

  def __init__(self,escape):
    self.screen = escape.screen
    # self.data_source = ResourceManager()
    
    
  def draw(self,room_id,map_manager):
    room_map,room_height,room_width = map_manager.get_room_map(room_id)
    my_rect = pygame.Rect(Settings.BODY_TOPLEFT,Settings.BODY_SIZE)
    pygame.draw.rect(self.screen,Settings.RED,my_rect)
  
    for y in range(room_height):
      for x in range(room_width):
        item = room_map[y][x]
        if item != 255:
          image = self.objects[item][0]
          self.screen.blit(image,(self.topleft_x+x*30,self.topleft_y+y*30-image.get_height()))
          pass
