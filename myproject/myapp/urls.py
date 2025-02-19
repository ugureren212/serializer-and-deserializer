from django.urls import path
from . import views  # Import views from the app

urlpatterns = [
    path('', views.home, name='home'),  # Example view
]
