import pygame

def ranking(first, second, third):
  pygame.init()

  res_x = 800
  res_y = 533

  fundo = pygame.image.load("background.png")
  placar = pygame.image.load("ranking2.png")

  window = pygame.display.set_mode((res_x, res_y))
  pygame.display.set_caption("Ranking")

  font = pygame.font.SysFont("Arial", 40)
  def draw_text(text, font, x, y, text_col=(0,0,0)):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

  play = True
  while play:
    pygame.time.delay(50)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        play = False
        pygame.quit()

    window.blit(fundo, (0,0))
    window.blit(placar, (((res_x/2)-230), 263))
    draw_text(second, font, ((res_x/2)-170), ((res_y/2)+20), (0, 0, 0))
    draw_text(first, font, ((res_x/2)-45), res_y/2-50)
    draw_text(third, font, ((res_x/2)+90), (res_y/2)+70)
    pygame.display.update()

  pygame.quit()