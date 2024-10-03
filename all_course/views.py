from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm  # You'll create this form next
from django.contrib.auth.decorators import login_required

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'all_course/course_list.html', {'courses': courses})

@login_required(login_url='login')
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'all_course/course_detail.html', {'course': course})

@login_required(login_url='login')
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'all_course/course_form.html', {'form': form})

@login_required(login_url='login')
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'all_course/course_form.html', {'form': form})

@login_required(login_url='login')
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'all_course/course_confirm_delete.html', {'course': course})
@login_required(login_url='login')
def course_box(request):
    courses = Course.objects.all()
    return render(request, 'all_course/course_box.html')