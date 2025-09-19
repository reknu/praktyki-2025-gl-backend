echo "Launching Server..."
find ./core_parking/migrations -type f ! -name '__init__.py' -delete && rm -rf ./db.sqlite3 && python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
echo "Server Launched Successfully!"