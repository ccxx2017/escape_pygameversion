from .data_loader import DataLoader
class ResourceManager:
  def __init__(self):
    self.loader = DataLoader()
    self._data_cache = {}
    self._image_cache = {}
  
  def get_map_data(self,path):
    """获取地图数据（带缓存）"""
    if path not in self._data_cache:
      self._data_cache[path] = self.loader.load_json(path)
    return self._data_cache[path]
  
  def get_scenery_data(self,path):
    """获取装饰物数据（带缓存）"""
    if path not in self._data_cache:
      self._data_cache[path] = self.loader.get_processed_scenery(path)
    return self._data_cache[path]
  
  def get_object_assets(self, path):
        """
        核心进阶：不仅缓存原始数据，还缓存处理后的 Pygame Image 对象。
        避免了每次调用都重新执行 pygame.image.load
        """
        cache_key = f"obj_assets_{path}"
        
        if cache_key not in self._data_cache:
            raw_data = self.loader.get_raw_object_data(path)
            processed = {}
            
            # 将原来的 _process_objects 逻辑移到这里，并增加图像缓存
            for k, v in raw_data.items():
                obj_id = int(k)
                # v[0] 是路径, v[1] 是另一个路径...
                img1 = self._get_cached_image(v[0])
                img2 = self._get_cached_image(v[1]) if v[1] else None
                
                processed[obj_id] = [img1, img2, v[2], v[3] if len(v)==4 else None]
            
            self._data_cache[cache_key] = processed
            
        return self._data_cache[cache_key]

  def _get_cached_image(self, img_path):
      """内部私有方法：确保同一张图片在内存中只有一份"""
      if img_path not in self._image_cache:
          print(f"--- 真正从硬盘加载图片: {img_path} ---")
          self._image_cache[img_path] = self.loader.load_image(img_path)
      return self._image_cache[img_path]
