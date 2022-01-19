from menu_jogador import menu_jogador
from app_adm import app_admin
from sys import exit

def tela_inicial():
    #Exibir menu de opções geral.

    opcoes_usuario = [1, 2, 3]

    while True:

        try:
            opcao_principal = int(input('Digite o número de uma das opções e aperte Enter.\n (1)MENU JOGADOR\n (2)MENU DE ADMINISTRADOR DA APLICAÇÃO\n (3)SAIR DA APLICAÇÃO\n'))
        except ValueError as erro:
            print(f'Ocorreu um erro: {erro}')
        except SyntaxError as erro:
            print(f'Ocorreu um erro: {erro}')
        except UnboundLocalError as erro:
            print(f'Ocorreu um erro: {erro}')
        else:
            if opcao_principal in opcoes_usuario:
                if opcao_principal == 1:
                    menu_jogador()
                elif opcao_principal == 2:
                    app_admin()
                elif opcao_principal == 3:
                    print('Você saiu da aplicação')
                    exit()
            else:
                print('Esta opção não é válida')