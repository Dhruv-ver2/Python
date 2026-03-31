from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.fun, name='fun-view'),
    path('profile/', views.profile_view, name='profile'), # New path
    path('contact/', views.contact_view, name='contact'), # New path
]
