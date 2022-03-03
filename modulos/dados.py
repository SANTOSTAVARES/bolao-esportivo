import sqlite3
from contextlib import closing

def palpites():
    conexao = sqlite3.connect("palpites.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE palpites (
      usuario text,
      codigo_partida text,
      resultado_partida text
    );
    """)
    conexao.close()


def salvar_palpite():
    conexao = sqlite3.connect("palpites.db")
    cursor =  conexao.cursor()
    cursor.execute(""" 
    INSERT INTO palpites (usuario, codigo_partida, resultado_partida)
    VALUES (?, ?, ?)
    """, (str(p1.usuario), str(p1.codigo_partida), str(p1.resultado_partida),))
    conexao.commit()
    conexao.close()
