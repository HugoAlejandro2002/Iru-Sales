from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import CustomerViewSet, NoteViewSet,  convert_lead_to_customer, delete_customer

router = DefaultRouter()

router.register('customers',CustomerViewSet, basename='customers')
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('convert_lead_to_customer/', convert_lead_to_customer, name='convert_lead_to_customer'),
    path('customers/delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('',include(router.urls))
]