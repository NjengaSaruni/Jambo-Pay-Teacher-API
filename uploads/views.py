from rest_framework import generics

from common.mixins import GetQuerysetMixin
from uploads.models import Image, File
from uploads.serializers import ImageSerializer, FileSerializer


class ImageListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class FileListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer