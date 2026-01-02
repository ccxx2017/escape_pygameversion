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
    
  