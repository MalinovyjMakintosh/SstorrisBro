import os
import sys

# Импортируйте настройки вашего проекта Django
from django.core.wsgi import get_wsgi_application

# Укажите настройки проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storisbro.settings')

# Запустите сервер разработки Django
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
