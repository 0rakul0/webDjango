# web-Django
 
estudos de front-end
 
[x]: # Language: markdown

[x]: # Path: README.md

# para iniciar o projeto
    
    conda create -n web-Django python=3.9
    conda activate djangoWeb
    pip install django
    django-admin startproject web
    cd web
    python manage.py makemigrations polls
    python manage.py migrate
    python manage.py shell
    from polls.models import Question, Mudanca
    Question.objects.all()
    from django.utils import timezone
    q = Question(question_texto="texto de pergunta",pub_date=timezone.now())
    python manage.py runserver
    python manage.py createsuperuser