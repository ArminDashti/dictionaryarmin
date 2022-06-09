from .models import words
from .permissions import vIsOwnerOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import wordsSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions

def words_list(request):
    if request.method == 'GET':
        permission_classes = [permissions.IsAuthenticatedOrReadOnly, vIsOwnerOrReadOnly]
        snippets = words.objects.all()
        serializer = wordsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    elif request.method == 'POST':
        # permission_classes = [permissions.IsAuthenticatedOrReadOnly, vIsOwnerOrReadOnly]
        data = JSONParser().parse(request)
        serializer = wordsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, vIsOwnerOrReadOnly]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, vIsOwnerOrReadOnly]
