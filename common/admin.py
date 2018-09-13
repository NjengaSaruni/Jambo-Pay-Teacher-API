# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps

from django.contrib import admin
from django.db.models.signals import post_migrate

from institutions.models import Institution
from users.models import User, AccountType

for model in apps.get_app_config('common').models.values():
    admin.site.register(model)


def add_default_user(sender, **kwargs):
    if User.objects.count() == 0:
        AccountType.objects.all().delete()
        print 'Creating Account Types'
        for account_type in ['Teacher', 'Parent', 'Student']:
            AccountType.objects.create(name=account_type)


        print 'Creating User'
        user = User.objects.create(
            'tweechy',
            'Peter',
            'tweechy!@#',
            last_name='Saruni',
            middle_name='Njenga',
            account_type = AccountType.objects.get(name='Teacher')
        )

        print 'Creating Default Institution'
        institution = Institution.objects.create(
            name='Starehe Boys Centre',
            created_by=user
        )


# Add default user to database
post_migrate.connect(add_default_user)