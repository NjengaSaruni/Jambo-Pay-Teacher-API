from rest_framework import generics

from common.mixins import GetQuerysetBaseMixin, GetQuerysetMixin
from users.filters import JoinRequestFilter, UserProfileFilter
from users.models import User, AccountType, InstitutionJoinRequest, UserProfile
from users.serializers import UserSerializer, UserListSerializer, AccountTypeSerializer, \
    InstitutionJoinRequestSerializer, InstitutionJoinRequestListSerializer, UserProfileSerializer, \
    UserProfileListSerializer


class UserCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(GetQuerysetBaseMixin, generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []
    search_fields = (
        'username', 'first_name', 'last_name', 'email', 'mobile',
    )
    ordering = ('full_name',)



    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        return UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        return UserSerializer


class AccountTypeListCreateView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = AccountTypeSerializer
    queryset = AccountType.objects.all()


class AccountTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountTypeSerializer
    queryset = AccountType.objects.all()


class InstitutionJoinRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = InstitutionJoinRequestSerializer
    queryset = InstitutionJoinRequest.objects.filter(approved=None)
    filter_class = JoinRequestFilter
    search_fields = (
        'institution__name', 'institution__created_by__username',
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InstitutionJoinRequestListSerializer
        return InstitutionJoinRequestSerializer

class InstitutionJoinRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstitutionJoinRequestSerializer
    queryset = InstitutionJoinRequest.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InstitutionJoinRequestListSerializer
        return InstitutionJoinRequestSerializer


class UserProfileListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_class = UserProfileFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserProfileListSerializer
        return UserProfileSerializer

class UserProfileDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserProfileListSerializer
        return UserProfileSerializer
