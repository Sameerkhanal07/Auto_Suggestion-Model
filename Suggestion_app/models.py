from django.db import models
from django.contrib.postgres.fields import ArrayField 

class KatahoWord(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    plus_code = models.CharField(max_length=20, blank=True, null=True)
    kataho_code = models.CharField(max_length=255)  # main text
    roman_code = models.CharField(max_length=255, blank=True, null=True)
    hint = models.CharField(max_length=255, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    hints = models.JSONField(blank=True, null=True)  # store ["अक्षर","Akshar"]
    meanings = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("kataho_code", "roman_code") 

    def __str__(self):
        return self.kataho_code


