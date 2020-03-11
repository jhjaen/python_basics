# -*- Coding: Utf-8 -*-

# produtos = []

# def cadastrar_produto(produto):
#     global produtos
#     produtos.append(produto)

# def listar_produtos():
#     global produtos
#     for p in produtos:
#         print(p)

# def deleta_produto(produto):
#     global produtos
#     if produtos in produtos:
#         produtos.remove(produto)
#     else:
#         pass


# deleta_produto('laranja')
# cadastrar_produto('abacaxi')
# cadastrar_produto('limao')
# cadastrar_produto('laranja')
# deleta_produto('abacaxi')


# import requests


# def status_code():
#     SITE = 'https://google.com'
#     return requests.get(SITE)


# print(status_code())
# nome = 'python'

# def linux():

#     nome = 'linux'
#     print(nome)

# linux()
# print(nome)


# def nome(seu_nome=None):
#     print(seu_nome)

# nome('Daniel')


# def alterarServidor(atual, novo):
#     print('Atual Servidor:', atual)
#     print('Novo Servidor:',novo)



# frutas = []


# def adiciona_frutas(*itens):
#     global frutas
#     for i in itens:
#         frutas.append(i)


# adiciona_frutas('abacaxi', 'limao', 'laranja', 'pera', 'uva')

# print(frutas)


carros = []

def adiciana_carros(**modelos):
    global carros
    carros.append(modelos)


adiciana_carros(modelo01='fusca', modelo02='Fox', modelo03='Fiat 147')

# print(carros)

# pessoas = []

# def cadastro(nome, cpf, idade):
#     global pessoas
#     pessoa = dict(user_name=nome,user_cpf=cpf,user_idade=idade)
#     pessoas.append(pessoa)


# cadastro('Renato', '123456786433', 26)
# print(pessoas)

# soma = lambda x,y: x+y

# print(soma(10, 20))


numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


dobro = [x*2 for x in numeros]

print(dobro)

# dobro = list(map(lambda x: x * 2, numeros))


# from functools import reduce

# soma = reduce(lambda x, y: x + y, numeros)

# n_par = list(filter(lambda x: x % 2 == 0, numeros))

# print(n_par)
# for x in numeros:
#     dobro = []
#     dobro.append(x * 2)