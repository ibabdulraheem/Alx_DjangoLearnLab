from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework import response, permissions
from rest_framework import generics, permissions, status



#Views for Registration endpoint
User=get_user_model()
class RegistrationView(generics.CreateApiView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

#Login View that return 'Token'
class LoginView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    return super().post(request, *args, **kwargs)
  token = Token.objects.get(key = response.data['Token'])
  Response({
    'token': token.key,
    'user_id': token.user_id,
    'username': token.user.username
  })

# Profile view created
  class ProfileView(generics.RetrieveUpdateAPIView):  # Profile View: show or update profile
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# Follow view 
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Current user follows another user"""
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({"message": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)

#Unfollow view
class UnfollowUserView(generics.GenericAPIViewAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Current user unfollows another user"""
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)
        return Response({"message": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
      
#["CustomUser.objects.all()"]

