from django.db import models


class TagDesc(models.Model):
    tags = models.CharField(max_length=30)
    desc = models.TextField()

    class Meta:
        abstract = True

class Solution(TagDesc):
    pass

class Need(TagDesc):
    solutions = models.ManyToManyField(Solution, through='IsSolution')

class Sugestion(TagDesc):
    pass

class IsSolution(models.Model):
    need = models.ForeignKey(Need)
    solution = models.ForeignKey(Solution)
    pos = models.IntegerField()
    desc = models.TextField()
    dt_added = models.DateTimeField()
    source = models.CharField(max_length=100)
