from celery import shared_task
from .models import Comment


@shared_task
def delete_inactive_comments():
    Comment.objects.filter(
        is_active=False,
    ).delete()

    return "inactive comments removed successfully"
