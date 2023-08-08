from django.urls import path
from blog.views import BlogLeft, BlogLeftDetails

urlpatterns = [
    path('blog-details/<int:pk>/', BlogLeftDetails.as_view(), name='blog-details-right'),
    path('', BlogLeft.as_view(), name='blog-left'),

]
