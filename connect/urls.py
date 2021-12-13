from django.urls import path
from .views import (
    PostViewsList,
    PostDetail,
    OfferViewsList,
    OfferDetail,
    CommentViewsList,
    CommentDetail,
)

urlpatterns = [
    path("", PostViewsList.as_view(), name="post"),
    path("<int:pk>/post_detail", PostDetail.as_view(), name="post_detail"),
    path("offer/", OfferViewsList.as_view(), name="offer"),
    path("offer/<int:pk>/offer_detail/", OfferDetail.as_view(), name="offer_detail"),
    path("comment", CommentViewsList.as_view(), name="comment"),
    path(
        "comment/<int:pk>/comment_detail/",
        CommentDetail.as_view(),
        name="comment_detail",
    ),
]
