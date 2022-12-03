from django.urls import path
from .views import Homepage,SnackListView,SnackListDetail
urlpatterns = [
    path('', Homepage.as_view(),name='home'),
    path('snacks',SnackListView.as_view(),name='snacks'),
    path('snacks/<pk>',SnackListDetail.as_view(),name='detail')
]
