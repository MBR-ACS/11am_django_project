from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.
def student_creation_view(request):
    if request.method == 'POST':
        form  = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("***Form is Submitted***")
            return redirect('student_list')
        else:
            return HttpResponse("***Form Submition failed***")
    form  = StudentForm()
    return render(request, 'student/student_create.html', {'form': form})

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_edit_view(request, id):
    student = Student.objects.get(id=id) # select * from students where id = 1
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # return HttpResponse("Form Updated Successfully")
            return redirect('student_list')
        else:
            return HttpResponse("Form Submition faield.")
    
    form = StudentForm(instance=student)
    return render(request, 'student/edit_student.html', {'form' : form})

def student_delete_view(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')


