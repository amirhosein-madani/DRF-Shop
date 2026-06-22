from django.urls import path
from .views import CommentDetailGenericApiView, CommentListGenericApiView

urlpatterns = [
    path("comment/", CommentListGenericApiView.as_view(), name="comment-list"),
    path(
        "comment/<int:pk>/",
        CommentDetailGenericApiView.as_view(),
        name="comment-detail",
    ),
]
