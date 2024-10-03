from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Course_Module
from .forms import BlogForm, CourseModuleForm

# Downlod PDf 
from django.http import HttpResponse
from .models import Course_Module
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required




# Blog Views
@login_required(login_url='login')
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})
@login_required(login_url='login')
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

@login_required(login_url='login')
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_form.html', {'form': form})


@login_required(login_url='login')
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blogs/blog_confirm_delete.html', {'blog': blog})

# Course Module Views
@login_required(login_url='login')
def course_module_list(request):
    modules = Course_Module.objects.all()
    return render(request, 'blogs/course_module_list.html', {'modules': modules})
@login_required(login_url='login')
def course_module_detail(request, pk):
    module = get_object_or_404(Course_Module, pk=pk)
    return render(request, 'blogs/course_module_detail.html', {'module': module})

@login_required(login_url='login')
def course_module_create(request):
    if request.method == 'POST':
        form = CourseModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_module_list')
    else:
        form = CourseModuleForm()
    return render(request, 'blogs/course_module_form.html', {'form': form})

@login_required(login_url='login')
def course_module_update(request, pk):
    module = get_object_or_404(Course_Module, pk=pk)
    if request.method == 'POST':
        form = CourseModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('course_module_detail', pk=module.pk)
    else:
        form = CourseModuleForm(instance=module)
    return render(request, 'blogs/course_module_form.html', {'form': form})

@login_required(login_url='login')
def course_module_delete(request, pk):
    module = get_object_or_404(Course_Module, pk=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('course_module_list')
    return render(request, 'blogs/course_module_confirm_delete.html', {'module': module})

@login_required(login_url='login')
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)  # Redirect to the detail view after saving
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/update_blog.html', {'form': form})

@login_required(login_url='login')
def download_pdf1(request, pk):
    module = Course_Module.objects.get(pk=pk)
    template_path = 'pdf/download_pdf.html'  # Specify your template path here
    context = {'module': module}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{module.course_name}.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response
