from django.shortcuts import render

# Create your views here.

from .models import Blog
from dash.models import Docs


def blogs(request):
    blog = Blog.objects
    docs = Docs.objects.filter().first()
    return render(request, 'projects.html', {'all_blogs': blog, 'docs': docs})