from django.shortcuts import render, redirect

from .models import Person, State
from .forms import PersonForm

def person_create_view(request):
    form  = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'home.html', {'form': form})

def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id)
    return render(request, 'state.html', {'states': states})