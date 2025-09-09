# Django Intro 
### Para realizar a instalação:
```python
# Gerar o espaço de trabalho virtual
python -m venv .venv 
# Linux/Mac
source .venv/bin/activate
# Windows 
.\.venv\Scripts\activate 

# Atualizar o pip
pip install --upgrade pip 
# Instala os pacotes do útilmo "backup".
pip install -r requirements.txt

# Manter os pacotes sempre atualizados.
pip freeze > requirements.txt
```

### Comandos básicos
```python
# Para iniciar o servidor
python manage.py runserver

# Para buscar migrações no banco de dados 
python manage.py makemigrations
# Para migrar o banco de dados
python manage.py migrate

# Criar o superuser
python manage.py createsuperuser
```