from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.Serializer):
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    title = serializers.CharField(style={'base_template': 'textarea.html'})  

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def validate(self, data):
        if data['code'] == 'tesla':
            data['code'] = 'GoodTesla'
            return data
        else:
            return data
    
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')