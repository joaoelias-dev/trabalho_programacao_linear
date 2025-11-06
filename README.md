-- Criando ambiente virtual
python3.14 -m venv venv

-- Ative o ambiente virtual:
source venv/bin/activate

-- instalando as dependências
pip install -r requirements.txt

-- congelar as depêndencias
pip freeze > requirements.txt

-- Rodar o projeto
python manage.py runserver

-- Rodando o docker
-- docker vai virtualizar o banco de dados
docker-compose up

-- para parar o docker
docker-compose down