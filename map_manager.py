# 文件名: map_manager.py
class MapManager:
    def __init__(self, resource_manager):
        self.res = resource_manager
        # ... 加载配置 ...
        self._cache = {} # 可以做简单的缓存，避免重复计算

    def get_map(self, room_id):
        # 如果缓存里有，直接给；没有则计算
        if room_id not in self._cache:
            self._cache[room_id] = self._generate_map(room_id)
        return self._cache[room_id]

    def _generate_map(self, room_id):
      room = room_id
      my_game_map_data = self.res.get_map_data("data/game_map_data.json")
      self.topleft_y = self.escape.screen.get_height()//2 - self.room_height//2*30
      self.topleft_x = self.escape.screen.get_width()//2 - self.room_width//2*30
      room_data = my_game_map_data[room]
      room_height = room_data[1]
      room_width  = room_data[2]
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

      room_map = [[side_edge]*room_width]
      for i in range(room_height-2):
        room_map += [[side_edge]+[floor_type]*(self.room_width-2)+[side_edge]]

      room_map += [[bottom_edge]*self.room_width]
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

      if room%5 != 1:
        left_room = room - 1
        if my_game_map_data[left_room][4]:
          room_map[middle_row][0] = floor_type
          room_map[middle_row+1][0] = floor_type
          room_map[middle_row-1][0] = floor_type

      if room < 45:
        room_below = room + 5
        if my_game_map_data[room_below][3]:
          room_map[self.room_h-1][middle_colum] = floor_type
          room_map[self.room_h-1][middle_colum-1] = floor_type
          room_map[self.room_h-1][middle_colum+1] = floor_type

      self.secenary = self.res.get_scenery_data("data/secenary.json")
      self.objects = self.res.get_object_assets("data/objects.json")

      if room in self.secenary:
        for secenary_item in self.secenary[room]:
          item = secenary_item[0]
          item_y = secenary_item[1]
          item_x = secenary_item[2]
          room_map[item_y][item_x] = item
          image_here = self.objects[item][0]
          image_width_in_tiles = image_here.get_width()/Settings.TILE_SIZE
          for tile_num in range(1,int(image_width_in_tiles)):
            room_map[item_y][item_x+tile_num] = 255

      return room_map, room_height, room_width

    def get_floor_type(self,room):
      if room in list(range(1,26)):
        return 2
      else:
        return 0
          