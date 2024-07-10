from django.db import models

class Variant(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)

class Question(models.Model):
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_option = models.CharField(max_length=50)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

class UserAnswer(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=50)
