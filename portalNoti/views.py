# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from portalNoti.models import Noticia, Categoria, Contacto
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.

def noticia_list(request):
    data = {}
    data['object_list'] = Noticia.objects.all().order_by('-created')[:6]
    data['destacada'] = Noticia.objects.filter(destacada = True).order_by('-created')[:1]

    template_name = 'portalNoti/index.html'
    return render(request, template_name, data)

def noticia_detalle(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    template_name = 'portalNoti/noticia_detalle.html'
    return render(request, template_name, {'noticia': noticia})

def contactos(request):
 	data = request.Contacto.objects.all()
 	template_name = 'portalNoti/contactos.html'
	return render(request, template_name, data)

