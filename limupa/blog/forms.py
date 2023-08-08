from django.forms import ModelForm

from blog.models import Comment


class BlogCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
