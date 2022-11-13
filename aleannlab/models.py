from django.db import models


class Rank(models.Model):
    rank_name = models.CharField(max_length=255)
    queue = models.IntegerField()

    def __str__(self):
        return self.rank_name


class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name









