from django.urls import path
from .views import choose_variant, enter_key, start_test, submit_answers, result

urlpatterns = [
    path('', choose_variant, name='choose_variant'),
    path('enter_key/<int:variant_id>/', enter_key, name='enter_key'),
    path('start_test/<int:variant_id>/<str:access_key>/', start_test, name='start_test'),
    path('submit/', submit_answers, name='submit_answers'),
    path('result/', result, name='result'),
]
