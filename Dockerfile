FROM python:3.11-slim

WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port 
EXPOSE 8000

# La commande sera surchargée par docker-compose 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]