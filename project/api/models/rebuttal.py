"""
Rebuttal model
Extends local Account and Response model
"""

from django.db import models

from .account import Account
from .response import Response


class Rebuttal(models.Model):
    author = models.ForeignKey(
        Account, default=None, null=True, on_delete=models.PROTECT
    )
    response = models.ForeignKey(
        Response, default=None, null=True, on_delete=models.PROTECT
    )

    body = models.TextField(max_length=1023)

    votes_vneg = models.IntegerField(default=0)
    votes_neg = models.IntegerField(default=0)
    votes_neutral = models.IntegerField(default=0)
    votes_pos = models.IntegerField(default=0)
    votes_vpos = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"
