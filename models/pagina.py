# -*- coding: utf-8 -*-
from google.appengine.ext import db


class Pagina(db.Model):
    title = db.StringProperty("Titulo", required = True)
    content = db.TextProperty("Conteúdo", required = True)
    data_created = db.DateTimeProperty("Criação", auto_now_add = True)
    data_updated = db.DateTimeProperty("Atualização", auto_now = True)

    def __str__(self):
        return str(self.title)


