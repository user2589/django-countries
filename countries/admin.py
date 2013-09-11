from django.contrib import admin
from models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ('visible', 'code', 'name')
    list_display_links = ('name', 'code')
    list_filter = ('visible',)
    search_fields = ('name',)

admin.site.register(Country, CountryAdmin)
