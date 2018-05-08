from django.shortcuts import render
from django.http import Http404
from django.template import *
from .models import New, Team, Kurs, Faq
# Create your views here.
def index(request):
    path=request.path
    news_all=New.objects.order_by('id')[0:5]
    return render(request, 'glavnaya/page_glavnaya.html',locals())

def news(request):
    news_all=New.objects.order_by('-published')
    return render(request, 'glavnaya/news.html',locals())

def new(request, News_id):
    try:
        new_n=New.objects.get(pk=News_id)
    except New.DoesNotExist:
        raise Http404("Извините, такой страницы не существует!")
    N={'new':new_n}
    return render(request, 'glavnaya/new.html',N)

def contacts(request):
    return render(request, 'glavnaya/contacts.html')

def istoria(request):
    return render(request, 'glavnaya/istoria.html')

def polozheniye(request):
    return render(request, 'glavnaya/polozheniye.html')

def faq(request):
    faqs=Faq.objects.all()
    return render(request, 'glavnaya/faq.html',locals())

def team(request):
    team_so=Team.objects.filter(status='Сотрудник')
    team_tr=Team.objects.filter(status='Тренер')
    return render(request, 'glavnaya/team.html',locals())

def kursy(request):
    kurs_off=Kurs.objects.filter(status='Очный')
    kurs_on=Kurs.objects.filter(status='Онлайн')
    return render(request, 'glavnaya/kursy.html',locals())

def photogallery(request):
    #foto=Foto.objects.all()
    return render(request, 'glavnaya/photogallery.html',locals())
