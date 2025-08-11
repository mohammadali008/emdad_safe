from django.shortcuts import render, redirect
from .forms import ContactRequestForm

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/?submitted=true')
    else:
        form = ContactRequestForm()
    return render(request, 'contact/contact_form.html', {'form': form})
