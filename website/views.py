from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import View

# Create your views here.
def home(request):

    template = loader.get_template('beyersss/home.html')
    return HttpResponse(template.render(request))
