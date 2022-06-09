from rest_framework import serializers
from .models import words
from django.contrib.auth.models import User

class wordsSerializer(serializers.ModelSerializer):
    word = serializers.CharField(max_length=100)
    defn = serializers.CharField(max_length=100)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return words.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.title = validated_data.get('title', instance.title)
        return instance

    class Meta:
        model = words
        fields = ['word', 'defn', 'owner']

    owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=words.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']