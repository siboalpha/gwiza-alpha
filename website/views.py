from django.shortcuts import redirect, render
from .forms import ContactFrom
# Create your views here.

def index(request):
    form = ContactFrom()

    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form}
    return render(request, 'index.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')
