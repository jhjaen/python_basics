# -*- coding: utf-8 -*-
# Crie uma classe Carro ela deve ter os atributos:
#  4 rodas
#  portas
#  motor
#  vidros
# e os seguintes metodos:
#   ligar
#   acelerar
#   frear
#   desligar

# class Carro():

#     def __init__(self):
#         self.rodas = 4
#         self.portas = 4
#         self.motor = True
#         self.vidros = True
#         self.ligado = False
#         self.parado = True
    
#     def ligar(self):
#         self.ligado = True
#         print('Ligando!')

#     def acelerar(self):
#         if self.ligado == True:
#             print('Acelerando!')
#             self.parado = False
#         else:
#             self.parado = True
    
#     def frear(self):
#         if self.parado == False:
#             print('Freando!')
#             self.parado = True
#         else:
#             pass

#     def desligar(self):
#         if self.ligado == True:
#             print('Desligando!')
#             self.ligado = False
#         else:
#             pass


# meuCarro = Carro()

# meuCarro.ligar()
# meuCarro.acelerar()
# meuCarro.frear()
# meuCarro.desligar()

# print(meuCarro.motor)

# class Personagem():
#     """Classe que representa um personagem de rpg"""

#     def __init__(self, nome):
#         """Inicializando as propriedade do personagem(Construtor)"""
#         self.nome = nome
#         self.xp = 0
#         self.hp = 100
#         self.mp = 100
#         self.forca = 5
#         self.defesa = 5
#         self.nivel = 1

# Herança
# class Mago(Personagem):

#     def conjurar_magia():
#         print('Casting..')

class Passaro():
    def __init__(self):
        self.penas = True
        self.asas = 2
        self.bico = True
        self.patas = 2
        self.rabo = True
        self.olhos = 2

    def voar(self):
        print('Passaro voando')
    
    def pousar(self):
        print('Pousando')

    def dormir(self):
        print('Dormindo')

    def comer(self):
        print('comendo')

    def cantar(self):
        print('cantando')

class Sabia(Passaro):

    def cantar(self):
        print('Assobiando')

class Galinha(Passaro):

    def voar(self):
        print('Pulando')
    
    def pousar(self):
        print('Queda controlada')

    def cantar(self):
        print('Cóóóóóóó')


sabia = Sabia()
galinha = Galinha()

print('Galinha: ')
galinha.cantar()
print('')

print('Sabia:')
sabia.cantar()
