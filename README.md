# Projeto Django

## 🚀 Configuração do Ambiente

### 1. Criando ambiente virtual
```bash
python3.14 -m venv venv
```

### 2. Ative o ambiente virtual
```bash
source venv/bin/activate
```

### 3. Instalando as dependências
```bash
pip install -r requirements.txt
```

### 4. Congelar as dependências (após instalar novos pacotes)
```bash
pip freeze > requirements.txt
```

## 🐘 Banco de Dados (Docker)

### Iniciando o PostgreSQL
O Docker vai virtualizar o banco de dados:
```bash
docker-compose up
```

### Parando o Docker
```bash
docker-compose down
```

## ▶️ Rodando o Projeto

### Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

---

## 📝 Observações

- Certifique-se de ter o Docker instalado para rodar o banco de dados
- O servidor estará disponível em `http://127.0.0.1:8000/`
- Sempre ative o ambiente virtual antes de trabalhar no projeto