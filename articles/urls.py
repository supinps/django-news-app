from django.urls import path

from .views import TestPageView
from .views import HomePageView, CategoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestPageView.as_view(), name='test'),
    path('category/', CategoryPageView.as_view(), name='category'),
]
