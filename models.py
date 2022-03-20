from uuid import uuid4

from django.db import models


class CaseFile(models.Model):
    class Meta:
        order = '-pub_date'
    
    _uuid = models.CharField(max_length=36, default='undefined')
    first_name = models.CharField(max_length=40, default='undefined')
    last_name = models.CharField(max_length=40, default='undefined')
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    @property
    def uuid(self):
        return self._uuid

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._uuid = uuid4()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + " " + str(self.id)
