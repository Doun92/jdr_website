from django.apps import AppConfig

class ScenarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scenario'

class ActeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acte'