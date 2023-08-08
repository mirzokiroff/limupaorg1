from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import BlogCommentForm
from blog.models import Post, BlogCategory, Comment


class BlogLeft(ListView):
    model = Post
    template_name = 'blog-left-sidebar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        if self.request.GET:
            key = self.request.GET.get('q')
            if key:
                data['posts'] = Post.objects.filter(title__icontains=key)
                print(data['posts'])
            else:
                pic = self.request.GET.dict().popitem()[0]
                data['posts'] = BlogCategory.objects.get(title=pic).post_category.all()
        else:
            data['posts'] = Post.objects.all()
        data['recent'] = Post.objects.all().order_by('-created_at')[:10]
        data['category'] = BlogCategory.objects.all()
        # data['comments'] = Comment.objects.filter(post_id=self.object.id).all()
        return data


class BlogLeftDetails(DetailView, CreateView):
    model = Post
    form_class = BlogCommentForm
    template_name = 'blog-details-right-sidebar.html'
    success_url = reverse_lazy('blog-left')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['detailpost'] = Post.objects.filter(id=self.object.id).first()
        data['postcategory'] = Post.objects.get(pk=self.object.id).categories.all()
        data['category'] = BlogCategory.objects.all()
        data['recent'] = Post.objects.all().order_by('-created_at')[:10]
        data['comments'] = Comment.objects.filter(post_id=self.object.id).all()
        data['post'] = self.object.id
        return data

