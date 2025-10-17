from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log-in')
        else:
            return HttpResponse("*** Form Submition is Failed ***")
        
    form = SignUpForm()
    return render(request,'registration/sign_up.html', {'form':form})