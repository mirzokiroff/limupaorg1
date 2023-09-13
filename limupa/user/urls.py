from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

from user.views import ShoppingCart, Index, WishList, UserRegisterView, ProductDetails, Shop3, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, SingleProduct, SingleProductTabStyleTop, \
    UserLoginView, AboutUs

urlpatterns = [
    path('user/aboutus/', AboutUs.as_view(), name='aboutus'),
    path('user/register/', UserRegisterView.as_view(), name='sign_up'),
    path('user/login/', UserLoginView.as_view(), name='sign_in'),
    path('user/product-details/', ProductDetails.as_view(), name='product-details'),
    path('user/shop-3/', Shop3.as_view(), name='shop-3'),
    path('user/shop-left/', ShopLeft.as_view(), name='shop-left'),
    path('user/shop-right/', ShopRight.as_view(), name='shop-right'),
    path('user/shop-list/', ShopList.as_view(), name='shop-list'),
    path('user/shop-list-left/', ShopListLeft.as_view(), name='shop-list-left'),
    path('user/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('user/single-product/', SingleProduct.as_view(), name='single-product'),
    path('user/single-product-tab-style-top/', SingleProductTabStyleTop.as_view(), name='single-product-tab-style-top'),
    # path('user/wishlist/', WishList.as_view(), name='wishlist'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
