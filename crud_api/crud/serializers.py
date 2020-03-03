from .models import List
from rest_framework import serializers

class MySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields=('id','title','description','created_at')