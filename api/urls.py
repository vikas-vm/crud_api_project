from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.TodoListAPI.as_view()),
    path('create', views.TodoCreateAPI.as_view()),
    path('<int:pk>/', views.TodoViewAPI.as_view()),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
