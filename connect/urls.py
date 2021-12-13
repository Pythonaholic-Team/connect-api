from django.urls import path
from .views import (
    PostViewsList,
    PostDetail,
    OfferViewsList,
    OfferDetail,
)

urlpatterns = [
    path("", PostViewsList.as_view(), name="post"),
    path("<int:pk>/post_detail", PostDetail.as_view(), name="post_detail"),
    path("offer/", OfferViewsList.as_view(), name="offer"),
    path("offer/<int:pk>/offer_detail/", OfferDetail.as_view(), name="offer_detail"),
]
