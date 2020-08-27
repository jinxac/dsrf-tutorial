from django.urls import path
from snippets import views

urlpatterns = [
  path('snippets/', views.snippets_list),
  path('snippets/<int:pk>/', views.snippets_detail)
]