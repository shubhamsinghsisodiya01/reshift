from .views import home, SensorPiViewSet
from django.urls import path
urlpatterns = [
    path('',home),
    path('details',SensorPiViewSet.as_view({'get': 'list'}), name="get_details")
]