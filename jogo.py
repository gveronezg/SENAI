#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Especifica que o script deve ser executado com Python 3 e usa a codificação UTF-8

# Importa o módulo pygame para criar o jogo
import pygame
# Importa o módulo Path do pathlib para manipulação de caminhos de arquivos
from pathlib import Path

# Obtém o diretório absoluto onde o script está localizado
DIRETORIO_ATUAL = str(Path(__file__).parent.absolute())

# Largura e altura da tela
largura_tela = 800
altura_tela = 600
# Largura e altura do personagem
largura_personagem = 100
altura_personagem = 100

# Cria a tela do jogo com uma resolução de 800x600 pixels
tela = pygame.display.set_mode([largura_tela, altura_tela])
# Define o título da janela do jogo como 'Sonic to Flash'
pygame.display.set_caption('Sonic to Flash')
# Cria um objeto Clock para controlar a taxa de atualização do jogo
clock = pygame.time.Clock()

# Carrega a imagem do personagem a partir do arquivo 'imagens/flash.png'
sonic = pygame.image.load('imagens/flash.png')
# Redimensiona a imagem do personagem para 100x100 pixels
flash = pygame.transform.scale(sonic, (largura_personagem, altura_personagem))
# Carrega a imagem de fundo a partir do arquivo 'imagens/fundo.png'
fundo = pygame.image.load('imagens/fundo.png')

# Inicializa o mixer de áudio do pygame
pygame.mixer.init()
# Carrega a música 'musicas/musica2.mp3'
pygame.mixer.music.load('musicas/musica2.mp3')
# Inicia a reprodução da música em loop
pygame.mixer.music.play()

# Inicializa as coordenadas x e y do personagem (sonic)
sonic_x = 100
sonic_y = 350
# Define a direção inicial do movimento como (0, 0) - sem movimento
direcao = (0, 0)

# Variável que controla o loop principal do jogo
executando = True
# Inicia o loop principal do jogo
while executando:
    # Processa todos os eventos da fila de eventos do pygame
    for evento in pygame.event.get():
        # Se o evento for o fechamento da janela (pygame.QUIT)
        if evento.type == pygame.QUIT:
            # Encerra o loop principal
            executando = False
        
        # Se uma tecla foi pressionada (pygame.KEYDOWN)
        if evento.type == pygame.KEYDOWN:
            # Se a tecla pressionada for W ou a seta para cima
            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                # Define a direção para cima
                direcao = (0, -20)
            # Se a tecla pressionada for S ou a seta para baixo
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                # Define a direção para baixo
                direcao = (0, 20)
            # Se a tecla pressionada for A ou a seta para a esquerda
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                # Define a direção para a esquerda
                direcao = (-20, 0)
            # Se a tecla pressionada for D ou a seta para a direita
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                # Define a direção para a direita
                direcao = (20, 0)
        
        # Se uma tecla foi solta (pygame.KEYUP)
        if evento.type == pygame.KEYUP:
            # Para o movimento do personagem
            direcao = (0, 0)

    # Atualiza as coordenadas x e y do personagem com base na direção
    sonic_x += direcao[0]
    sonic_y += direcao[1]

    # Verifica se o personagem saiu da tela pela direita
    if sonic_x > largura_tela:
        # Move o personagem para a extremidade esquerda da tela
        sonic_x = -largura_personagem
    # Verifica se o personagem saiu da tela pela esquerda
    if sonic_x < -largura_personagem:
        # Move o personagem para a extremidade direita da tela
        sonic_x = largura_tela

    # Verifica se o personagem saiu da tela pela parte inferior
    if sonic_y > altura_tela:
        # Move o personagem para a extremidade superior da tela
        sonic_y = -altura_personagem
    # Verifica se o personagem saiu da tela pela parte superior
    if sonic_y < -altura_personagem:
        # Move o personagem para a extremidade inferior da tela
        sonic_y = altura_tela
    
    # Desenha o fundo na tela na posição (0, 0)
    tela.blit(fundo, [0, 0])
    # Desenha o personagem na tela na posição atual (sonic_x, sonic_y)
    tela.blit(flash, [sonic_x, sonic_y])
    # Define a taxa de atualização do jogo para 30 frames por segundo
    clock.tick(50)
    # Atualiza a tela para mostrar as alterações
    pygame.display.update()

# Encerra o pygame e libera os recursos usados
pygame.quit()
