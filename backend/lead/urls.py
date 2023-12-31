from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import LeadViewSet

router = DefaultRouter()

router.register('leads',LeadViewSet, basename='leads')

urlpatterns = [
    path('',include(router.urls))
]