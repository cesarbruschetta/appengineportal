# -*- coding: utf-8 -*-
from google.appengine.ext import db
from Slug import SlugProperty


class Pagina(db.Model):
    title = db.StringProperty("Titulo", required = True)
    content = db.TextProperty("Conteúdo", required = True)
    data_created = db.DateTimeProperty("Criação", auto_now_add = True)
    data_updated = db.DateTimeProperty("Atualização", auto_now = True)
    slug = SlugProperty(title)


    def __str__(self):
        return str(self.title)


    @classmethod
    def getAll(self):
        return Pagina.all()
    
    @classmethod   
    def getItem(self,slug):
        return Pagina.all().filter('slug =',slug).get()