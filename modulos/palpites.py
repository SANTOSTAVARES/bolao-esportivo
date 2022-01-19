import sqlite3
from contextlib import closing

def tabela_palpites():
    #Criar tabela de registro de palpites dos jogadores.

    try:
        conexao = sqlite3.connect("palpites.db")
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE palpites (
          id integer primary key autoincrement,
          usuario text,
          codigo_partida integer,
          palpite_partida integer,
          acerto text,
          rodada integer
        );
        """)
        conexao.close()
    except sqlite3.OperationalError as erro_previsto:
        print(erro_previsto)
    except:
        print('Ocorreu um erro na criação da tabela de partidas.')
    else:
        print('Tabela criada com sucesso.')


def lancar_palpites():
    #Lançar palpites de uma rodada específica.

    try:
        usuario = str(input('Informe o seu nome Username.'))
        informar_rodada = int(input('Você deseja lançar palpite sobre qual rodada?'))
        lista_aposta = []

        with sqlite3.connect("partidas.db") as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute("select * from partidas where rodada=:buscar_rodada", {"buscar_rodada": informar_rodada})
                while True:
                    resultado = cursor.fetchone()
                    if resultado is None:
                        break
                    print(f"Rodada: {resultado[3]} - id_partida: {resultado[0]}\n Confronto: {resultado[1]} x {resultado[2]}")
                    aposta = int(input(
                        'Informe o seu palpite sobre o mandante, conforme os números a seguir.\n (1) Vitória\n (2) Empate\n (3) Derrota\n'))
                    aposta_partida = (usuario, resultado[0], aposta, informar_rodada)
                    lista_aposta.append(aposta_partida)

        conexao = sqlite3.connect("palpites.db")
        cursor = conexao.cursor()
        cursor.executemany("""
        INSERT INTO palpites (usuario, codigo_partida, palpite_partida, rodada) 
        VALUES (?,?,?,?)
        """, lista_aposta)
        conexao.commit()
        conexao.close()
    except:
        print('Ocorreu um erro no lançamento da aposta.')


def todos_palpites():
    #Exibe todos palpites registrados.

    conexao = sqlite3.connect("palpites.db")
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT * FROM palpites;
    """)
    for _ in cursor.fetchall():
        print(_)
    conexao.close()


def palpites_rodada():
    #Exibir palpites da rodada.

    try:
        informar_rodada = int(input('Informe a rodada que você deseja consultar os palpites.'))

        # Este bloco busca na tabela de dados os jogos da rodada e os adiciona na lista de partidas.
        with sqlite3.connect("palpites.db") as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute(f'select * from palpites where rodada = "{informar_rodada}"')
                while True:
                    resultado = cursor.fetchone()
                    if resultado is None:
                        break
                    print(resultado)
    except:
        print("Ocorreu um erro, ao tentar exibir os palpites da rodada.")