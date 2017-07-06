# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from portalNoti.models import Noticia, Categoria, Contacto

class NoticiaAdmin (admin.ModelAdmin):
	list_display = ('id','titular','categoria')


class CategoriaAdmin (admin.ModelAdmin):
	pass

class ContactoAdmin (admin.ModelAdmin):
	list_display = ('nombre','apellido' , 'email', 'telefono', 'domicilio', 'imagen')


admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Contacto, ContactoAdmin)


# Register your models here.
