from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.

def student_list(request):   # Function based View.
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_create(request):
    '''if user submits the form by clicking the subit button, the the request is 'POST' '''
    # if request.method == 'POST':
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("Sudent Details Submitted")
    #     else:
    #         return HttpResponse("Form Submittion Failed.")
    # else:
    form = StudentForm()
    return render(request, 'student/student_create.html', {'form': form})
    '''if user request to add a student , so it is GET method. then this function returns and renders the empty form.'''

