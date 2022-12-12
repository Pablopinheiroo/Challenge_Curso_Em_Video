""" Desafio 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

msg = 'Reproduzindo um Toque MP3'
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

from playsound import playsound

# É Necessário colocar a música no mesmo local do arquivo.py
print('Redrodução de Áudio.mp3')
rp = input('Aperte Enter para reprodução')
print(playsound('toque.mp3'))

# Obs: Áudio baixando de: https://toqueparacelular.com/toques-wonderful/ - usado somente para teste,
# sem quaisquer fim lucrativo