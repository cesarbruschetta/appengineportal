#!/usr/bin/env python
# -*- coding: utf-8 -*-
import set_sys_path

from google.appengine.ext.webapp import util
from google.appengine.ext import webapp

from google.appengine.ext.webapp.util import run_wsgi_app

import appengine_admin
from config import *
from models import *

from views import MainHandler, PaginaHandler







def main():
    URL = [(r'^(/admin)(.*)$', appengine_admin.Admin),  # Admin pages 
           ('/', MainHandler),
           (r'^(/pg)(.*)$', PaginaHandler),
           ]
    
    
    application = webapp.WSGIApplication(URL, debug=DEBUG)
    util.run_wsgi_app(application)
    webapp.template.register_template_library('templatetags.portal_extra')

if __name__ == '__main__':
    main()
    