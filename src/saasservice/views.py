from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    try:
        percent = ((page_qs.count()/qs.count())*100)
    except:
        percent = 0
    html_template = "home.html"
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count":page_qs.count(),
        'total_visit': qs.count(),
        'percent': percent
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)