# -*- coding: utf-8 -*-
from pagina import Pagina
import appengine_admin

## Admin views ##
class AdminPagina(appengine_admin.ModelAdmin):
    model = Pagina
    listFields = ('title', 'data_created', 'data_updated')
    editFields = ('title', 'content')
    readonlyFields = ('data_created', 'data_updated')



# Register to admin site
appengine_admin.register(AdminPagina)