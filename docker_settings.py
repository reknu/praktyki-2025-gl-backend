import os
from pathlib import Path

# Ustaw podstawowy katalog projektu. `os.getcwd()` jest bezpieczne w Dockerze.
BASE_DIR = Path(os.getcwd())

# Lista zainstalowanych aplikacji musi zawierać `staticfiles`
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # Dodaj tutaj inne aplikacje, jeśli są potrzebne do collectstatic
]

# Katalog, do którego collectstatic skopiuje wszystkie pliki
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Secret Key i inne niezbędne ustawienia
# Django potrzebuje SECRET_KEY, nawet w trybie collectstatic
SECRET_KEY = 'any-secret-key-for-build-time'