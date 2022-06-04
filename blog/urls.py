from django.urls import path
from .views import PostView, PostDetail, PostCreate, PostUpdate, PostDelete, CommentView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', PostView.as_view(), name='blog-home'),
    path('api/<int:pk>/comment/', CommentView.as_view(), name='blog_comment'),
    path('api/post/<pk>/', PostDetail.as_view(), name='post-detail'),
    path('api/create/', PostCreate.as_view(), name='post-create'),
    path('api/post/<pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('api/post/<pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('api/about/', views.about, name='blog-about'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)