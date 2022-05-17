from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.template import loader
from django.template.loader import get_template
from app_coder.models import Professor

def template_using_context(
    self, name: str = 'Name', last_name: str = 'Last_name'):
    miHtml = open(r"live_class_18\live_class_18\templates\template.html", "r")
    template = Template(miHtml.read())
    miHtml.close()

    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [4, 5, 8, 7, 3]
    }

    my_context = Context(context_dict)
    render = template.render(my_context)
    return HttpResponse(render)

def template_using_loader(
    self, name: str ='name', last_name: str = 'last_name'):
    template = loader.get_template('template_loader.html')
    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [4, 5, 8, 7, 3]
    }
    render = template.render(context_dict)
    return HttpResponse(render)

def template_challenge(
    self, name: str ='name', last_name: str = 'last_name'):
    template = loader.get_template('template_challenge.html')
    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [4, 5, 8, 7, 3]
    }
    render = template.render(context_dict)
    return HttpResponse(render)

def template_professor(
    self, name: str ='name', last_name: str = 'last_name'):
    template = loader.get_template('template_professor.html')
    profesor = Professor(name=name, last_name=last_name)
    profesor.save()
    context_dict = {
        'profesor' : profesor
    }
    render = template.render(context_dict)
    return HttpResponse(render)