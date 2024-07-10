from django.shortcuts import render, redirect
from .models import Variant, Question, UserAnswer
from django import forms

class AccessKeyForm(forms.Form):
    access_key = forms.CharField(label='Access Key', max_length=50)

def choose_variant(request):
    variants = Variant.objects.all()

    if request.method == 'POST':
        form = AccessKeyForm(request.POST)
        if form.is_valid():
            access_key = form.cleaned_data['access_key']
            variant_id = request.POST.get('variant_id')

            try:
                variant = Variant.objects.get(pk=variant_id, key=access_key)
            except Variant.DoesNotExist:
                print(f"Invalid access key {access_key} for variant {variant_id}")
                return render(request, 'python_test_app/choose_variant.html', {'variants': variants, 'form': form})

            print(f"Valid access key {access_key} for variant {variant_id}")
            return redirect('start_test', variant_id=variant_id, access_key=access_key)
    else:
        form = AccessKeyForm()

    return render(request, 'python_test_app/choose_variant.html', {'variants': variants, 'form': form})


def enter_key(request, variant_id):
    variant = Variant.objects.get(pk=variant_id)
    return render(request, 'python_test_app/enter_key.html', {'variant': variant})

def start_test(request, variant_id, access_key):
    questions = Question.objects.filter(variant_id=variant_id)
    context = {'questions': questions, 'access_key': access_key}
    return render(request, 'python_test_app/index.html', context)


def submit_answers(request):
    if request.method == 'POST':
        access_key = request.POST.get('access_key')
        for question_id, selected_option in request.POST.items():
            if question_id.isdigit():
                question = Question.objects.get(pk=question_id)
                if question.variant.key == access_key:
                    UserAnswer.objects.create(
                        user_id=1,  # Change this to the actual user ID
                        question=question,
                        selected_option=selected_option
                    )
        return redirect('result')
    else:
        return redirect('choose_variant')

def result(request):
    user_answers = UserAnswer.objects.filter(user_id=1)  # Change this to the actual user ID
    correct_answers = 0
    total_questions = len(user_answers)

    for user_answer in user_answers:
        if user_answer.selected_option == user_answer.question.correct_option:
            correct_answers += 1

    context = {
        'user_answers': user_answers,
        'correct_answers': correct_answers,
        'total_questions': total_questions,
    }
    return render(request, 'python_test_app/result.html', context)