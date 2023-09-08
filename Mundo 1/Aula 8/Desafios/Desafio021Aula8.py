# Faça um program em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.init()
input('Digite Play para começar a Musica: ')
pygame.mixer_music.load('ladywriter.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Digite Stop para parar a Musica: ')
