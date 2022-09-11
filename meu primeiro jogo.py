import pygame
pygame.init()

#variavel fundo
fundo = pygame.image.load('pacman.png')

#variaveis da posição
x = 400
y = 300
velocidade = 10

#criando a janela que vai aparecer com o tamanho dela e o nome em cima
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sword art Online')

#mantendo ela aberta e sem que atualize tão rapido
janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            janela_aberta = False

#criando os comandos
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
       y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade

    janela.blit(fundo, (0,0))


#criando objeto que será movido
    pygame.draw.circle(janela, (244, 255, 0), (x, y),40)
    pygame.display.update()




pygame.quit()
