import pygame
from settings import Settings
from draw import DrawRoom

class Escape:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode(Settings.WINDOW_SIZE)
    self.running = True
    self.current_room = Settings.START_ROOM
    self.draw_room = DrawRoom(self)

  def _handle_event(self,event):
    if event.type == pygame.QUIT:
        self.running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        
        if event.button == 1:
          self.current_room += 1

  def _update_screen(self):
    #  self.screen.fill(Settings.BLUE)
    self.draw_room.draw()
    pygame.display.flip()

  def print_map(self):
    for y in range(self.draw_room.room_height):
      for x in range(self.draw_room.room_width):
        print(self.draw_room.room_map[y][x],end=" ")
      print()

  def run_game(self):
    while self.running:
      for event in pygame.event.get():
        self._handle_event(event)

      self._update_screen()
      
if __name__ == "__main__":
  
  my_game = Escape()
  # print(f"{my_game.draw_room.secenary=}")
  # my_game.print_map()
  my_game.run_game()