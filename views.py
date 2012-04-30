# -*- coding: utf-8 -*-
from google.appengine.ext import webapp

from Base import doRender
from models.pagina import Pagina
from debug import dbg 

class MainHandler(webapp.RequestHandler):
    def get(self):
        #self.response.out.write('Hello world!')
        doRender(self,'index.html')


class PaginaHandler(webapp.RequestHandler):
    def get(self, urlPrefix, url):
        #dbg()
        D={}
        D['pagina'] = Pagina.getItem(url.replace('/',''))
        doRender(self,'pagina.html',D)
