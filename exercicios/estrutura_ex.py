# -*- coding: utf-8 -*-

# # dado a lista

# times = ['time', ['Corinthians', 'Palmeiras', 'São Paulo'], 'cores', ['Preto', 'Branco', 'Verde', 'Vermelho']]

# # imprima na tela as seguintes mensagens:


# # time: <nome_time>, cores: <cores_time>

# print(f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][1]}')
# print(f'{times[0]}: {times[1][1]}, {times[2]}: {times[3][2]}, {times[3][1]}')
# print(f'{times[0]}: {times[1][2]}, {times[2]}: {times[3][0]}, {times[3][1]}, {times[3][3]}')

# dado o dicionario:

dados = {
    'estados': {
        'sp':{
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg':{
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }

}

# Imprima as seguintes informações:

# 1. Nome dos estados

# modo certo, nem tanto
# print(dados['estados']['sp']['nome'])
# print(dados['estados']['rj']['nome'])
# print(dados['estados']['mg']['nome'])

#modo certo
# for i in dados['estados'].keys():
#     print(dados['estados'][i]['nome'])

# 2. Nome dos estados, quantidade de municipios e  população

# modo certo, nem tanto
# print(f"Nome: {dados['estados']['sp']['nome']} \nMunicipios: {dados['estados']['sp']['municipios']}\nPopulação: {dados['estados']['sp']['populacao']}")
# print(20*'-')
# print(f"Nome: {dados['estados']['rj']['nome']} \nMunicipios: {dados['estados']['rj']['municipios']}\nPopulação: {dados['estados']['rj']['populacao']}")
# print(20*'-')
# print(f"Nome: {dados['estados']['mg']['nome']} \nMunicipios: {dados['estados']['mg']['municipios']}\nPopulação: {dados['estados']['mg']['populacao']}")

# modo certo
# for i in dados['estados'].keys():
#     print(f"Nome: {dados['estados'][i]['nome']} \nMunicipios: {dados['estados'][i]['municipios']}\nPopulação: {dados['estados'][i]['populacao']}")
#     print(' ')
#     print(20*'-')

# Calculo de notas
# peça 4 notas do aluno
# se a nota final for maior que 7
# imprima aprovado
# se não
#imprima reprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print('Aluno aprovado')
elif media < 7 and media >= 5:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')


n1 = float(input('Digite a primeira numero: '))
n2 = float(input('Digite a segundo numero: '))

if n1 > n2:
    print('Numero 1 é o maior!')
elif n1==n2:
    print('Numeros iguais!')
else:
    print('Numero 2 é o maior!')