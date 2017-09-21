from django.db import models


class Courses(models.Model):
    """Create course model."""

    name = models.CharField(max_length=60, min_length=5)
    desc = models.CharField(max_length=500, min_length=15)
    added = models.DateTimeField(auto_now_add=True)
