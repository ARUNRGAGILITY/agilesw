from django.contrib import admin
from .models import *


class NewTodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title',  'author','active', 'done')
admin.site.register(NewTodoList, NewTodoListAdmin)
