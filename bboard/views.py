from django.template import loader

from django.http import HttpResponse
from django.shortcuts import render

from bboard.models import Bb


def index(request):
    bbs = Bb.objects.order_by('-publish')
    context = {'bbs':bbs}

    return render(request, 'bboard/index.html', context)