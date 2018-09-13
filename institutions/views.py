from rest_framework import generics

from institutions.models import Institution, InstitutionType
from institutions.serializers import InstitutionSerializer, InstitutionTypeSerializer


class InstitutionListView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class InstitutionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionTypeListCreateView(generics.ListCreateAPIView):
    queryset = InstitutionType.objects.all()
    serializer_class = InstitutionTypeSerializer

class InstitutionTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstitutionType.objects.all()
    serializer_class = InstitutionTypeSerializer