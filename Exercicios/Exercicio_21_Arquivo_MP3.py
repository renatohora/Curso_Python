''''Faça um programa em python que abra e reproduza o audio de um arquivo MP3.'''''

import pygame
pygame.init()
pygame.mixer.music.load('Exercicio_021_.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#nao funcionou.

