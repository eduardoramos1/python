# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuario'
    # o intelisense captura a string acima e deixa como 'dica' quando se passa o mouse em cima do nome da classe
    # '__' duplo underline é uma convenção python para dizer que algo deve ser tratado como privado

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0


    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)
    
    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas


class Data(object):
    'Classe para criação de data formatada'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print str(self.dia) + '/' + str(self.mes) + '/' + str(self.ano)
