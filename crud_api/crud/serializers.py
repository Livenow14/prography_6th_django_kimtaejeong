from .models import List
from rest_framework import serializers

class MySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields=('id','title','description','created_at')

class MyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id','title','description','created_at','updated_at')

class MyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('title', 'description','created_at','created_at')