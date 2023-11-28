from django.urls import path
from .views import Home, Page

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/', Page.as_view(), name='page'),
]