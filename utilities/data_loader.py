import json
import pygame

class DataLoader:
  
  """纯粹的加载器：只负责从磁盘读取并转换格式，不维护缓存"""

  @staticmethod
  def load_json(path):
    with open(path,"r") as f:
      data = json.load(f)# 反序列化
      return data
    
  @staticmethod
  def load_image(path):
    return pygame.image.load(path)
  
  def get_processed_scenery(self,path):
    data = self.load_json(path)
    return {int(k):v for k,v in data.items()}
  
  def get_raw_object_data(self,path):
    return self.load_json(path)
    
  # def get_game_map_data(self,path):
  #   if self._game_map_data is None:
  #     self._game_map_data = DataLoader.load_json(path)
  #   return self._game_map_data
  
  # def get_secenary_data(self,path):
  #   if self._secenary_data is None:
  #     self._secenary_data = DataLoader.load_json(path)
  #   processed = {int(k):v for k,v in self._secenary_data.items()}
  #   return processed
  
  # def get_object_data(self,path):
  #   if self._objects is None:
  #     self._objects = DataLoader.load_json(path)
  #   processed = self._process_objects(self._objects)
  #   return processed
  
  # def _process_objects(self,objects):
  #   processed_objects = {int(key):item for key,item in objects.items()}
  #   processed = {}
  #   for k,v in processed_objects.items():
  #       v1 = pygame.image.load(v[0])
  #       v2 = pygame.image.load(v[1]) if v[1] is not None else None
  #       v3 = v[2]
  #       v4 = v[3] if len(v)==4 else None
  #       processed[k] = [v1,v2,v3,v4]
  #   return processed