from rest_framework.serializers import ModelSerializer

from trading.models import ContactInfo, Product, Vendor
from trading.validators import validate_hierarchy


class ContactInfoSerializer(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class VendorSerializer(ModelSerializer):
    contact = ContactInfoSerializer
    products = ProductSerializer(many=True)

    class Meta:
        model = Vendor
        fields = '__all__'
        validators = [validate_hierarchy]


class VendorUpdateSerializer(ModelSerializer):
    """
    Serializer for updating vendor's fields.
    """
    class Meta:
        model = Vendor
        fields = ('pk', 'title', 'level', 'contact', 'products', 'debt_to_supplier')
        read_only_fields = ('pk', 'created_at', 'debt_to_supplier',)
        validators = [validate_hierarchy]
