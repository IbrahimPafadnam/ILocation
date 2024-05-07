from django.contrib import admin

from .models import Agent

class AgentAdmin(admin.ModelAdmin):
  list_display = ('id', 'nom', 'email', 'ajout_date')
  list_display_links = ('id', 'nom')
  search_fields = ('nom',)
  list_per_page = 25

admin.site.register(Agent, AgentAdmin)