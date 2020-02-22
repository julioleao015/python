import math
import time
import os

# Função para Retornar ao Menu Principal.
def backMenu():
    print('\nDesejas voltar ao Menu? ')
    print('1. Sim. \n2. Não.')
    op_backMenu = int(input("\nDigite sua escolha: "))
    if(op_backMenu == 1):
        menu()
    elif(op_backMenu == 2):
        print('\nFinalizando Programa...')
        time.sleep(1)
        os.system("clear")
        #os.system("cls")
        os.system("exit")
    else:
        os.system("clear")
        #os.system("cls")
        print('\nOpção Inválida!')
        time.sleep(1)
        backMenu()
    #Fim da Função de Menu Principal.


# Função de Exibição de um Cabeçalho.
def cabecalho():
    os.system("clear")
    #os.system("cls")
    print('=' * 30)
    print(' ' * 10, 'Python')
    print('=' * 30)
    #Fim da Função do Cabeçalho.


# Função de Menu Principal.
def menu():
    cabecalho()
    print('\nOpções: ')
    print('1. Calcular IMC. \n2. Calcular Média de Notas. \n3. Sair')

    option = int(input('\nDigite sua escolha: '))

    if (option == 1):
        calculaIMC()
    elif (option == 2):
        mediaNota()
    elif (option == 3):
        print('\n3. Finalizando Programa...')
        time.sleep(1.5)
        os.system("clear")
        #os.system("cls")
        os.system("exit")
    else:
        print('\nOpção Inválida!')
        time.sleep(1)
        menu()
    # Fim da Função Menu.


# Função para Calcular IMC.
def calculaIMC():
    cabecalho()
    print('\n1. Calcular IMC.')
    nome = input('Qual seu nome? ')
    peso = float(input('Qual seu peso: '))
    altura = float(input('Qual sua altura? '))

    imc = peso/math.pow(altura, 2)

    if(imc < 18.5 ):
        print('\nResultado: ')
        print('{}, seu IMC é {}, você está na classificação "{}" com grau de obesidade {}.'.format(nome, round(imc), 'Magreza', '0'))
    elif((imc >= 18.5) and (imc <= 24.9)):
        print('\nResultado: ')
        print('{}, seu IMC é {}, você está na classificação "{}" com grau de obesidade {}.'.format(nome, round(imc), 'Normal', '0'))
    elif((imc >= 25) and (imc <= 29.9)):
        print('\nResultado: ')
        print('{}, seu IMC é {}, você está na classificação "{}" com grau de obesidade {}.'.format(nome, round(imc), 'Sobrepeso', 'I'))
    elif ((imc >= 30) and (imc <= 39.9)):
        print('\nResultado: ')
        print('{}, seu IMC é {}, você está na classificação "{}" com grau de obesidade {}.'.format(nome, round(imc), 'Obesidade', 'II'))
    elif (imc >= 40):
        print('\nResultado: ')
        print('{}, seu IMC é {}, você está na classificação "{}" com grau de obesidade {}.'.format(nome, round(imc), 'Obesidade Grave', 'III'))

    backMenu()
    #Fim da Função para Calcular IMC.


# Função para Calcular Média de Notas.
def mediaNota():
    cabecalho()
    print('\n2. Calcular Média de Notas.')
    print('\nQual seu nivel de estudo? ')
    print('1. Fundamental ou Médio.')
    print('2. Superior.')
    op_nivelEstudo = int(input("\nDigite sua escolha: "))

    #Nível Fundamental e Médio.
    if(op_nivelEstudo == 1):
        os.system("clear")
        #os.system("cls")
        cabecalho()

        media = float(input('Qual a Média Mínima na sua Escolha? '))
        nota1 = float(input('\nDigite sua Primeira Nota: '))
        nota2 = float(input('Digite sua Segunda Nota: '))
        nota3 = float(input('Digite sua Terceira Nota: '))
        nota4 = float(input('Digite sua Quarta Nota: '))

        notaFinal = (nota1+nota2+nota3+nota4)/4

        if(notaFinal >= media):
            print('\nResultado: ')
            print('Você foi Aprovado, sua Média foi de {}!'.format(notaFinal))
            backMenu()
        else:
            print('\nResultado: ')
            print('Você foi Reprovado, sua Média foi de {}!'.format(notaFinal))
            backMenu()

    #Nível Superior.
    elif(op_nivelEstudo == 2):
        os.system("clear")
        #os.system("cls")
        cabecalho()

        media = float(input('Qual a Média Mínima na sua Faculdade? '))
        nota1 = float(input('\nDigite sua Primeira Nota: '))
        nota2 = float(input('Digite sua Segunda Nota: '))

        notaFinal = (nota1 + nota2) / 2

        if (notaFinal >= media):
            print('\nResultado: ')
            print('Você foi Aprovado, sua Média foi de {}!'.format(notaFinal))
            backMenu()
        else:
            print('\nResultado: ')
            print('Você foi Reprovado, sua Média foi de {}!'.format(notaFinal))
            backMenu()

    else:
        os.system("clear")
        #os.system("cls")
        print('\nOpção Inválida!')
        time.sleep(1.5)
        mediaNota()


""" Chama da Função Menu Onde Se Inicia o Programa"""
menu()
