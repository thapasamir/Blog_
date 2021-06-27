from django.db.models import manager
from django.http.response import HttpResponse
from api.models import Blog
from api.serializers import BlogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


class BlogView(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        if pk is None:
            Blog_ = Blog.objects.all()
            serialize = BlogSerializer(Blog_,many=True)
            return Response(serialize.data,status=status.HTTP_200_OK) 
        id = pk    
        Blog_ = self.get_object(id)
        serialize = BlogSerializer(Blog_,many=False)
        return Response(serialize.data,status=status.HTTP_200_OK) 
    
    def post(self,request,format=None):
        serialize = BlogSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        if pk is None:
            return Response({'msg':'Please provide a id you want to put'})
        Blog_ = self.get_object(pk)
        serialize = BlogSerializer(Blog_,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        Blog_ = Blog.objects.get(id=pk)
        serialize = BlogSerializer(Blog_,data=request.data,partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        try:
            print(pk)
            pk = pk 
            obj = Blog.objects.get(id=pk)
            obj.delete()
            return HttpResponse({'Deleted sucesfully'})
        except Exception as e:
            return HttpResponse({e})