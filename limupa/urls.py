from django.urls import path, include

from shop.views import Index, W404, AboutUs, LoginRegister, Faq, Contact

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('users/', include('user.urls')),
    path('', Index.as_view(), name='index'),
    path('404/', W404.as_view(), name='404'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),
    path('login-register/', LoginRegister.as_view(), name='login-register'),
    path('faq/', Faq.as_view(), name='faq'),
    path('contact/', Contact.as_view(), name='contact'),
    path('', Index.as_view(), name='index'),

]
