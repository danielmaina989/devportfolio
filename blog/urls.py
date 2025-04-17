from django.urls import path
from .views import BlogListView, BlogDetailView, ReplyCommentView, AddCommentView


app_name='blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('comment/<int:comment_id>/reply/', ReplyCommentView.as_view(), name='reply_comment'),
    path('post/<slug:slug>/comment/', AddCommentView.as_view(), name='add_comment'), 
]
