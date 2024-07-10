from django.contrib import admin
from .models import Question, Variant, UserAnswer

admin.site.register(Question)
admin.site.register(Variant)
admin.site.register(UserAnswer)

