# 📚 API Livros

Uma API REST simples para cadastro, listagem e gerenciamento de livros, desenvolvida com **Python**, **Flask** e **SQLite**. Com o intuito de 
ser consumida por um site criado de doação de livros, ambos realizados como projeto de conclusão do curso de Desenvolverdor Full Stack do Vai na Web.

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)

## 📂 Estrutura do Projeto
```
api_livros/
├── app.py          # Arquivo principal que executa a aplicação Flask
├── models.py       # Definições do modelo de dados e conexão com o banco
├── database.db     # Banco de dados SQLite
└── README.md       # Documentação do Projeto
```

## 🔧 Como Executar

### Pré-requisitos

- Python 3.10+
- `pip` instalado

### 1. Clone o repositório

```bash
git clone https://github.com/arielvasconcelosgoncalves/api_livros.git
cd api_livros
```
### 2. Crie um ambiente virtual e ative-o
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
#### Caso o arquivo requirements.txt não exista, instale manualmente:
```bash
pip install flask
```
### 4. Execute a API
```bash
python app.py
```
### 5. Acesse a API no navegador
#### Abra: http://localhost:5000

## 📌 Funcionalidades
✅ Cadastrar livros

✅ Listar todos os livros

✅ Buscar livros por ID

✅ Deletar livros por ID

## 🛠️ Melhorias Futuras

 - Atualizar livros

 - Filtro por autor, título ou ano

 - Paginação

 - Interface web simples com HTML

 - Testes automatizados

## 👨‍💻 Autor
Ariel Vasconcelos




