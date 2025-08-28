import pygame

print('Sutup start')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('Setup end')

print('Start loop')
while True:
    #checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#fechando janela
            quit()#fechando o pygame