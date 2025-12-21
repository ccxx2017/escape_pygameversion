import json
import pygame

class DataLoader:
  
  @staticmethod
  def load_json(path):
    with open(path,"r") as f:
      data = json.load(f)# 反序列化
      return data
    
  def get_game_map_data(self,path):
    map_data = DataLoader.load_json(path)
    return map_data
  
  def get_secenary_data(self,path):
    secenary_data = DataLoader.load_json(path)
    return secenary_data
  
  def get_object_data(self,path):
    object_data = DataLoader.load_json(path)
    processed = self._process_objects(object_data)
    return processed
  
  def _process_objects(self,objects):
    processed_objects = {int(key):item for key,item in objects.items()}
    processed = {}
    for k,v in processed_objects.items():
        v1 = pygame.image.load(v[0])
        v2 = pygame.image.load(v[1]) if v[1] is not None else None
        v3 = v[2]
        v4 = v[3] if len(v)==4 else None
        processed[k] = [v1,v2,v3,v4]
    return processed