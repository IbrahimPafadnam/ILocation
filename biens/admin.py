from django.contrib import admin

from django.contrib import admin

from .models import Bien, Categories

class BienAdmin(admin.ModelAdmin):
  list_display = ('id', 'nom', 'est_disponible', 'prix', 'ajout_date', 'agent','categorie')
  list_display_links = ('id', 'nom',)
  list_filter = ('agent',)
  list_editable = ('est_disponible',)
  search_fields = ('nom', 'description', 'ville', 'quartier', 'prix')
  list_per_page = 25

admin.site.register(Bien, BienAdmin)
admin.site.register(Categories)
