from django.shortcuts import render, redirect
from .models import Student, Courses, Teacher
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CoursesSerializer, TeacherSerializer, StudentSerializer

# Create your views here.
@login_required
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

@login_required
def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

@login_required
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

@login_required
def student_delete_view(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class CoursesView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated]

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]