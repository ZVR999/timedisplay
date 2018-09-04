# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", gmtime())
    }
    print context
    return render(request, 'time_display/index.html', context)
