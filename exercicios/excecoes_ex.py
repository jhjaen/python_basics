# -*- Coding: utf-8 -*-

# faça um programa que valide se o usuário é funcionario
# caso seja
# imprima acesso permitido
# caso não
# impima acesso negado
# sendo que o funcionario frodo está bloqueado
# caso ele tente entrar será exibido um NameError com a seguinte mensagem
# Usuário bloqueado, ir direto pro RH

funcionarios = ['joao','maria','carlos','paula','mario','frodo']
usuario = input('Digite seu login: ')

try:
    if usuario in funcionarios:
        if usuario == funcionarios[-1]:
            raise NameError('Usuário bloqueado, ir direto pro RH')
        else:
            print('Acesso Permitido')
    else:
        print('Acesso Negado!')
except NameError as n:
    print(n)
