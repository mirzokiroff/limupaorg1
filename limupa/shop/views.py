from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from shop.models import GeneralProductCategory, Detailed, Product, Core
from user.forms import OurTeamForm
from user.models import OurTeam


class W404(TemplateView):
    template_name = '404.html'


class AboutUs(View):
    def get(self, request, *args, **kwargs):
        customers = OurTeam.objects.all()
        return render(request, 'about-us.html', {'types': customers})


class BlogDetailsRight(TemplateView):
    template_name = 'blog-details-right-sidebar.html'


class BlogLeft(TemplateView):
    template_name = 'blog-left-sidebar.html'


class Cart(ListView):
    model = GeneralProductCategory
    template_name = 'cart.html'


class CheckOut(TemplateView):
    template_name = 'checkout.html'


class Compare(TemplateView):
    template_name = 'compare.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class Faq(TemplateView):
    template_name = 'faq.html'


class Index(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(Index, self).get_context_data()
        if self.request.GET:
            key = self.request.GET.get('q')
            data['post'] = Product.objects.filter(title__icontains=key)
        else:
            data['post'] = Product.objects.all()
        return data


class LoginRegister(TemplateView):
    template_name = 'login-register.html'


class ProductDetails(TemplateView):
    template_name = 'product-details.html'


class Shop3(TemplateView):
    template_name = 'shop-3-column.html'


class ShopLeft(TemplateView):
    template_name = 'shop.html'


class ShopRight(TemplateView):
    template_name = 'shop-right-sidebar.html'


class ShopList(TemplateView):
    template_name = 'shop-list.html'


class ShopListLeft(TemplateView):
    template_name = 'shop-list-left-sidebar.html'


class ShoppingCart(TemplateView):
    template_name = 'shopping-cart.html'


class SingleProduct(TemplateView):
    template_name = 'single-product.html'


class SingleProductAffiliate(TemplateView):
    template_name = 'single-product-affiliate.html'


class SingleProductCarousel(TemplateView):
    template_name = 'single-product-carousel.html'


class SingleProductGalleryLeft(TemplateView):
    template_name = 'single-product-gallery-left.html'


class SingleProductGroup(TemplateView):
    template_name = 'single-product-group.html'


class SingleProductNormal(TemplateView):
    template_name = 'single-product-normal.html'


class SingleProductSale(TemplateView):
    template_name = 'single-product-sale.html'


class SingleProductTabStyleTop(TemplateView):
    template_name = 'single-product-tab-style-top.html'


class WishList(TemplateView):
    template_name = 'wishlist.html'


class SearchView(ListView):
    model = Detailed
    template_name = 'search-results.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.request.GET:
            key = self.request.GET.get('q')
            if key:
                context['posts'] = Product.objects.filter(title__icontains=key)
                print(context['posts'])
            else:
                pic = self.request.GET.dict().popitem()[0]
                context['posts'] = Core.objects.get(title=pic).post_category.all()
        else:
            context['posts'] = Detailed.objects.all()

        return context

        # def get_context_data(self, *, object_list=None, **kwargs):
        #     data = super().get_context_data(object_list=object_list, **kwargs)
        #     if self.request.GET:
        #         key = self.request.GET.get('q')
        #         if key:
        #             data['posts'] = Post.objects.filter(title__icontains=key)
        #             print(data['posts'])
        #         else:
        #             pic = self.request.GET.dict().popitem()[0]
        #             data['posts'] = BlogCategory.objects.get(title=pic).post_category.all()
        #     else:
        #         data['posts'] = Post.objects.all()
        #     data['recent'] = Post.objects.all().order_by('-created_at')[:10]
        #     data['category'] = BlogCategory.objects.all()
        #     # data['comments'] = Comment.objects.filter(post_id=self.object.id).all()
        #     return data
