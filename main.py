import pygame, random
from sprite_sheet import SpriteSheet

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #cria janela
screen.set_colorkey((0, 0, 0)) #define transparente
clock = pygame.time.Clock()

#título e ícone
pygame.display.set_caption("Universo Discreto Productions...")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

#fundo
fundo_img = pygame.image.load("fundo.jpg")
nova_largura_fundo, nova_altura_fundo = int(fundo_img.get_width() * 0.25), int(fundo_img.get_height() * 0.25)
fundo_img = pygame.transform.scale(fundo_img, (nova_largura_fundo, nova_altura_fundo))

#boneco do mario
mario_img = pygame.image.load("mario.png")
mario_img = pygame.transform.scale(mario_img, (int(mario_img.get_width() * 0.5), int(mario_img.get_height() * 0.5)))
mario_pos_x = 0
mario_pos_y = 150

#sprite sheet mario
mario_sprite = SpriteSheet("mario_sprite_sheet.png", "sprite_data")
mario_sprite.set_state("PARADO")

#boneco do goomba
goomba_img = pygame.image.load("goomba.png")
goomba_pos_x = WIDTH / 2
goomba_pos_y = 50

#gráfico bola de fogo
bola_fogo_img = pygame.image.load("bolafogo.png")
bola_fogo_img = pygame.transform.scale(bola_fogo_img, (int(bola_fogo_img.get_width() * 0.25), int(bola_fogo_img.get_height() * 0.25)))
bola_fogo_em_movimento = False
bola_fogo_pos_x = mario_pos_x + 160
bola_fogo_pos_y = mario_pos_y
bola_fogo_angle = 0

#game loop
running = True
mario_update_key_x = 0
goomba_update_random_x = 0
goomba_update_random_y = 0
frame_counter = 0

mario_andando = 0
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    #screen.fill((192, 192, 192)) #colorir a tela de cinza
    screen.blit(fundo_img, (0, 0))

    #adicionar o goomba no canvas
    screen.blit(goomba_img, (goomba_pos_x, goomba_pos_y))
    goomba_pos_x += goomba_update_random_x
    goomba_pos_y += goomba_update_random_y
    #a cada 60 frames, o goomba se movimenta pra outra direção
    if frame_counter % 60 == 0:
        goomba_update_random_x = random.uniform(-3.0, 3.0)
        goomba_update_random_y = random.uniform(-3.0, 3.0)
        print("Direção do goomba: (", goomba_update_random_x, goomba_update_random_y, ")")
    #se o goomba sair da tela do lado direito...
    if goomba_pos_x > WIDTH - goomba_img.get_width():
        goomba_pos_x = WIDTH - goomba_img.get_width()
    #se o goomba sair da tela do lado esquerdo...
    if goomba_pos_x < 0:
        goomba_pos_x = 0

    #se o goomba sair da tela por cima...
    if goomba_pos_y > HEIGHT - goomba_img.get_height():
        goomba_pos_y = HEIGHT - goomba_img.get_height()
    if goomba_pos_y < 0: #se o goomba sair da tela por baixo...
        goomba_pos_y = 0

    #adicionar o mario no canvas
    if frame_counter % 30 == 0:
        mario_andando += 1
    if mario_andando > 2:
        mario_andando = 0
    screen.blit(mario_sprite.image_data, (0, 0), (mario_sprite.get_frame("ANDANDO", mario_andando)))

    mario_pos_x += mario_update_key_x
    if mario_pos_x > WIDTH: #se o mario sair da tela do lado direito...
        mario_pos_x = - mario_img.get_width()
    if mario_pos_x < - mario_img.get_width() : #se o mario sair da tela do lado esquerdo...
        mario_pos_x = WIDTH

    if e.type == pygame.KEYDOWN: #alguma tecla foi pressionada?
        if e.key == pygame.K_LEFT: #apertou a seta da esquerda
            print("apertou a seta da esquerda")
            mario_update_key_x = -3
        if e.key == pygame.K_RIGHT: #apertou a seta da direita
            print("apertou a seta da direita")
            mario_update_key_x = 3
        if e.key == pygame.K_RETURN: #apertou enter
            print("apertou o ENTER")
            bola_fogo_pos_x = mario_pos_x + 160
            if bola_fogo_em_movimento == False:
                bola_fogo_em_movimento = True

    if e.type == pygame.KEYUP: #alguma tecla foi solta?
        if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
            print("soltou as setas")
            mario_update_key_x = 0

    #se a bola de fogo tiver sido disparada...
    if bola_fogo_em_movimento:
        bola_fogo_angle -= 5
        bola_rodando = pygame.transform.rotate(bola_fogo_img, bola_fogo_angle)
        screen.blit(bola_rodando, (bola_fogo_pos_x, bola_fogo_pos_y))
        bola_fogo_pos_x += 8
    #else:

    #se a bola de fogo saiu da tela...
    if (bola_fogo_pos_x > WIDTH):
        bola_fogo_em_movimento = False
        bola_fogo_pos_x = mario_pos_x + 160

    pygame.display.update()

    clock.tick(60)
    #print("FPS:", clock.get_fps())

    frame_counter += 1
