import pygame,json
from settings import Settings
from utilities.data_loader import DataLoader
class DrawRoom:

  def __init__(self,escape):
    self.screen = escape.screen
    self.data_source = DataLoader()
    self.my_game_map_data = None
    self.objects = None
    self.secenary = None
    self.old_room = None
    
  def generate_map(self,room_id):
    self.my_game_map_data = self.data_source.get_game_map_data("data/game_map_data.json")
    self.room_height = self.my_game_map_data[room_id][1]
    self.room_width = self.my_game_map_data[room_id][2]
    self.topleft_y = self.screen.get_height()//2 - self.room_height//2*30
    self.topleft_x = self.screen.get_width()//2 - self.room_width//2*30
    room_data = self.my_game_map_data[room_id]
    self.room_height = room_data[1]
    self.room_width  = room_data[2]
    floor_type = self.get_floor_type(room_id)
    if room_id in list(range(1,21)):

      side_edge = 2
      bottom_edge = 2
    elif room_id in list(range(21,26)):
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

    if room_id%5 != 1:
      left_room = room_id - 1
      if self.my_game_map_data[left_room][4]:
        self.room_map[middle_row][0] = floor_type
        self.room_map[middle_row+1][0] = floor_type
        self.room_map[middle_row-1][0] = floor_type

    if room_id < 45:
      room_below = room_id + 5
      if self.my_game_map_data[room_below][3]:
        self.room_map[self.room_height-1][middle_colum] = floor_type
        self.room_map[self.room_height-1][middle_colum-1] = floor_type
        self.room_map[self.room_height-1][middle_colum+1] = floor_type

    self.secenary = self.data_source.get_secenary_data("data/secenary.json")
    self.objects = self.data_source.get_object_data("data/objects.json")
    if room_id in self.secenary:
      for secenary_item in self.secenary[room_id]:
        item = secenary_item[0]
        item_y = secenary_item[1]
        item_x = secenary_item[2]
        self.room_map[item_y][item_x] = item
        image_here = self.objects[item][0]
        image_width_in_tiles = image_here.get_width()/Settings.TILE_SIZE
        for tile_num in range(1,int(image_width_in_tiles)):
          self.room_map[item_y][item_x+tile_num] = 255


  def get_floor_type(self,room_id):
    room_id = room_id + 1
    if room_id in list(range(1,26)):
      return 2
    else:
      return 0

  def draw(self,room_id):
    my_rect = pygame.Rect(Settings.BODY_TOPLEFT,Settings.BODY_SIZE)
    pygame.draw.rect(self.screen,Settings.RED,my_rect)
    if self.old_room != room_id:
      self.generate_map(room_id)
      self.old_room = room_id
    
    
    for y in range(self.room_height):
      for x in range(self.room_width):
        item = self.room_map[y][x]
        if item != 255:
          image = self.objects[item][0]
          self.screen.blit(image,(self.topleft_x+x*30,self.topleft_y+y*30-image.get_height()))
          pass
