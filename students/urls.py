from django.urls import path
from . import views


urlpatterns = [
    path('show_data/', views.show_data, name='show_data'),
    path('submit_data/', views.submit_data, name='submit_data'),
]