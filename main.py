import pygame, random
from player import Player
from enemy import Enemy

pygame.init()

WIDTH, HEIGHT = 800, 600
X, Y = 0, 1
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) #cria janela
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

#sprite sheet mario
player = Player("mario_sprite_sheet.png", "sprite_data")
player.set_state("PARADO")
player.set_size(2.0)
player.set_position(100, 450)
mario_andando_frame = 0

#boneco do goomba
#TODO: classe abstrata entity
goomba = Enemy("Goomba", "goomba.png")
goomba.set_position(WIDTH / 2, 50)

#gráfico bola de fogo
'''
bola_fogo_img = pygame.image.load("bolafogo.png")
bola_fogo_img = pygame.transform.scale(bola_fogo_img, (int(bola_fogo_img.get_width() * 0.25), int(bola_fogo_img.get_height() * 0.25)))
bola_fogo_em_movimento = False
bola_fogo_pos_x = mario_pos_x + 160
bola_fogo_pos_y = mario_pos_y
bola_fogo_angle = 0
'''

#game loop
running = True
mario_update_key_x = 0
goomba_update_random_x = 0
goomba_update_random_y = 0
frame_counter = 0

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.blit(fundo_img, (0, 0))

    #adicionar o goomba no canvas
    screen.blit(goomba.image_data, goomba.get_position())
    goomba.add_position(goomba_update_random_x, goomba_update_random_y)
    #a cada 60 frames, o goomba se movimenta pra outra direção
    if frame_counter % 60 == 0:
        goomba_update_random_x = random.uniform(-3.0, 3.0)
        goomba_update_random_y = random.uniform(-3.0, 3.0)
        #print("Direção do goomba: (", goomba_update_random_x, goomba_update_random_y, ")")
    #se o goomba sair da tela do lado direito...
    if goomba.get_position()[X] > WIDTH - goomba.image_data.get_width():
        goomba.set_position_x(WIDTH - goomba.image_data.get_width())
    #se o goomba sair da tela do lado esquerdo...
    if goomba.get_position()[X] < 0:
        goomba.set_position_x(0)

    #se o goomba sair da tela por cima...
    if goomba.get_position()[Y] > HEIGHT - goomba.image_data.get_height():
        goomba.set_position_y(HEIGHT - goomba.image_data.get_height())
    if goomba.get_position()[Y] < 0: #se o goomba sair da tela por baixo...
        goomba.set_position_y(0)

    #adicionar o mario no canvas
    if frame_counter % 2 == 0:
        mario_andando_frame += 1
    if mario_andando_frame > 2:
        mario_andando_frame = 0

    player.add_position_x(mario_update_key_x)
    if player.get_position()[X] > WIDTH: #se o mario sair da tela do lado direito...
        player.add_position_x( - player.image_data.get_width())
    if player.get_position()[X] < - player.image_data.get_width() : #se o mario sair da tela do lado esquerdo...
        player.set_position_x(WIDTH)

    #print(player.get_state())
    #renderiza o mario
    if player.get_state() == "PARADO":
        if player.direction == "DIREITA":
            screen.blit(player.image_data, player.get_position(), (player.get_frame("PARADO", 0)))
        if player.direction == "ESQUERDA":
            mario_rect = player.image_data.subsurface((player.get_frame("PARADO", 0)))
            screen.blit(pygame.transform.flip(mario_rect, True, False), player.get_position())
    elif player.get_state() == "ANDANDO":
        if player.direction == "DIREITA":
            screen.blit(player.image_data, player.get_position(), (player.get_frame("ANDANDO", mario_andando_frame)))
        if player.direction == "ESQUERDA":
            mario_rect = player.image_data.subsurface((player.get_frame("ANDANDO", mario_andando_frame)))
            screen.blit(pygame.transform.flip(mario_rect, True, False), player.get_position())
    elif player.get_state() == "PULANDO":
        #player.add_position_y()
        print("vo = ", player.vo)
        print("a = ", player.a)
        print("t = ", player.t)

        print(player.vo * frame_counter + player.a * player.t**2 * 1/2)
        input()
        player.t += 1

    if e.type == pygame.KEYDOWN: #alguma tecla foi pressionada?
        if e.key == pygame.K_LEFT: #apertou a seta da esquerda
            #print("apertou a seta da esquerda")
            player.set_state("ANDANDO")
            player.set_direction("ESQUERDA")
            mario_update_key_x = -3
        if e.key == pygame.K_RIGHT: #apertou a seta da direita
            #print("apertou a seta da direita")
            player.set_state("ANDANDO")
            player.set_direction("DIREITA")
            mario_update_key_x = 3
        if e.key == pygame.K_RETURN: #apertou enter
            #print("apertou o ENTER")
            player.set_state("PULANDO")
            player.set_direction("DIREITA")

            player.t = 0

            '''
            bola_fogo_pos_x = mario_pos_x + 160
            if bola_fogo_em_movimento == False:
                bola_fogo_em_movimento = True
            '''

    #print(player.direction)

    if e.type == pygame.KEYUP: #alguma tecla foi solta?
        if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
            #print("soltou as setas")
            player.set_state("PARADO")
            mario_update_key_x = 0

    #se a bola de fogo tiver sido disparada...
    '''
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
    '''

    pygame.display.update()

    clock.tick(60)
    #print("FPS:", clock.get_fps())

    frame_counter += 1
