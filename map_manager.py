from utilities.resource_manager import ResourceManager
from settings import Settings
from typing import List
from dataclasses import dataclass

# 叠buff
@dataclass#装饰器
class RoomData:
  tiles:List[List[int]]
  height:int
  width:int



class MapManager:
  """生成地图并返回地图数据"""
  def __init__(self,screen):
    self.screen = screen
    self.room_data = None
    self.room_cached = None
    self.data_source = ResourceManager()

  def get_room_map(self,room_id):
    if self.room_cached != room_id:
      self.room_data = self.generate_map(room_id)
      self.room_cached = room_id
    return self.room_data
  
  def generate_map(self,room_id):
    map_data = self.data_source.get_game_map_data("data/game_map_data.json")
    room_height = map_data[room_id][1]
    room_width = map_data[room_id][2]
    room_data = map_data[room_id]
    room_height = room_data[1]
    room_width  = room_data[2]
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

    room_map = [[side_edge]*room_width]
    for i in range(room_height-2):
      room_map += [[side_edge]+[floor_type]*(room_width-2)+[side_edge]]

    room_map += [[bottom_edge]*room_width]
    middle_colum = room_width//2
    middle_row = room_height//2
    if room_data[3]:#表示顶部有出口
      room_map[0][middle_colum] = floor_type
      room_map[0][middle_colum-1] = floor_type
      room_map[0][middle_colum+1] = floor_type
    
    if room_data[4]:#右侧有出口
      room_map[middle_row][room_width-1] = floor_type
      room_map[middle_row+1][room_width-1] = floor_type
      room_map[middle_row-1][room_width-1] = floor_type

    if room_id%5 != 1:
      left_room = room_id - 1
      if map_data[left_room][4]:
        room_map[middle_row][0] = floor_type
        room_map[middle_row+1][0] = floor_type
        room_map[middle_row-1][0] = floor_type

    if room_id < 45:
      room_below = room_id + 5
      if map_data[room_below][3]:
        room_map[room_height-1][middle_colum] = floor_type
        room_map[room_height-1][middle_colum-1] = floor_type
        room_map[room_height-1][middle_colum+1] = floor_type

    self.secenary = self.data_source.get_secenary_data("data/secenary.json")
    self.objects = self.data_source.get_object_data("data/objects.json")
    if room_id in self.secenary:
      for secenary_item in self.secenary[room_id]:
        item = secenary_item[0]
        item_y = secenary_item[1]
        item_x = secenary_item[2]
        room_map[item_y][item_x] = item
        image_here = self.objects[item].image
        image_width_in_tiles = image_here.get_width()/Settings.TILE_SIZE
        for tile_num in range(1,int(image_width_in_tiles)):
          room_map[item_y][item_x+tile_num] = 255

    return RoomData(
      tiles=room_map,
      height=room_height,
      width=room_width
    )


  def get_floor_type(self,room_id):
    room_id = room_id + 1
    if room_id in list(range(1,26)):
      return 2
    else:
      return 0 