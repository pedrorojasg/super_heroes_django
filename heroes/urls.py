from django.urls import path
from heroes.views import listar_heroes


urlpatterns = [
    path('', listar_heroes, name="heroes"),
]
