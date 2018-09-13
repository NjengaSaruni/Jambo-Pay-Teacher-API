from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from common.models import AbstractBase, Comment, Like
from common.utils import get_unique_number
from divisions.models import ClassLevel, Student, ClassRoom, InstitutionSubject, Class
from uploads.models import File, unique_file_location


class Exam(AbstractBase):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255, blank=True, editable=False)
    class_levels = models.ManyToManyField(ClassLevel, related_name='exams')
    notes = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        if self.created_by.institution is None:
            return '{} - {}'.format(self.name, self.number)
        return '{} - {} - {}'.format(self.created_by.institution.name, self.name, self.number)

    def clean(self):
        if self._state.adding:
            # Assign next visit number in sequence for new visits
            # Add logic to make it unique per project
            if not self.number:
                self.number = get_unique_number(self)

    class Meta:
        app_label = 'exams'


class ExamRegistration(AbstractBase):
    student = models.ForeignKey(Student, related_name='exam_registrations')
    exam = models.ForeignKey(Exam, related_name='exam_registrations')

    def __unicode__(self):
        return '{} - {}'.format(self.created_by.institution.name, self.student.user.last_name, self.exam.name)

    class Meta:
        app_label = 'exams'


class ExamPaper(AbstractBase):
    exam = models.ForeignKey(Exam, related_name='papers')
    subject = models.ForeignKey(InstitutionSubject, related_name='exam_papers')
    start = models.DateTimeField(default=timezone.now, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    total_mark = models.FloatField(blank=True, default=0)
    location = models.ForeignKey(ClassRoom, null=True, blank=True, related_name='papers')
    classes = models.ManyToManyField(Class, blank=True, related_name='papers')
    url = models.FileField(upload_to=unique_file_location, null=True, blank=True)

    def get_end(self):
        try:
            return self.start + self.duration
        except TypeError:
            return self.start

    end = property(get_end)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.created_by.institution.name, self.exam.name, self.subject.name)

    class Meta:
        app_label = 'exams'


class Grade(AbstractBase):
    name = models.CharField(max_length=255)
    ceiling = models.FloatField(blank=True, default=0.00)
    floor = models.FloatField(blank=True, default=0.00)

    def __unicode__(self):
        return '{} - {} - {} - {}'.format(self.created_by.institution.name, self.name, int(self.floor),
                                          int(self.ceiling))

    class Meta:
        app_label = 'exams'

class StudentTotal(object):
    def __init__(self, total=0, rank=None):
        self.total = total
        self.rank = rank



class ClassExamResult(AbstractBase):
    exam = models.ForeignKey(Exam, related_name='class_result')
    _class = models.ForeignKey(Class, related_name='exam_results')
    comments = models.ManyToManyField(Comment, related_name='class_exam_results', blank=True)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.created_by.institution.name, self._class.name, self.exam.name)

    def get_total(self):
        total = 0
        for performance in self.paper_performances.all():
            if performance.mean:
                total += performance.mean

        return total

    total = property(get_total)

    class Meta:
        app_label = 'exams'
        unique_together = ['exam', '_class']


class ClassPaperPerformance(AbstractBase):
    class_result = models.ForeignKey(ClassExamResult, related_name='paper_performances')
    paper = models.ForeignKey(ExamPaper, related_name='class_performance')
    comments = models.ManyToManyField(Comment, related_name='class_paper_performances', blank=True)

    def __unicode__(self):
        return '{} - {}'.format(self.paper.exam.name, self.class_result)

    def get_grade(self):
        if self.mean:
            for grade in Grade.objects.filter(created_by__institution=self.created_by.institution):
                if grade.floor <= self.mean <= grade.ceiling:
                    return grade

    grade = property(get_grade)

    def get_mean(self):
        if self.student_performances.count() > 0:
            return self.total / self.student_performances.count()


    mean = property(get_mean)

    def get_total(self):
        total = 0
        for student_performance in self.student_performances.all():
            total += student_performance.mark

        return total

    total = property(get_total)


    class Meta:
        app_label = 'exams'


class StudentPerformance(AbstractBase):
    student = models.ForeignKey(Student, related_name='student_performances')
    mark = models.FloatField(blank=True, default=0.00)
    grade = models.ForeignKey(Grade, blank=True, null=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    class_performance = models.ForeignKey(ClassPaperPerformance, blank=True, related_name='student_performances')
    comments = models.ManyToManyField(Comment, related_name='student_paper_performances', blank=True)
    likes = models.ManyToManyField(Like, related_name='student_performances', blank=True)
    edited = models.BooleanField(default=True, blank=True)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.created_by.institution.name, self.student.user.last_name, self.mark)


    def get_like_count(self):
        return self.likes.count()

    like_count = property(get_like_count)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if StudentPerformance.objects.filter(id=self.id).exists() and self.mark != StudentPerformance.objects.get(id=self.id).mark:
            fellow_performances = StudentPerformance.objects.filter(class_performance=self.class_performance)

            for performance in fellow_performances:
                better_performances_count = fellow_performances.filter(mark__gt=performance.mark).count()
                performance.rank = better_performances_count + 1
                performance.save()

        if self.mark:
            for grade in Grade.objects.filter(created_by__institution=self.created_by.institution):
                if grade.floor <= self.mark <= grade.ceiling:
                    self.grade = grade
                    break


        super(StudentPerformance, self).save()

    class Meta:
        app_label = 'exams'
        unique_together = ['student', 'class_performance']
        ordering =['student']





