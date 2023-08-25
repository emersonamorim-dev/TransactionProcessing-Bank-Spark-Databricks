FROM python:3.8-slim

WORKDIR /app

# Copie os requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
