from .views import home, PowerConsumptionViewSet
from django.urls import path
urlpatterns = [
    path('',home),
    path('details',PowerConsumptionViewSet.as_view({'get': 'list'}), name="get_details")
]