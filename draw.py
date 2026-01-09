import pygame,json
from settings import Settings
from utilities.resource_manager import ResourceManager
class DrawRoom:

  def __init__(self,escape):
    self.screen = escape.screen
    self.data_source = ResourceManager()
    self.objects = self.data_source.get_object_data("data/objects.json")
    self._update_center_postion()
    
  def _update_center_postion(self):
    self.center_y = self.screen.get_height()//2 
    self.center_x = self.screen.get_width()//2 
    
  def draw(self,room_id,map_manager):
    room_map,room_height,room_width = map_manager.get_room_map(room_id)
    my_rect = pygame.Rect(Settings.BODY_TOPLEFT,Settings.BODY_SIZE)
    pygame.draw.rect(self.screen,Settings.RED,my_rect)
    start_x = self.center_x-room_width//2
    start_y = self.center_y-room_height//2
    for y in range(room_height):
      for x in range(room_width):
        item = room_map[y][x]
        if item != 255:
          image = self.objects[item][0]
          self.screen.blit(image,(start_x+x*30,start_y+y*30-image.get_height()))
          pass
