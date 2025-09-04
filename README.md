# Django Intro 
### Para realizar a instalação:
```python
python -m venv .venv # Gerar o espaço de trabalho virtual

source .venv/bin/activate # Linux/Mac
.venv/Scripts/activate # Windows

pip install --upgrade pip # Atualizar o pip
pip install -r requirements.txt # Instala os pacotes atualizados!
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