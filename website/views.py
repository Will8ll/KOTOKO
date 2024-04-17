# views.py
from django.shortcuts import render
from .forms import BMICalculationForm

def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def home(request):
    bmi = None
    if request.method == 'POST':
        form = BMICalculationForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            bmi = calculate_bmi(height, weight)
    else:
        form = BMICalculationForm()
    return render(request, 'index.html', {'form': form, 'bmi': bmi})