from django.contrib import admin

# Register your models here.
from .models import Team
from .models import Player

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'date_created')

admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
