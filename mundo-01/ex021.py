"""Exercício Python #021 - Tocando um MP3"""

import pygame
pygame.init()
#Não vou colocar nenhuma música por motivo de direitos autorais
pygame.mixer.music.load('Musica em mp3 escolhida') #substituir por musica escolhida na pasta
pygame.mixer.music.play()
pygame.event.wait()
input()
