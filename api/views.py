from api.models import Blog
from api.serializers import BlogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BlogView(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self,request,pk=None,format=None):
        if pk is None:
            Blog_ = Blog.objects.all()
            serialize = BlogSerializer(Blog_,many=True)
            return Response(serialize.data,status=status.HTTP_200_OK) 
            
        Blog_ = self.get_object(id)
        serialize = BlogSerializer(Blog_)
        return Response(serialize.data,status=status.HTTP_200_OK) 
    
        
           
    