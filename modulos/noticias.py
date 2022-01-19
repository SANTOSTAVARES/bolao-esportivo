def acessar_links():
    #Exibe notícias de alguns times específicos, após o usuário selecionar um time com input pré-determinado.
    import urllib.request

    # Links dos times que são possíveis acessar notícia.
    links_times = {'espn': {1: 'https://www.espn.com.br/futebol/time/_/id/819/flamengo',
                            2: 'https://www.espn.com.br/futebol/time/_/id/874/corinthians',
                            3: 'https://www.espn.com.br/futebol/time/_/id/2674/santos',
                            4: 'https://www.espn.com.br/futebol/time/_/id/2029/palmeiras',
                            5: 'https://www.espn.com.br/futebol/time/_/id/2026/sao-paulo'},
                   'uol': {1: 'https://www.uol.com.br/esporte/ao-vivo/futebol/flamengo-agora/',
                           2: 'https://www.uol.com.br/esporte/ao-vivo/futebol/corinthians-agora/',
                           3: 'https://www.uol.com.br/esporte/ao-vivo/futebol/santos-agora/',
                           4: 'https://www.uol.com.br/esporte/ao-vivo/futebol/palmeiras-agora/',
                           5: 'https://www.uol.com.br/esporte/ao-vivo/futebol/sao-paulo-agora/'}}

    opcoes_time = [1, 2, 3, 4, 5]

    while True:

        try:
            numero_time = int(input('Insira o número do time para acessar as notícias e aperte Enter.\n(1) FLAMENGO (2)CORINTHIANS (3)SANTOS (4)PALMEIRAS (5)SÃO-PAULO'))  # Usuário seleciona o time a ser pesquisado.
        except:
            print('Aconteceu um erro')
        else:
            if numero_time in opcoes_time:

                fonte = urllib.request.urlopen(links_times['espn'][numero_time])
                ler_fonte = fonte.read()
                codigo_html = ler_fonte.decode("utf8")
                fonte.close()
                indice = 0
                textos_espn = []
                for _ in range(4):
                    indice_2 = codigo_html.find('data-mptype="story">', indice)
                    indice_3 = codigo_html.find('</a>', indice_2)
                    textos_espn.append(codigo_html[indice_2 + 20:indice_3])
                    indice = indice_3

                fonte = urllib.request.urlopen(links_times['uol'][numero_time])
                ler_fonte = fonte.read()
                codigo_html = ler_fonte.decode("utf8")
                fonte.close()
                indice = 0
                textos_uol = []
                for _ in range(4):
                    indice_2 = codigo_html.find('{"quote":{"cite":', indice)
                    indice_3 = codigo_html.find('","', indice_2)
                    textos_uol.append(codigo_html[indice_2 + 17:indice_3])
                    indice = indice_3

                print("\nFonte: ESPN")
                for _ in textos_espn:
                    print(_)

                print("\nFonte: UOL")
                for _ in textos_uol:
                    print(_)

                print('\n')
                break

            else:
                print('Esta opção não é válida')


def noticias_ou_sair():
    while True:

        opcao_continuar = [1, 2]

        try:
            acessar_app = int(input(
                "Digite o número correspondente a sua opção e aperte Enter.\n (1)Voltar para menu anterior\n (2)Acessar mais notícias"))
        except:
            print('Ocorreu um erro.')
        else:
            if acessar_app in opcao_continuar:
                if acessar_app == 1:
                    #(1)Voltar para menu anterior
                    break
                elif acessar_app == 2:
                    #(2)Acessar mais notícias
                    acessar_links()
                else:
                    print('Esta opção não é válida. Escolha a opção (1) ou (2).\n')
            else:
                print('As opções válidas são (1) e (2).\n')

def ler_noticias():
    acessar_links()
    noticias_ou_sair()

