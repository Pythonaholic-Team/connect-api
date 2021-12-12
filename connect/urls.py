from django.urls import path
from .views import PostViewsList,PostDetail
urlpatterns = [
    path('',PostViewsList.as_view(), name='post'),
    path('<int:pk>/post_detail', PostDetail.as_view(), name='post_detail')
]