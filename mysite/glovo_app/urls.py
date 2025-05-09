from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'cart_item', CartItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('store/create/', StoreCreateAPIView.as_view(), name='store_create'),
    path('combo/', ComboListAPIView.as_view(), name='combo_list'),
    path('combo/create/', ComboCreateAPIView.as_view(), name='combo_create'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('store_list/', StoreListOwnerAPIView.as_view(), name='store_list_owner'),
    path('store_list/<int:pk>/', StoreDetailUpdateDestroyOwnerAPIView.as_view(), name='store_list_edit'),
    path('combo_list/', ComboListOwnerAPIView.as_view(), name='combo_list_owner'),
    path('combo_list/<int:pk>/', ComboDetailUpdateDestroyOwnerAPIView.as_view(), name='combo_list_edit'),
    path('product_list/', ProductListOwnerAPIView.as_view(), name='product_list_owner'),
    path('product_list/<int:pk>/', ProductDetailUpdateDestroyOwnerAPIView.as_view(), name='product_list_edit'),
    path('review/', StoreReviewAPIView.as_view(), name='review_create'),



]





