from django.views.generic import ListView
from MyBlog.post import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']
