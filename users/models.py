from __future__ import unicode_literals

import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from common.models import AbstractBase, AbstractBareBase, Subject
from institutions.models import Institution
from uploads.models import Image

GENDER_TYPES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER')
)


class MyUserManager(BaseUserManager):
    """
    Reimplementing the django.contrib.auth.models UserManager
    by extending the BaseUserManager
    """

    def create(self, username, first_name, password=None,
               **extra_fields):
        p = make_password(password)
        user = self.model(
            username=username, first_name=first_name, password=p, **extra_fields)
        user.save()
        return user

    def create_superuser(self, username, first_name,
                         password, **extra_fields):
        user = self.create(username, first_name,
                           password, **extra_fields)
        user.active = True
        user.deleted = False
        user.is_superuser = True
        user.save()
        return user


class AccountType(AbstractBareBase):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.name)

    class Meta:
        app_label = 'users'


class User(AbstractBaseUser, PermissionsMixin):
    """
    Most Acquired from AbstractUser
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_TYPES, null=True, blank=True)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(
        default=False,
        help_text="Deletes should deactivate not do actual deletes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_number = models.CharField(max_length=40, null=True, blank=True)
    supervisors = models.ManyToManyField('self', related_name='supervisees', blank=True)
    institution = models.ForeignKey(Institution, related_name='members', null=True, blank=True)
    account_type = models.ForeignKey(AccountType, related_name='users', null=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        return '{}'.format(self.username)

    @property
    def is_staff(self):
        return self.is_superuser

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    short_name = property(get_short_name)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (
            (self.first_name or ''), (self.middle_name or ''), (self.last_name or ''))
        return full_name.strip()


    full_name = property(get_full_name)

    def first_three_pics(self):
        return self.profiles.all()[:3]

    class Meta:
        app_label = 'users'
        ordering = ['first_name', 'last_name', 'username']


class InstitutionJoinRequest(AbstractBase):
    # TODO What to do with denied requests
    created_by = models.OneToOneField(User, related_name='join_requests')
    institution = models.ForeignKey(Institution, related_name='join_requests')
    approved = models.NullBooleanField(null=True, blank=True)
    actor = models.ForeignKey(User, related_name='handled_join_requests', null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.approved:
            user = self.created_by
            user.institution = self.institution
            user.save()

        super(InstitutionJoinRequest, self).save(force_insert, force_update, using, update_fields)

    def __unicode__(self):
        return '{} - {}'.format(self.institution.name, self.created_by.username, self.approved)

    class Meta:
        app_label = 'users'
        unique_together = ('created_by', 'institution')


class UserProfile(AbstractBase):
    user = models.ForeignKey(User, null=True, blank=True, related_name='profiles')
    bio = models.TextField(null=True, blank=True)
    image = models.ForeignKey(Image, null=True, blank=True, related_name='profiles')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.user:
            self.user = self.created_by

        super(UserProfile, self).save()

    class Meta:
        app_label = 'users'
        ordering = ['-created_at']
