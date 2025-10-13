from django.urls import path, include
from student import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student/', views.StudentView, basename='student')
router.register('course/', views.CoursesView, basename='course')
router.register('teacher/', views.TeacherView, basename='teacher')

urlpatterns = [
    path('add_student/', views.student_creation_view, name='add_student'),
    path('student_list/', views.student_list_view, name='student_list'),
    path('edit_student/<int:id>', views.student_edit_view, name='edit_student'),
    path('delete_student/<int:id>', views.student_delete_view, name='delete_student'), 
    path('', include(router.urls)),
]