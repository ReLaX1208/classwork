from django.contrib import admin

from bboard.models import Bb
from bboard.models import Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'price', 'publish', 'rubric')
    list_display_links = ('name', 'content')
    search_fields = ('name', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
