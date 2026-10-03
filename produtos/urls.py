from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.novo, name='novo'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('editar/<int:id>', views.editar, name='editar')
]