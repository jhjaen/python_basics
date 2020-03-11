# -*- coding: utf-8 -*-

# class Servidor():

#     def __init__ (self):
#         self.cpu = None
#         self.memoria = None
#         self.disco = None
#         self.hostname = None

#     def adicionaProcessador(self, novo_proc):
#         self.cpu = novo_proc

#     def removeProcessador(self):
#         self.cpu = None

#     def adicionaDisco(self, disco):
#         self.disco = disco

#     def aumentaMemoria(self, mem):
#         if self.memoria ==None:
#             self.memoria = mem
#         else:
#             self.memoria += mem

#     def alterarHostname(self, host):
#         if self.memoria == None or self.cpu == None or self.disco == None:
#             print('Maquina não encontrada')
#         else:
#             self.hostname = host
#             print(f'Nova máquina: {host}')


# dns = Servidor()
# web = Servidor()
# dns.adicionaProcessador('Intel Xeon')
# dns.removeProcessador()
# dns.aumentaMemoria(4096)
# dns.alterarHostname('Servidor_DNS')
# print(web.cpu)
# print(dns.cpu)

class Automovel():

    def __init__(self, cor, pneu, marca, motor):
        self.cor = cor
        self.pneu = pneu
        self.marca = marca
        self.motor = motor

carro = Automovel('Prata', 4, 'Fiat 147', 'V8')

