#!python3
#  -*- coding: utf-8 -*-

# n = 1
# while n < 10:
#     print(f'Numero: {n}')
#     n += 1

# print('Fim do While! ')

# frutas = ['limao','pera','abacaxi','maça','uva']
# for fruta in frutas:
#     print(fruta)
# print('Fim For! ')

# for n in range(1, 100, 1)
#     print(n)

# for n in frutas:
#     print(len(n))

# for n in 'frutas':
#     print(n)

# for num,item in enumerate(frutas):
#     print(f'Index: {num} \nFruta: {item}')

#Concessionaria
# carros = ['Corsa', 'Cruze','Fiat 147']
# cores = ['branco','preto','prata']

# for carro in carros:
#     for cor in cores:
#         print(f'Carro: {carro}, Cor: {cor}')
#     print(20*'-')

#Controle loop

# cont = 0

# while cont < 10:
#     print(f'vezes de execucao {cont + 1}')
#     if cont == 5:
#         print('Bloco de condição interrompe o loop')
#         break
#     cont += 1

# uso do continue
# impar = []

# for num in range(20):
#     if num % 2 == 0:
#         continue
#     else:
#         impar.append(num)

# print(impar)

usuarios = ['maria','joao','caio','roberto']
user = []
for n in usuarios:
    user.append(n.lower())

cont = 0
while True:

    usuario = input("Digite seu login: ")

    if usuario in user:
        print('Acesso concedido')
        break
    elif usuario.lower() in user:
        print('Acesso concedido')
        print(f'usuario: {usuario.lower()} e não {usuario}')
        break

    else:
        if cont < 3:
            print('Acesso negado')
            cont += 1
            continue
        else:
            print('usuario bloqueado')
            break


