from django.db import models
from reversion import revisions as reversion

from common.models import AbstractBase, Subject, Color
from users.models import User


class InstitutionSubject(AbstractBase):
    name = models.CharField(max_length=255)
    field = models.ForeignKey(Subject, related_name='institution_subjects')

    def __unicode__(self):
        return '{} - {}'.format(self.created_by.institution, self.field.name)

    class Meta:
        app_label = 'divisions'

class Stream(AbstractBase):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    color = models.ForeignKey(Color, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        app_label = 'divisions'



@reversion.register
class ClassLevel(AbstractBase):
    name = models.CharField(max_length=255)
    value = models.PositiveSmallIntegerField(default=1)

    # def __unicode__(self):
    #     # return '{} - {} : {}'.format(self.created_by.institution.name, self.name, self.value)

    class Meta:
        app_label = 'divisions'


class Class(AbstractBase):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(null=True, blank=True)
    level = models.ForeignKey(ClassLevel, null=True, blank=True, related_name='classes')
    stream = models.ForeignKey(Stream, null=True, blank=True, related_name='classes')
    year = models.PositiveIntegerField(default=2017)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.level.name + ' - ' + self.stream.name

        return super(Class, self).save(force_insert, force_update, using, update_fields)

    # def __unicode__(self):
    #     return '{} - {}'.format(self.created_by.institution.name, self.name)

    class Meta:
        app_label = 'divisions'


@reversion.register
class Parent(AbstractBase):
    user = models.OneToOneField(User, related_name='parent', null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        if self.created_by.institution is None:
            return '{}'.format(self.user.last_name)
        return '{} - {}'.format(self.created_by.institution.name, self.user.last_name)

    class Meta:
        app_label = 'divisions'


@reversion.register
class Student(AbstractBase):
    user = models.OneToOneField(User, related_name='student', null=True, blank=True)
    current_class = models.ForeignKey(Class, related_name='students', null=True, blank=True)
    registration_number = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey(Parent, related_name='students', null=True, blank=True)

    def __unicode__(self):
        if self.created_by.institution is None:
            return '{}'.format(self.user.last_name)
        return '{} - {}'.format(self.created_by.institution.name, self.user.last_name)

    class Meta:
        app_label = 'divisions'
        ordering = ['user',]

class StudentComment(AbstractBase):
    student = models.ForeignKey(Student, related_name='comments')
    comment = models.TextField()
    notified = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        if self.created_by.institution is None:
            return '{}'.format(self.student.user.full_name)
        return '{} - {}'.format(self.created_by.institution.name, self.student.user.full_name)

    class Meta:
        app_label = 'divisions'
        ordering = ['-created_at']

@reversion.register
class Teacher(AbstractBase):
    user = models.OneToOneField(User, related_name='teacher', null=True, blank=True)
    subjects = models.ManyToManyField(InstitutionSubject, related_name='teachers', blank=True)
    classes = models.ManyToManyField(Class, related_name='teachers', blank=True)
    class_teacher_of = models.OneToOneField(Class, related_name='class_teacher', blank=True, null=True)

    def __unicode__(self):
        if self.created_by.institution is None:
            return '{}'.format(self.user.last_name)
        return '{} - {}'.format(self.created_by.institution.name, self.user.last_name)

    class Meta:
        app_label = 'divisions'

class ClassRoom(AbstractBase):
    name = models.CharField(max_length=255)
    occupants = models.PositiveIntegerField(default=0, blank=True)
    current_class = models.OneToOneField(Class, related_name='room', null=True, blank=True)

    def __unicode__(self):
        if self.created_by.institution is None:
            return '{}'.format(self.name)
        return '{} - {}'.format(self.created_by.institution.name, self.name)


    class Meta:
        app_label = 'divisions'

#
# class DivisionsReport(AbstractBase):
#     def get_student_count():