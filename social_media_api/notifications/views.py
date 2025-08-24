# notifications/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Fetch notifications for logged-in user, unread first
        return Notification.objects.filter(recipient=self.request.user).order_by("read", "-timestamp")


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def mark_notification_as_read(request, pk):
    try:
        notification = Notification.objects.get(pk=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({"detail": "Notification marked as read."})
    except Notification.DoesNotExist:
        return Response({"detail": "Notification not found."}, status=404)

