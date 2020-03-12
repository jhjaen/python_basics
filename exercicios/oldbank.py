# -*- coding: utf-8 -*-
import datetime

class Conta_Bancaria():

    def __init__(self, conta, nome, saldo):
        self.numeroConta = conta
        self.nomeUsuario = nome
        self.saldoUsuario = saldo
        self.numeroBanco = '999'
        self.numeroAgencia = '08'

    def depositar(self, valor):
        self.saldoUsuario += valor
    
    def sacar(self, valor):
        if self.saldoUsuario < valor:
            print('Saldo insuficiente!')
        else:
            print(f'Saldo anterior: R$ {self.saldoUsuario}')
            self.saldoUsuario -= valor
            print(f'Valor sacado: R$ {valor}\nSaldo Atual: R$ {self.saldoUsuario}')
    
    def extrato(self):
        print(f'Data da consulta: {datetime.datetime.now()}')
        print('-'*20)
        print(f'Cliente: {self.nomeUsuario}')
        print(f'Ag: {self.numeroAgencia} Conta: {self.numeroConta}')
        print(f'Saldo em conta: R$ {self.saldoUsuario}')

conta001 = Conta_Bancaria(90657, 'Jose', 100)

conta001.depositar(5000)

conta001.sacar(250)

conta001.extrato()
