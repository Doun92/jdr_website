from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_scenarios, name="index_scenarios"),
    path("<int:scenario_id>", views.detail_scenario, name="detail_scenario"),
]
