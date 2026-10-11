from django.contrib import admin
from django.urls import path
import MyBlog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyBlog.views.PostListView.as_view(), name='posts')
]
