from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "social"

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/', views.edit_profile, name="profile_edit"),
    path('network/', views.network, name="network"),
    path('friends/', views.friends_list, name="friends_list"),
    path('like_post/<int:post_id>/', views.like_post, name = 'like_post'),
    path('like_comment/<int:comment_id>/', views.like_comment, name = 'like_comment'),
    path('comment/<int:post_id>/', views.add_comment, name = 'add_comment'),
    path("follow/<int:user_id>/", views.follow_user, name="follow_user"),
    path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow_user"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)