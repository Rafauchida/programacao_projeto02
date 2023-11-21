import pygame
from time import sleep


def draw_text(window, text, font, x, y, text_col=(0,0,0)):
  img = font.render(text, True, text_col)
  window.blit(img, (x, y))


def game():
  pygame.init()

  res_x = 800
  res_y = 533

  fundo = pygame.image.load("background.png")
  cassino1 = pygame.image.load("cassino.png")
  cassino2 = pygame.image.load("close_cassino.png")


  window = pygame.display.set_mode((res_x, res_y))
  pygame.display.set_caption("Caça-níquel")

  play = True
  while play:
    for i in range(40):  
      pygame.time.delay(50)
        
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          play = False

      window.blit(cassino1, (0, 0))
      # window.blit(fundo, (0, 0))
      # window.blit(cassino1, (((res_x/2) - 119), (res_y - 350)))

      pygame.display.update()


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        play = False
    window.blit(cassino2, (0, 0))
    # window.blit(fundo, (0, 0))
    # window.blit(cassino2, (((res_x/2) - 119), (res_y - 350)))
    pygame.display.update()
    sleep(2)
    play = False

  pygame.quit()
    




def ranking(first, second, third):
  pygame.init()

  res_x = 800
  res_y = 533


  fundo = pygame.image.load("background.png")
  placar = pygame.image.load("ranking2.png")

  window = pygame.display.set_mode((res_x, res_y))
  pygame.display.set_caption("Ranking")

  font = pygame.font.SysFont("Arial", 40)

  play = True
  while play:
    pygame.time.delay(50)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        play = False

    window.blit(fundo, (0, 0))
    window.blit(placar, (((res_x/2)-230), 263))
    draw_text(window, second, font, ((res_x/2)-195), ((res_y/2)+20), (0, 0, 0))
    draw_text(window, first, font, ((res_x/2)-65), res_y/2-50)
    draw_text(window, third, font, ((res_x/2)+90), (res_y/2)+70)
    pygame.display.update()

  pygame.quit()