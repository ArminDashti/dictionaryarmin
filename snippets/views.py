from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import api_view, throttle_classes

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@throttle_classes([OncePerDayUserThrottle])
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, code=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

