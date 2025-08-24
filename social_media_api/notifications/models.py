from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User,related_name="notifications",on_delete=models.CASCADE)
    actor = models.ForeignKey( User,related_name="notifications_from", on_delete=models.CASCADE )
    verb = models.CharField(max_length=255)  # "liked", "commented", "followed"
    target_content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE, null=True,blank=True )
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # mark as read/unread

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        if self.target:
            return f"{self.actor} {self.verb} {self.target}"
        return f"{self.actor} {self.verb}"
