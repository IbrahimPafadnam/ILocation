from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'nom', 'bien', 'email', 'contact_date')
  list_display_links = ('id', 'nom')
  search_fields = ('nom', 'email', 'bien')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)