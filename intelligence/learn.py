import os

import django
from numpy import *

from intelligence.models import StudentPrediction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from exams.models import StudentPerformance
from institutions.models import Institution
from divisions.models import InstitutionSubject, Class

import numpy as np
from matplotlib import pyplot as plt

def predict(institution, subject, cls):

    # Step 1 - Prepare data
    performances = StudentPerformance.objects.none()

    if institution is not None:
        performances = StudentPerformance.objects.filter(created_by__institution=institution)

    if subject is not None:
        performances = performances.filter(class_performance__paper__subject=subject)

    if cls is not None:
        performances = performances.filter(class_performance__class_result___class=cls)


    for student in cls.students.all():
        student_performances = performances.filter(student=student)

        average_performance = reduce(lambda x, y: x + y,
                                     [performance. mark for performance in student_performances]
                                     )/student_performances.count()

        latest_performance = student_performances.latest('created_at').mark

        prediction_model, _ = StudentPrediction.objects.get_or_create(
            created_by=student.created_by,
            subject=subject,
            _class=cls,
            student=student,
            average=average_performance,
            used_to_train=latest_performance
        )

    X = np.matrix([prediction.average for prediction in StudentPrediction.objects.filter(subject=subject)]).T
    print X
    Y = np.matrix([prediction.used_to_train for prediction in StudentPrediction.objects.filter(subject=subject)]).T

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

def plotModel(x, y, w):
    plt.plot(x[:,1], y, "x")
    plt.plot(x[:,1], x * w, "r-")
    print w
    print x * w
    plt.show()

def test(modelFunction, institution, subject, cls):
    X, Y = predict(institution, subject, cls)
    X = np.hstack([np.matrix(np.ones(len(X))).T, X])
    w = modelFunction(X, Y)
    plotModel(X, Y, w)

StudentPrediction.objects.all().delete()

institution = Institution.objects.get(name='Starehe Boys Centre')
subject = InstitutionSubject.objects.get(name='Biology')
cls = Class.objects.get(name='Form Four - Green')

test(fitModel_gradient, institution, subject, cls)