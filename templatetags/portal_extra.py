# -*- coding: utf-8 -*-

from google.appengine.ext import webapp

from RssFeed import RSSFeed


register = webapp.template.create_template_register()

def get_RSS(self):
       
    #url = 'http://rss.home.uol.com.br/index.xml'
    url = 'http://rss.noticias.uol.com.br/ultnot/index.xml'
    timeout = 60
    
    itens = RSSFeed(url, timeout)
    itens.update()
    
    return itens.items[:5]


#Registro de tag filter em template
register.filter(get_RSS)


