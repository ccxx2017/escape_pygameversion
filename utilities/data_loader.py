import json
import pygame

class DataLoader:
  

  @staticmethod
  def load_json(path):
    with open(path,"r") as f:
      data = json.load(f)# 反序列化
      return data
    
  @staticmethod
  def load_image(path):
    return pygame.image.load(path)
    
  