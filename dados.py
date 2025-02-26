import sqlite3

def criar_banco_dados():
    """
    Cria um banco de dados SQLite com tabelas para livros, usuários e empréstimos.
    """
    try:
        # Conexão com o banco de dados (cria o arquivo se não existir)
        con = sqlite3.connect('dados.db')
        cursor = con.cursor()  # Cria um cursor para executar comandos SQL

        # Criar tabela de livros
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                editora TEXT,
                ano_publicacao INTEGER,
                isbn TEXT UNIQUE
            )
        ''')

        # Criar tabela de usuários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                endereco TEXT,
                email TEXT UNIQUE,
                telefone TEXT
            )
        ''')

        # Criar tabela de empréstimos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_livro INTEGER NOT NULL,
                id_usuario INTEGER NOT NULL,
                data_emprestimo TEXT NOT NULL,
                data_devolucao TEXT,
                FOREIGN KEY (id_livro) REFERENCES livros(id),
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        ''')

        con.commit()  # Salva as alterações no banco de dados
        print("Banco de dados criado com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")

    finally:
        if con:
            con.close()  # Fecha a conexão com o banco de dados

if __name__ == "__main__":
    criar_banco_dados()