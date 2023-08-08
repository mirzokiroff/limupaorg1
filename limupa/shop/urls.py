from django.urls import path
from shop.views import ShoppingCart, WishList, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, \
    ProductDetails, ShopLeft, SingleProductNormal, Index, SearchView

# from shop.views import setcookie

urlpatterns = [
    path('shop/cart/', Cart.as_view(), name='cart'),
    path('shop/check-out/', CheckOut.as_view(), name='check-out'),
    path('shop/compare/', Compare.as_view(), name='compare'),
    path('shop/product-details/', ProductDetails.as_view(), name='product-details'),
    path('shop', ShopLeft.as_view(), name='shop'),
    path('shop/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('shop/single-product/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('wishlist/', WishList.as_view(), name='wishlist'),
    # path('setcookie', setcookie, name='cookie'),
    path('', Index.as_view(), name='index'),
    # path('search/', SearchView.as_view(), name='search-results'),
]
