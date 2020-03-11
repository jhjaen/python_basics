# -*- coding: utf-8 -*-
personagens = []

def addPersonagem(nomePersonagem):
    global personagens
    personagens.append(nomePersonagem)

#Função q apaga o personagem da lista
def rmvPersonagem(nomePersonagem):
    global personagens
    personagens.remove(nomePersonagem)

print(personagens)