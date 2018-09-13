from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from common.models import Like
from common.serializers import AbstractFieldsMixin
from common.utils import get_unique_number
from divisions.models import Teacher, Student, Parent
from institutions.serializers import InstitutionInlineSerializer
from uploads.models import Image
from uploads.serializers import ImageSerializer, ImageInlineSerializer
from users.models import User, UserProfile, AccountType, InstitutionJoinRequest

class UserProfileSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileInlineSerializer(serializers.ModelSerializer):
    image = ImageInlineSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'created_at', 'image','bio')

class AccountTypeSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = AccountType
        fields = '__all__'

class AccountTypeInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = AccountType
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)

        try:
            if user.account_type.name == 'Teacher':
                Teacher.objects.create(user=user, created_by=user)
            elif user.account_type.name == 'Student':
                Student.objects.create(user=user, created_by=user)
            elif user.account_type.name == 'Parent':
                Parent.objects.create(user=user,token=get_unique_number(user), created_by=user)
        except:
            pass

    def update(self, user, validated_data):
        password = validated_data.pop('password', None)

        # Incase update contains  a password
        if password is not None:
            password = make_password(password)
            setattr(user, 'password', password)

        return super(UserSerializer, self).update(user, validated_data)

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    profiles = UserProfileInlineSerializer(read_only=True, many=True, source='first_three_pics')
    institution = InstitutionInlineSerializer(read_only=True)
    account_type = AccountTypeInlineSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'full_name','username',
                  'institution', 'gender', 'profiles', 'account_type', 'created_at',
                  'is_admin', 'teacher', 'student', 'parent']

class UserInlineSerializer(serializers.ModelSerializer):
    profiles = UserProfileInlineSerializer(read_only=True, many=True, source='first_three_pics')
    account_type = AccountTypeInlineSerializer(read_only=True)
    institution = InstitutionInlineSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'full_name',
                  'username', 'institution', 'gender','is_admin', 'account_type', 'profiles']

class LikeInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    created_by= UserInlineSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'created_at','created_by')

class InstitutionJoinRequestSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = InstitutionJoinRequest
        fields = '__all__'

class InstitutionJoinRequestListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    institution = InstitutionInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)
    approved_by = UserInlineSerializer(read_only=True)


    class Meta:
        model = InstitutionJoinRequest
        fields = ('id', 'created_by', 'created_at', 'institution', 'approved', 'approved_by')

class InstitutionJoinRequestInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = InstitutionJoinRequest
        fields = ('id', 'created_by','institution', 'approved', 'created_at')

class ForProfileUserInlineSerializer(serializers.ModelSerializer):
    account_type = AccountTypeInlineSerializer(read_only=True)
    institution = InstitutionInlineSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'full_name',
                  'username', 'institution', 'gender','is_admin', 'account_type']

class UserProfileListSerializer(serializers.ModelSerializer):
    created_by = ForProfileUserInlineSerializer(read_only=True)
    image = ImageInlineSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'created_by','bio','image')
