rm .db.sqlite3

rm -rf agents/migrations/*
rm -rf biens/migrations/*
rm -rf contacts/migrations/*
rm -rf comptes/migrations/*
rm -rf pages/migrations/*
rm -rf media/*

python manage.py migrate admin zero
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero


python3 manage.py makemigrations agents

python3 manage.py makemigrations biens

python3 manage.py makemigrations pages

python3 manage.py makemigrations contacts

python3 manage.py makemigrations comptes

python3 manage.py migrate



