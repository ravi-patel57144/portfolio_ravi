from django.shortcuts import render

from .models import Profile
from dash.models import Docs


# Create your views here.
def home(request):
    profile = Profile.objects
    docs = Docs.objects.filter().first()
    return render(request, 'index.html', {'profile': profile, 'docs': docs})