from django.urls import path
from . import views

urlpatterns = [
    # Listar e criar posts
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    
    # Detalhes, editar e deletar post específico
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    
    # Confirmação de delete (para modal)
    path('posts/<int:pk>/confirm-delete/', views.confirm_delete, name='post-confirm-delete'),
]