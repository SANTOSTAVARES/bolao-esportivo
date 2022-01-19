from partidas import tabela_partidas, lancar_partida, exibir_rodada, todas_partidas, atualizar_partida_palpites, apagar_partida
from palpites import tabela_palpites, todos_palpites


def app_admin():
    #Exibe as opções para administradores do app.

    while True:

        try:
            opcoes_admin = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            opcao_admin = int(input('Digite uma das opções abaixo e aperte "ENTER".\n(1) Criar tabela  de registro de partida.\n(2) Lançar partida nova.\n(3) Exibir partidas de uma rodada.\n(4) Exibir partidas de todas rodadas.\n(5) Inserir o resultado do time mandante.\n(6) Apagar partida.\n(7) Criar tabela de registro de palpite dos apostadores.\n(8) Exibir todos palpites registrados.\n(9) Voltar para menu principal'))
            if opcao_admin in opcoes_admin:
                if opcao_admin == 1:
                    #(1) Criar tabela de registro de partida.
                    tabela_partidas()
                elif opcao_admin == 2:
                    #(2) Lançar partida nova.
                    lancar_partida()
                elif opcao_admin == 3:
                    #(3) Exibir partidas de uma rodada.
                    exibir_rodada()
                elif opcao_admin == 4:
                    #(4) Exibir partidas de todas rodadas.
                    todas_partidas()
                elif opcao_admin == 5:
                    #(5) Inserir o resultado do time mandante.
                    atualizar_partida_palpites()
                elif opcao_admin == 6:
                    #(6) Apagar partida.
                    apagar_partida()
                elif opcao_admin == 7:
                    #(7) Criar tabela de registro de palpite dos apostadores.
                    tabela_palpites()
                elif opcao_admin == 8:
                    #(8) Exibir todos palpites registrados.
                    todos_palpites()
                elif opcao_admin == 9:
                    #(9) Voltar para menu principal
                    break
            else:
                print('Esta opção não é válida.')
        except:
            print('Ocorreu um erro.')