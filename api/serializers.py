from django.db.models import fields
from rest_framework import serializers
from api.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('owner',)        
