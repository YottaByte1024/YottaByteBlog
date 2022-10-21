from django.urls import path

from .views import BlogListView, ColPostsListView, PostView, \
    RegisterUserView, LoginUserView, logout_user, AddPostView, \
    UpdatePostView

urlpatterns = [
    path('', ColPostsListView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/addpost/', AddPostView.as_view(), name='add_post'),
    path('blog/<slug:post_slug>/', PostView.as_view(), name='post'),
    path('blog/<slug:post_slug>/update/', UpdatePostView.as_view(), name='update_post'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    ]
