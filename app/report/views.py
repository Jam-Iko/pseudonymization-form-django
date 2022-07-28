from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PseudoFunctionSelectionForm

def index(request):
    return render(request, 'report/index.html')


def select_pseudo(request):
    context = {}
    if request.method == 'POST':
        form = PseudoFunctionSelectionForm(request.POST)
        if form.is_valid():
            context['pseudo_function'] = form.evaluate_form()
            return render(request, 'report/index.html', context)
        return redirect('select-pseudo-view')
    else:
        form = PseudoFunctionSelectionForm()
    context = {
        'form': form
    }
    return render(request, 'report/select_pseudo.html', context)