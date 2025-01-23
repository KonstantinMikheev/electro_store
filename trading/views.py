from rest_framework import viewsets, generics

from trading.models import ContactInfo, Product, Vendor
from trading.paginators import Paginator
from trading.serializers import ContactInfoSerializer, ProductSerializer, VendorSerializer, VendorUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class ContactInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing contact information.
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    pagination_class = Paginator

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ('email', 'country', 'city')
    search_fields = ('email', 'country', 'city',)
    ordering_fields = ('email', 'country', 'city',)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Paginator

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ('title', 'model')
    search_fields = ('title', 'model',)
    ordering_fields = ('title', 'model',)


class VendorCreateAPIView(generics.CreateAPIView):
    """API endpoint for creating a new vendor."""
    serializer_class = VendorSerializer


class VendorListAPIView(generics.ListAPIView):
    """API endpoint for listing all vendors."""
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorRetrieveAPIView(generics.RetrieveAPIView):
    """API endpoint for retrieving a specific vendor."""
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorUpdateAPIView(generics.UpdateAPIView):
    """API endpoint for updating a specific vendor."""
    serializer_class = VendorUpdateSerializer
    queryset = Vendor.objects.all()


class VendorDestroyAPIView(generics.DestroyAPIView):
    """API endpoint for deleting a specific vendor."""
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
