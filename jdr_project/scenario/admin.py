from django.contrib import admin

# import the models
from .models import Scénario, Acte


class ScenarioAdmin(admin.ModelAdmin):
    fields = ["titre", "description"]

class ActeAdmin(admin.ModelAdmin):
    fields = ["scenario", "titre", "description", "numero"]

# Register your models here.
admin.site.register(Scénario, ScenarioAdmin)
admin.site.register(Acte, ActeAdmin)
