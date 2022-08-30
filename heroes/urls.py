from django.urls import path
from heroes.views import listar_heroes, get_heroe


urlpatterns = [
    path('', listar_heroes, name="heroes"),
    path('<int:id>/', get_heroe, name="heroe"),
]
