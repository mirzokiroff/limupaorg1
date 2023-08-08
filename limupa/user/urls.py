from django.urls import path
from user.views import ShoppingCart, Index, WishList, LoginRegister, ProductDetails, Shop3, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleTop, \
    UserLoginView, AboutUs

urlpatterns = [
    path('user/aboutus/', AboutUs.as_view(), name='aboutus'),
    path('user/login-register/', LoginRegister.as_view(), name='login-register'),
    path('user/login-register/', UserLoginView.as_view(), name='login'),
    path('user/product-details/', ProductDetails.as_view(), name='product-details'),
    path('user/shop-3/', Shop3.as_view(), name='shop-3'),
    path('user/shop-left/', ShopLeft.as_view(), name='shop-left'),
    path('user/shop-right/', ShopRight.as_view(), name='shop-right'),
    path('user/shop-list/', ShopList.as_view(), name='shop-list'),
    path('user/shop-list-left/', ShopListLeft.as_view(), name='shop-list-left'),
    path('user/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('user/single-product/', SingleProduct.as_view(), name='single-product'),
    path('user/single-product-affiliate/', SingleProductAffiliate.as_view(), name='single-product-affiliate'),
    path('user/single-product-carousel/', SingleProductCarousel.as_view(), name='single-product-carousel'),
    path('user/single-product-gallery-left/', SingleProductGalleryLeft.as_view(), name='single-product-gallery-left'),
    path('user/single-product-group/', SingleProductGroup.as_view(), name='single-product-group'),
    path('user/single-product-normal/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('user/single-product-sale/', SingleProductSale.as_view(), name='single-product-sale'),
    path('user/single-product-tab-style-top/', SingleProductTabStyleTop.as_view(), name='single-product-tab-style-top'),
    # path('user/wishlist/', WishList.as_view(), name='wishlist'),
]
