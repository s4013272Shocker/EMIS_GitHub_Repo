from django.db import models

# Create your models here.
class ExamReport(models.Model):
    moduleName = models.CharField(max_length = 200)
    reportText = models.TextField(max_length = 800)