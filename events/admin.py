from django.contrib import admin

# Register your models here.
from .models import Event, Choice, Odds

class ChoicesAdmin(admin.TabularInline):
    model = Choice


class OddsAdmin(admin.TabularInline):
    model = Odds

class EventAdmin(admin.ModelAdmin):
    inlines = [
        ChoicesAdmin,
        OddsAdmin
    ]


admin.site.register(Event, EventAdmin)
