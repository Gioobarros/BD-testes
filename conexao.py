### CREATE TABLE contato (
###    id serial primary key not null,
###    nome varchar(100) not null,
###   email varchar(40) not null,
###    telefone varchar(20),
###    data_nasc DATE not null default current_date
###);


import psycopg2
from psycopg2 import sql

def conexao():
    try:
        conn = psycopg2.connect(
            dbname="contato",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def inserir_dados(conn, nome, email, telefone, data_nasc):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO contato (nome, email, telefone, data_nasc) 
                VALUES (%s, %s, %s, %s)
            """, (nome, email, telefone, data_nasc))
            conn.commit()
            print("Dados inseridos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def selecionar_dados(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM contato")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Erro ao ler dados: {e}")

def atualizar_dados(conn, id, nome, email, telefone, data_nasc):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE contato 
                SET nome = %s, email = %s, telefone = %s, data_nasc = %s 
                WHERE id = %s
            """, (nome, email, telefone, data_nasc, id))
            conn.commit()
            print("Dados atualizados com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")

def deletar_dados(conn, id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM contato WHERE id = %s", (id,))
            conn.commit()
            print("Dados deletados com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar dados: {e}")

if __name__ == "__main__":

    while(True):
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            telefone = input("Digite o telefone: ")
            data_nasc = input("Digite a data de nascimento (AAAA-MM-DD): ")
            conn = conexao()
            if conn:
                inserir_dados(conn, nome, email, telefone, data_nasc)
                conn.close()
        
        elif opcao == 2:
            conn = conexao()
            if conn:
                selecionar_dados(conn)
                conn.close()
        
        elif opcao == 3:
            id = int(input("Digite o id: "))
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            telefone = input("Digite o telefone: ")
            data_nasc = input("Digite a data de nascimento (AAAA-MM-DD): ")
            conn = conexao()
            if conn:
                atualizar_dados(conn, id, nome, email, telefone, data_nasc)
                conn.close()
        
        elif opcao == 4:
            id = int(input("Digite o id: "))
            conn = conexao()
            if conn:
                deletar_dados(conn, id)
                conn.close()
        
        elif opcao == 5:
            break
        
        else:
            print("Opção inválida")
