# ============================================================
# Imagen para la aplicacion Django (equivalente al Dockerfile
# original de Spring Boot, pero para Python/Django).
# ============================================================
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dependencias de sistema necesarias para compilar mysqlclient
# y para que el contenedor pueda esperar a que la base de datos
# este lista (default-mysql-client trae el comando 'mysqladmin').
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiamos primero solo requirements.txt para aprovechar la cache
# de Docker y no reinstalar dependencias en cada build.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copiamos el resto del codigo fuente
COPY . .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Mismo puerto que exponia el proyecto Spring Boot original
EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]
