# Importa o Flask para criar a aplicação web e o request para obter dados das requisições HTTP
# O jsonify é usado para converter dicionários Python em respostas JSON
from flask import Flask, request, jsonify
from flask_cors import CORS

# Importa o módulo sqlite3 para manipulação do banco de dados SQLite
import sqlite3

# Cria uma instância da aplicação Flask
app = Flask(__name__)
CORS(app)

# Função para inicializar o banco de dados SQLite


def init_db():
    # Abre uma conexão com o banco de dados 'database.db' usando o contexto "with" para garantir o fechamento
    with sqlite3.connect('database.db') as conn:
        # Cria a tabela "livros" se ela não existir, com as colunas:
        # id (chave primária auto-incrementada), titulo, categoria, autor e imagem_url
        conn.execute("""CREATE TABLE IF NOT EXISTS livros(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   categoria TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   imagem_url TEXT NOT NULL
                   )""")
        # Imprime uma mensagem no console informando que o banco de dados foi criado
        print("Banco de dados criado!!")


# Chama a função para criar o banco de dados ao iniciar o servidor
init_db()

# Define uma rota para a página inicial da aplicação


@app.route('/')
def home_page():
    # Retorna uma resposta HTML simples quando a rota principal é acessada
    return '<h2>Minha pagina com Flask</h2>'

# Define uma rota para cadastrar um novo livro via método POST


@app.route('/doar', methods=['POST'])
def doar():
    # Obtém os dados da requisição no formato JSON
    dados = request.get_json()

    # Extrai as informações do livro a partir dos dados recebidos
    titulo = dados.get('titulo')
    categoria = dados.get('categoria')
    autor = dados.get('autor')
    imagem_url = dados.get('imagem_url')

    # Verifica se todos os campos obrigatórios estão presentes
    if not all([titulo, categoria, autor, imagem_url]):
        # Retorna uma mensagem de erro e o código HTTP 400 (Bad Request) se faltar algum campo
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    # Abre uma conexão com o banco de dados usando o contexto "with"
    with sqlite3.connect('database.db') as conn:
        # Insere os dados do livro na tabela "livros" utilizando parâmetros para evitar SQL Injection
        conn.execute("""INSERT INTO livros (titulo, categoria, autor, imagem_url)
                     VALUES (?,?,?,?) 
                     """, (titulo, categoria, autor, imagem_url))

        # Confirma as alterações no banco de dados
        conn.commit()

        # Retorna uma mensagem de sucesso e o código HTTP 201 (Created)
        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
    with sqlite3.connect('database.db') as conn:
        livros = conn.execute("SELECT * FROM livros").fetchall()

    livros_formatados = []

    for livro in livros:
        dicionario_livros = {
        "id": livro[0],
        "titulo": livro[1],
        "categoria": livro[2],
        "autor": livro[3],
        "imagem_url": livro[4]
        }
        livros_formatados.append(dicionario_livros)
    return jsonify(livros_formatados)



# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Inicia o servidor Flask no modo de depuração (debug=True)
    app.run(debug=True)