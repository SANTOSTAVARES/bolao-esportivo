from noticias import ler_noticias
from partidas import exibir_rodada, ranking
from palpites import lancar_palpites, palpites_rodada

def menu_jogador():
  #Exibe as opções dos jogadores

  while True:

    opcoes_usuario = [1, 2, 3, 4, 5]

    try:
        opcao_usuario = int(input('Digite uma das opções abaixo e aperte "ENTER".\n (1) Acesse as notícias dos times\n (2) Lance seus palpites\n (3) Veja quem são os ganhadores da rodada.\n (4) Exibir palpites da rodada.\n (5) Voltar para menu principal\n'))

        if opcao_usuario in opcoes_usuario:
          if opcao_usuario == 1:
            # (1)Acesse as notícias dos times
            ler_noticias()
          elif opcao_usuario == 2:
            # (2)Lance seus palpites
            lancar_palpites()
            pass
          elif opcao_usuario == 3:
            # (3) Veja quem são os ganhadores da rodada.
            ranking()
          elif opcao_usuario == 4:
            # (4) Exibir palpites da rodada.
            palpites_rodada()
          elif opcao_usuario == 5:
            # (5)Voltar para menu principal.
            break
    except:
        print('Aconteceu um erro')