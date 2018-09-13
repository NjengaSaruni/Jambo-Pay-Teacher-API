from __future__ import unicode_literals
from reversion import revisions as reversion

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

from common.models import AbstractBase, Person
from uploads.models import File


@reversion.register
class Genre(AbstractBase):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '{} - {}'.format(self.institution.name, self.name)

    class Meta:
        app_label = 'library'

@reversion.register
class Author(AbstractBase):
    person = models.ForeignKey(Person)
    genre = models.ForeignKey(Genre, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ratings = GenericRelation(Rating, related_query_name='authors')

    def __unicode__(self):
        return '{} - {}'.format(self.institution.name, self.person.last_name)

    class Meta:
        app_label = 'library'

@reversion.register
class BookType(AbstractBase):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '{} - {}'.format(self.institution.name, self.name)

    class Meta:
        app_label = 'library'


@reversion.register
class Book(AbstractBase):
    title = models.CharField(max_length=255)
    type = models.ForeignKey(BookType, null=True, blank=True)
    file = models.OneToOneField(File, null=True, blank=True, related_name="book")
    subject = models.CharField(max_length=255, null=True, blank=True)
    ISBN = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author,null=True, blank=True)

    def clean(self):
        if not self.title:
            self.title = self.file.title

    def __unicode__(self):
        return '{} - {}'.format(self.institution.name, self.title)

    class Meta:
        app_label = 'library'