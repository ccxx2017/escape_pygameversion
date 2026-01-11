import pygame
from .data_loader import DataLoader
from dataclasses import dataclass
from typing import Optional

@dataclass
class GameObject:
  image:pygame.Surface
  alt_image:Optional[pygame.Surface]
  name:str 
  description:str

class ResourceManager:
  def __init__(self):
    self.loader = DataLoader()
    self._data_cache = {}
    self._image_cache = {}

  def get_game_map_data(self,path):
    if path not in self._data_cache :
      self._data_cache[path] = self.loader.load_json(path)
    return self._data_cache[path]
  
  def get_secenary_data(self,path):
    if path not in self._data_cache:
      secenary_data = self.loader.load_json(path)
      self._data_cache[path] = {int(k):v for k,v in secenary_data.items()}
    return self._data_cache[path]
  
  def get_object_data(self,path):
    if path not in self._data_cache:
      object_data = self.loader.load_json(path)
      self._data_cache[path] = self._process_objects(object_data)
    
    return self._data_cache[path]
  

  def _process_objects(self,objects):
    processed_objects = {int(key):item for key,item in objects.items()}
    processed = {}
    for k,v in processed_objects.items():
        # v1 = pygame.image.load(v[0])
        v1 = self._get_cached_image(v[0])
        v2 = self._get_cached_image(v[1]) if v[1] is not None else None
        v3 = v[2]
        v4 = v[3] if len(v)==4 else None
        # processed[k] = [v1,v2,v3,v4]
        processed[k] = GameObject(image=v1,alt_image=v2,name=v3,description=v4)
    return processed
  
  def _get_cached_image(self,img_path):
    if img_path not in self._image_cache:
      self._image_cache[img_path] = self.loader.load_image(img_path)

    return self._image_cache[img_path]
