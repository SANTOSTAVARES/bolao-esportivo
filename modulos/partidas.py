import sqlite3
from contextlib import closing


def tabela_partidas():
    #Criar tabela de registro de partidas.

    try:
        conexao = sqlite3.connect("partidas.db")
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE partidas (
          id_partida integer,
          time_mandante text,
          time_visitante text,
          rodada integer,
          resultado_mandante integer
        );
        """)
        cursor.close()
        conexao.close()
    except sqlite3.OperationalError as erro_previsto:
        print(erro_previsto)
    except:
        print('Ocorreu um erro na criação da tabela de partidas.')
    else:
        print('Tabela criada com sucesso.')

def lancar_partida():
    #Inserir registro de uma nova partida na tabela de dados.

    try:
        mandante = str(input('Informe o nome do time mandante.'))
        visitante = str(input('Informe o nome do time visitante.'))
        rodada = int(input('Informe o número da rodada.'))
        id_partida = int(input('Código da partida.'))

        conexao = sqlite3.connect("partidas.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO partidas (id_partida, time_mandante, time_visitante, rodada, resultado_mandante) VALUES(?,?,?,?,?)",
            (id_partida, mandante, visitante, rodada, ''))
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        print('Ocorreu um erro. Por favor, tente novamente.')
    else:
        print('Partida salva com sucesso.\n')


def exibir_rodada():
    #Exibir uma rodada específica com base no número inserido.

    try:
        informar_rodada = int(input('Qual rodada você deseja consultar?'))

        with sqlite3.connect("partidas.db") as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute("select * from partidas where rodada=:buscar_rodada", {"buscar_rodada": informar_rodada})
                while True:
                    resultado = cursor.fetchone()
                    if resultado is None:
                        break
                    print(f"id_partida: {resultado[0]} - Confronto: {resultado[1]} x {resultado[2]} - Rodada: {resultado[3]} - Resultado mandante: {resultado[4]}\n")
    except:
        print('Aconteceu um erro')


def todas_partidas():
    #Exibe todas partidas registradas na tabela de dados.

    conexao = sqlite3.connect("partidas.db")
    cursor = conexao.cursor()
    cursor.execute("select * from partidas")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"id_partida: {registro[0]} - time_mandante: {registro[1]} - time_visitane: {registro[2]} - rodada: {registro[3]} - resultado_mandante: {registro[4]}")
    conexao.close()


def atualizar_partida_palpites():
    #Informar o resultado do mandante de uma partida e atualizar na tabela de palpite sobre se cada apostador acertou ou não.. Cada número representa um resultado: (1) Vitória (2) Empate (3) Derrota.

    try:
        id_prtda = int(input("Informe o Id da partida que você irá lançar o resultado do mandante."))
        resultado_mandte = int(input("Informe o resultado do mandante, conforme os números a seguir.\n (1)Vitória\n (2)Empate\n (3)Derrota."))
        palpites_partida = []

        #Este bloco atualiza na tabela de registro de partida, o resultado do time mandante.
        conexao = sqlite3.connect("partidas.db")
        cursor = conexao.cursor()
        cursor.execute("""update partidas
                set resultado_mandante=:resultado_final
                where id_partida=:codigo_partida """, {"resultado_final": resultado_mandte, "codigo_partida": id_prtda})
        conexao.commit()
        conexao.close()

        #Este bloco cria uma lista com os palpites dos jogadores sobre uma partida específica. Esta lista é composta por outras listas e a coluna 0 refere-se ao id do registro no banco de dadose a coluna 1 com o palpite do apostador sobre a partida.
        with sqlite3.connect("palpites.db") as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute("select * from palpites where codigo_partida=:buscar_palpites", {"buscar_palpites": id_prtda})
                while True:
                    resultado = cursor.fetchone()
                    if resultado is None:
                        break
                    adiciona_palpite = palpites_partida.append([resultado[0], resultado[3]])

        #Este bloco registra na tabela de palpites se o apostador acertou ou não sobre cada partida.
        for _ in palpites_partida:
            if _[1] == resultado_mandte:
                conexao = sqlite3.connect("palpites.db")
                cursor = conexao.cursor()
                cursor.execute("""update palpites
                    set acerto=:preencher
                    where id=:palpite_registrado """, {"preencher": "SIM", "palpite_registrado": _[0]})
                conexao.commit()
                conexao.close()
            else:
                conexao = sqlite3.connect("palpites.db")
                cursor = conexao.cursor()
                cursor.execute("""update palpites
                    set acerto=:preencher
                    where id=:palpite_registrado """, {"preencher": "NÃO", "palpite_registrado": _[0]})
                conexao.commit()
                conexao.close()
        print('Atualizações realizadas com sucesso')
    except:
        print('Ocorreu um erro ao salvar as atualizações.')

def apagar_partida():
    #Excluir uma partida com base no id dela.

    informar_partida = input("Informe o código da partida que você deseja excluir")

    with sqlite3.connect("partidas.db") as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute("""delete from partidas where id_partida=:buscar_partida""", {"buscar_partida":informar_partida})
            print("Registros apagados: ", cursor.rowcount)
            if cursor.rowcount == 1:
                conexao.commit()
                print("Alteração gravada com sucesso")
            else:
                conexao.rollback()
                print("Ocorreu um erro na realização da tarefa.")


def ranking():
    #Aprensentar os ganhadores da rodada.

    try:
        informar_rodada = int(input('Informe a rodada que você irá atualizar o ranking'))
        lista_palpites = []
        apostadores = set()
        acerto_apostador = []
        ganhadores = []
        maior_resultado = []

        #Este bloco busca na tabela de dados os jogos da rodada e os adiciona na lista de partidas.
        with sqlite3.connect("palpites.db") as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute(f'select * from palpites where rodada = "{informar_rodada}"')
                while True:
                    resultado = cursor.fetchone()
                    if resultado is None:
                        break
                    adiciona_apostador = apostadores.add(resultado[1])
                    adicionar_lista = lista_palpites.append([resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5]])
        apostadores = list(apostadores)

        #Este bloco verifica quantos acertos cada apostador teve na rodada e os classifica.
        for x in apostadores:
            for y in lista_palpites:
                filtro_acertos = filter(lambda y: y[1] == x and y[4] == "SIM" and y[5] == informar_rodada, lista_palpites)
                filtro_acertos = list(filtro_acertos)
            abc = [x, int(len(filtro_acertos))]
            acerto_apostador.append(abc)
        acertos_ordenados = sorted(acerto_apostador, key=lambda x: x[1], reverse=True)
        maior_resultado = acertos_ordenados[0][1]
        for x in acertos_ordenados:
            if x[1] == maior_resultado:
                ganhadores.append(x)
        print(f'Os ganhadores desta rodada são: {ganhadores}')

    except:
        print('Não foi possível apresentar o Ranking da rodada, pois aconteceu um erro.')