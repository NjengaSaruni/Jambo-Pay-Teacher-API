# Generates a unique number that is used as a human friendly identifier
# Good thing its sequenced by date make items easy to find to
from random import randint

from django.utils import timezone
from sklearn.linear_model import LinearRegression


def unique_file_name(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.id, extension)
    return '/'.join([str(instance.created_at.date()), filename])


def get_unique_number(self):
    try:
        latest_object = type(self).objects.filter(created_by__institution=self.institution).latest('created_at')
        number = latest_object.number
        if number[:6] == timezone.now().date().strftime("%Y%m"):
            return number[:6] + format(int(number[-2:], 16) + 1, 'X').zfill(2)
        return str(timezone.now().date().strftime("%Y%m")) + '00'

    except:
        return str(timezone.now().date().strftime("%Y%m")) + '00'


