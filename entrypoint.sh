#!/bin/sh
set -e

if [ "${DB_ENGINE:-mysql}" = "mysql" ]; then
  echo "Esperando a que la base de datos MySQL este disponible en ${DB_HOST:-mysql}:${DB_PORT:-3306}..."
  until mysqladmin ping -h"${DB_HOST:-mysql}" -P"${DB_PORT:-3306}" -u"${DB_USER:-root}" -p"${DB_PASSWORD:-}" --silent; do
    sleep 2
  done
  echo "Base de datos disponible."
else
  echo "DB_ENGINE=${DB_ENGINE:-sqlite3}; usando SQLite local para esta ejecucion."
fi

# --fake-initial: la tabla 'aprendiz' ya la crea el dump de Mysql-init/
# al arrancar el contenedor de MySQL, asi que Django no debe intentar
# crearla de nuevo (fallaria con "table already exists"). Esto le dice
# a Django que revise si la tabla ya existe con esa forma y, si es asi,
# solo marque esa migracion como aplicada sin volver a correr el SQL.
echo "Aplicando migraciones..."
python manage.py migrate --fake-initial --noinput

echo "Recolectando archivos estaticos..."
python manage.py collectstatic --noinput

echo "Iniciando servidor Gunicorn en el puerto 8080..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8080 --workers 3
