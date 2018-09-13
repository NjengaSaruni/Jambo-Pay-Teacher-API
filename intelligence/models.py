from __future__ import unicode_literals

from django.db import models

from common.models import AbstractBase
from divisions.models import Student, InstitutionSubject, Class

import numpy as np

from exams.models import StudentPerformance


def predict(institution, subject, cls):
    # Step 1 - Prepare data
    performances = StudentPerformance.objects.none()

    if institution is not None:
        performances = StudentPerformance.objects.filter(created_by__institution=institution)

    if subject is not None:
        performances = performances.filter(class_performance__paper__subject=subject)

    if cls is not None:
        performances = performances.filter(class_performance__class_result___class=cls)

    class_prediction_model, _ = ClassSubjectPrediction.objects.get_or_create(
        created_by=cls.created_by,
        subject=subject,
        _class=cls
    )

    for student in cls.students.all():
        student_performances = performances.filter(student=student)

        average_performance = reduce(lambda x, y: x + y,
                                     [performance.mark for performance in student_performances]
                                     ) / student_performances.count()

        latest_performance = student_performances.latest('created_at').mark

        prediction_model, _ = StudentPrediction.objects.get_or_create(
            created_by=cls.created_by,
            class_prediction=class_prediction_model,
            student=student,
            average=average_performance,
            final=latest_performance
        )

    X = np.matrix([prediction.average for prediction in StudentPrediction.objects.filter(
        class_prediction=class_prediction_model)]).T
    Y = np.matrix([prediction.final for prediction in StudentPrediction.objects.filter(
        class_prediction=class_prediction_model)]).T

    return X, Y


def fitModel_gradient(x, y):
    N = len(x)
    w = np.zeros((x.shape[1], 1))
    eta = 0.0001

    maxIteration = 100000
    for i in range(maxIteration):
        error = x * w - y
        gradient = x.T * error / N
        w = w - eta * gradient
    return w


def getMAndC(modelFunction, institution, subject, cls):
    X, Y = predict(institution, subject, cls)
    X = np.hstack([np.matrix(np.ones(len(X))).T, X])

    w = modelFunction(X, Y)

    return w[1].T[0, 0], w[0].T[0, 0]


class ClassSubjectPrediction(AbstractBase):
    subject = models.ForeignKey(InstitutionSubject, null=True, blank=True, related_name='class_predictions')
    _class = models.ForeignKey(Class, null=True, blank=True, related_name='subject_predictions')

    def get_predicted(self):
        institution = self.created_by.institution
        subject = self.subject
        cls = self._class

        m, c = getMAndC(fitModel_gradient, institution, subject, cls)

        return [m, c]

    gradient = property(get_predicted)

    def __unicode__(self):
        return '{}'.format(self.created_by.institution.name)

    class Meta:
        app_label = 'intelligence'


class StudentPrediction(AbstractBase):
    class_prediction = models.ForeignKey(ClassSubjectPrediction, related_name='student_predictions')
    student = models.ForeignKey(Student, related_name='predictions')
    average = models.FloatField(blank=True, default=0.00)
    final = models.FloatField(blank=True, default=0.00)

    def __unicode__(self):
        return '{} - {}'.format(self.created_by.institution.name, self.student.user.last_name)

    class Meta:
        app_label = 'intelligence'
        ordering = ['student']
