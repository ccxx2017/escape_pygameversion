import pygame,json
from settings import Settings

class DrawRoom:

  def __init__(self,screen,resource_manager):
    self.screen = screen
    self.res = resource_manager
    # 只保留资源引用，不保留游戏逻辑状态
    self.objects = self.res.get_object_assets("data/objects.json")
    
  def draw(self,room_id,map_manager):
    room_map, room_height, room_width = map_manager.get_map_grid(room_id)
    tile_size = 30
    topleft_x = self.screen.get_width() // 2 - (room_width * tile_size) // 2
    topleft_y = self.screen.get_height() // 2 - (room_height * tile_size) // 2
    my_rect = pygame.Rect(Settings.BODY_TOPLEFT,Settings.BODY_SIZE)
    pygame.draw.rect(self.escape.screen,Settings.RED,my_rect)
    
    for y in range(room_height):
      for x in range(room_width):
        item = room_map[y][x]
        if item != 255:
          image = self.objects[item][0]
          self.escape.screen.blit(image,(topleft_x+x*30,topleft_y+y*30-image.get_height()))
          pass
