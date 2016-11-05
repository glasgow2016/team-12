from django.contrib import admin
from helixapp.models import tree


class showTree(admin.ModelAdmin):
    list_display = ('treeName')

admin.site.register(tree)

