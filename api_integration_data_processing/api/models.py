from django.db import models

# Create your models here.
class ClassifyName(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,null=True,blank=True)
    probability = models.FloatField(default=0)
    sample_size = models.IntegerField(default=0)
    is_confident = models.BooleanField(default=False)
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
