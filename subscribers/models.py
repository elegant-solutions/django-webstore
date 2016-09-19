from __future__ import unicode_literals

from django.db import models


class SignUp(models.Model):
    """ Stores a user's sign up information. """
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email
