# -*- coding: UTF-8 -*-
import re


def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)


def listar(nomes):
    print 'Listando nomes: '
    for nome in nomes:
        print nome


def filtrar(nomes):
    print 'Digite o nome que deseja procurar'
    nome = raw_input()
    nome_filtrado = re.findall(nome, ''.join(nomes))
    print nome_filtrado


def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite 3 para procurar um nome'
        print 'Digite 2 para mostrar lista de nomes, 1 para cadastrar, 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            filtrar(nomes)


menu()
