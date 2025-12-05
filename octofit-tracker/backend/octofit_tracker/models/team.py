from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    def __str__(self):
        return self.name