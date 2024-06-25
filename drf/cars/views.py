import django_filters.rest_framework

from . models import Car
from . serializers import CarSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . permissions import CustomPermission

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CustomPermission,)
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['brand', 'mark', 'year', 'price']
