import pygame,json
from settings import Settings
from utilities.resource_manager import ResourceManager
class DrawRoom:

  def __init__(self,escape):
    self.escape = escape
    self.res = ResourceManager()
    self.current_room_cached = None
    # self.generate_map(escape.current_room)
    
  def generate_map(self,room_id):
   
    room = room_id
    self.my_game_map_data = self.res.get_map_data("data/game_map_data.json")
    self.room_height = self.my_game_map_data[room][1]
    self.room_width = self.my_game_map_data[room][2]
    self.topleft_y = self.escape.screen.get_height()//2 - self.room_height//2*30
    self.topleft_x = self.escape.screen.get_width()//2 - self.room_width//2*30
    room_data = self.my_game_map_data[room]
    self.room_height = room_data[1]
    self.room_width  = room_data[2]
    floor_type = self.get_floor_type(room)
    if room in list(range(1,21)):

      side_edge = 2
      bottom_edge = 2
    elif room in list(range(21,26)):
      side_edge = 2
      bottom_edge = 1
    else:
      side_edge = 1
      bottom_edge = 1

    self.room_map = [[side_edge]*self.room_width]
    for i in range(self.room_height-2):
      self.room_map += [[side_edge]+[floor_type]*(self.room_width-2)+[side_edge]]

    self.room_map += [[bottom_edge]*self.room_width]
    middle_colum = self.room_width//2
    middle_row = self.room_height//2
    if room_data[3]:#表示顶部有出口
      self.room_map[0][middle_colum] = floor_type
      self.room_map[0][middle_colum-1] = floor_type
      self.room_map[0][middle_colum+1] = floor_type
    
    if room_data[4]:#右侧有出口
      self.room_map[middle_row][self.room_width-1] = floor_type
      self.room_map[middle_row+1][self.room_width-1] = floor_type
      self.room_map[middle_row-1][self.room_width-1] = floor_type

    if room%5 != 1:
      left_room = room - 1
      if self.my_game_map_data[left_room][4]:
        self.room_map[middle_row][0] = floor_type
        self.room_map[middle_row+1][0] = floor_type
        self.room_map[middle_row-1][0] = floor_type

    if room < 45:
      room_below = room + 5
      if self.my_game_map_data[room_below][3]:
        self.room_map[self.room_height-1][middle_colum] = floor_type
        self.room_map[self.room_height-1][middle_colum-1] = floor_type
        self.room_map[self.room_height-1][middle_colum+1] = floor_type

    self.secenary = self.res.get_scenery_data("data/secenary.json")
    self.objects = self.res.get_object_assets("data/objects.json")
    if room in self.secenary:
      for secenary_item in self.secenary[room]:
        item = secenary_item[0]
        item_y = secenary_item[1]
        item_x = secenary_item[2]
        self.room_map[item_y][item_x] = item
        image_here = self.objects[item][0]
        image_width_in_tiles = image_here.get_width()/Settings.TILE_SIZE
        for tile_num in range(1,int(image_width_in_tiles)):
          self.room_map[item_y][item_x+tile_num] = 255


  def get_floor_type(self,room):
    if room in list(range(1,26)):
      return 2
    else:
      return 0

  def draw(self):
    room = self.escape.current_room
    my_rect = pygame.Rect(Settings.BODY_TOPLEFT,Settings.BODY_SIZE)
    pygame.draw.rect(self.escape.screen,Settings.RED,my_rect)
    if room != self.current_room_cached:
      self.generate_map(room)
      self.current_room_cached = room
    
    for y in range(self.room_height):
      for x in range(self.room_width):
        item = self.room_map[y][x]
        if item != 255:
          image = self.objects[item][0]
          self.escape.screen.blit(image,(self.topleft_x+x*30,self.topleft_y+y*30-image.get_height()))
          pass
