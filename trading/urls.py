from django.urls import path
from rest_framework.routers import DefaultRouter

from trading.views import ContactInfoViewSet, ProductViewSet, VendorCreateAPIView, VendorListAPIView, \
    VendorRetrieveAPIView, VendorUpdateAPIView, VendorDestroyAPIView
from users.apps import UsersConfig
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactInfoViewSet, basename='users')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path("vendors/create/", VendorCreateAPIView.as_view(), name="vendor_create"),
    path("vendors/", VendorListAPIView.as_view(), name="vendors_list"),
    path("vendors/retrieve/<int:pk>/", VendorRetrieveAPIView.as_view(),name="vendor_retrieve",),
    path("vendors/update/<int:pk>/", VendorUpdateAPIView.as_view(), name="vendor_update"),
    path(
        "vendors/destroy/<int:pk>/", VendorDestroyAPIView.as_view(), name="vendor_destroy"
    ),
]

urlpatterns += router.urls
