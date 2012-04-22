# -*- coding: utf-8 -*-
from google.appengine.ext import webapp

from Base import doRender


class MainHandler(webapp.RequestHandler):
    def get(self):
        #self.response.out.write('Hello world!')
        doRender(self,'index.html')


class PaginaHandler(webapp.RequestHandler):
    def get(self, urlPrefix, url):
        D={}
        D['parametro'] = urlPrefix
        D['teste'] = url
        doRender(self,'pagina.html',D)
