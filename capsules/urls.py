from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.listeCapsules, name='liste'),
    path('liste des capsules/', views.allCapsules, name='capsules'),
    path('capsule/<int:id>/', views.getCapsule, name='capsule'),
    path('addcapsule/', views.addCapsule, name='ajouter'),
    path('update/<int:id>/', views.updateCapsule, name='editer'),
    path('delete/<int:id>/', views.deleteCapsule, name='supprimer'),
]
