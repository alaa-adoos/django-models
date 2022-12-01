from django.urls import path
from .views import Homepage,SnackListView
urlpatterns = [
    path('', Homepage.as_view(),name='home'),
    path('snacks',SnackListView.as_view(),name='snacks')#
]
